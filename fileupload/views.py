# encoding: utf-8
import json
import csv
import re
import sys
import os
import csv

from django.http import HttpResponse
from django.conf import settings
from django.views.generic import CreateView, DeleteView, ListView
from .models import Picture
from .response import JSONResponse, response_mimetype
from .serialize import serialize

class DocumentCreateView(CreateView):
    model = Picture
    fields = "__all__"

    def form_valid(self, form):
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'    
        name = self.object.file.name
        output_name = self.object.slug
        file = str(name)

        with open(("Vulcan/media/%s") %file, 'rU') as csvfile, open(("Vulcan/media/documents/customer_zaius_output.csv"), 'wb') as output:
            results = []
            apostrophe = []

            writer = csv.writer(output)
            readCSV = csv.reader(csvfile, delimiter = ',')
            writer.writerow(["email"])
            next(readCSV)

            for row in readCSV:
                address = row

                if address == []:
                    next(readCSV)

                else:
                    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z0-9-]+)*(\.[a-z0-9-]+)*(\.[a-z0-9-]+)$', address[0].lower())
                    if match != None:
                        writer.writerow(address)

                    else:
                        sub = re.sub('[\xc2\xc3\xa3\xbe\x8e\xae\x83\xa8\xc4\xca;]','', address[0].lower())
                        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z0-9-]+)*(\.[a-z0-9-]+)$', sub)

                        if match != None:
                            writer.writerow([sub])

                        else:
                            results.append(address[0])
    
            for test in results:
                match = re.search(r"'", test.lower())
                if match != None:
                    apostrophe.append([test])
                else:
                    writer.writerow(["FIX THIS EMAIL: %r " % test])

            for item in apostrophe:
                writer.writerow([item])

            writer.writerow(["sean.mbogo@sothebys.com"])
            writer.writerow(["clara.pascal@sothebys.com"])
            writer.writerow(["nanxi.fan@sothebys.com"])
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')

class BasicVersionCreateView(DocumentCreateView):
    template_name_suffix = '_basic_form'


class PictureDeleteView(DeleteView):
    model = Picture

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class PictureListView(ListView):
    model = Picture

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
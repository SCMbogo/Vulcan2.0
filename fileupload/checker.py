import csv
import re
import sys
import os

file = 'myFile.csv'

def main():
	email_row_deleter(file)
	email_splitter(file)
	email_splitter_1(file)
	email_trimmer(file)
	email_checker(file)

def email_row_deleter(file):
	with open(file, 'rU') as csvfile, open(('temp_%s' % file), 'wb') as output:
		writer = csv.writer(output)
		readCSV = csv.reader(csvfile, delimiter = ',')
		
		writer.writerow(["email"])
		next(readCSV)

		for row in readCSV:
			address = row

			if address == []:
				next(readCSV)
			else:
				writer.writerow(address)	


def email_splitter(file):
	with open(('temp_%s' % file), 'rU') as csvfile, open(('temp_2_%s' % file), 'wb') as output:
		writer = csv.writer(output)
		readCSV = csv.reader(csvfile, delimiter = ',')
		
		writer.writerow(["email"])
		next(readCSV)
		
		sep = ';'
		for row in readCSV:
			address = row

			match = re.search(r';', address[0])	
			if match != None:
					address = address[0]
					address_one = address.split(sep,1)[0]
					writer.writerow([address_one])

					if address.split(sep,1)[1] != None :
						address_two = address.split(sep,1)[1]
						writer.writerow([address_two])

			else:
				writer.writerow(address)

def email_splitter_1(file):
	with open(('temp_2_%s' % file), 'rU') as csvfile, open(('temp_3_%s' % file), 'wb') as output:
		writer = csv.writer(output)
		readCSV = csv.reader(csvfile, delimiter = ',')
		
		writer.writerow(["email"])
		next(readCSV)
		
		sep = ';'
		for row in readCSV:
			address = row

			match = re.search(r';', address[0])	
			if match != None:
					address = address[0]
					address_one = address.split(sep,1)[0]
					writer.writerow([address_one])

					if address.split(sep,1)[1] != None :
						address_two = address.split(sep,1)[1]
						writer.writerow([address_two])

			else:
				writer.writerow(address)

def email_trimmer(file):
	with open(('temp_3_%s' % file), 'rU') as csvfile, open(('temp_4_%s' % file), 'wb') as output:
		writer = csv.writer(output)
		readCSV = csv.reader(csvfile, delimiter = ',')
		
		writer.writerow(["email"])
		next(readCSV)
		
		for row in readCSV:
			address = row

			if address == []:
				next(readCSV)			
			
			else:
				address = row[0]
				address.strip()
				address = re.sub(' ', '',address)
				writer.writerow([address])	


def email_checker(file):
	results = []

	with open(('temp_4_%s' % file), 'rU') as csvfile, open(('customer_zaius_%s' % file), 'wb') as output:
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
				writer.writerow([test])
			else:
				writer.writerow(["FIX THIS EMAIL: %r " % test])

		writer.writerow(["sean.mbogo@sothebys.com"])
		writer.writerow(["clara.pascal@sothebys.com"])
		writer.writerow(["nanxi.fan@sothebys.com"])

	os.remove(('temp_%s' % file))
	os.remove(('temp_2_%s' % file))
	os.remove(('temp_3_%s' % file))
	os.remove(('temp_4_%s' % file))

main()

	

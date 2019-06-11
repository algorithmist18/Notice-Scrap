"""
		A small automation tool so that I never forget when a new notice arrives
"""

#Importing libraries
import requests
import re
import os
from bs4 import BeautifulSoup
import datetime

#Cleaning up data
def clean_up(s):

	data = s.text
	data = data.rstrip("\n")
	data = re.sub(r'To view notice', '', data)
	data = re.sub(r'Click here', '', data)
	data = re.sub(r'Notice reg.', '\n', data)
	data = re.sub(r'[\n\r]+', '\n', data)
	data = data.rstrip("\n")

	return data	

def extract_date(s):

	datetime.datetime.strptime(s, "%d/%m/%y")
	return date.day, date.month, date.year

def is_date(s):


	if s[2] == '/' or s[2] == '.' or s[2] == '-':
		d = int(s[0:2])
		#print(d)
		if d >= 1 and d <= 31:
			m = int(s[3:5])
			#print(m)
			if m >= 1 and m <= 12:
				y = int(s[6:])
				if y >= 1:
					return True
	return False
	"""
	except:
		return False
	"""
def is_noticehead(s):

	pass
#Data structures
headers = []
dates = []
pdfs = []

#Regular expressions
notice_header = "ct100_ContentPlaceHolder1_Repeater3_"

url = 'http://www.heritageit.edu/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
s = soup.find("div", {"id" : "notice"})

data = clean_up(s)
#print(data)

#Writing to file
f = open('notice.txt', 'w')
f.write(data)
f.close()

print(is_date('11-02-2031'))

#Reading from file line by line
f = open('notice.txt', 'r')
for line in f:
	line = line.strip()
	if len(line) == 10 and is_date(line):
		print('Date = {}'.format(line))
f.close()
#Extracting PDF URL
urls = s.find_all('a', href = True)
p = 0
for url in urls:
	pdf = url['href']
	pdf_url = 'http://www.heritageit.edu/' + pdf
	print(pdf_url)	
	p = p + 1
	response = requests.get(pdf_url)
	#file_name = 'pdf' + str(p) + '.pdf'
	f = open(pdf[10:], 'wb+')
	f.write(response.content)




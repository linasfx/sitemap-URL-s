from bs4 import BeautifulSoup
import requests

url = raw_input("Enter a website URL: ")
url=('http://'+url)

r  = requests.get(url)                       
site_map="/sitemap.xml"

def site(xml):
	import urllib
	import re
	xml_data =urllib.urlopen(url+site_map)
	count=0
	xml_list=list()
	xml_list2=list()	
	for line in xml_data:
		x=re.findall('loc>(.+)</loc',line)
		if len(x)>0: 
			count=count+1
			xml_list.append(x)	
	for line2 in xml_list:
		for url2 in line2:
			xml_list2.append(url2)
			print url2
	
	return "Number of URL's extracted:",count

req=requests.head(url+site_map)              #<Response [200]>  
status_code=req.status_code

if status_code==200:
	print site(url)
else:
	print "No sitemap.xml.","Status code=",status_code

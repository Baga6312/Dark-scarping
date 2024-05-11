from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import json 
import threading
import sys 
keywords = []
if sys.argv[2] not in ["and" , "or "] : 
	keywords = sys.argv[2:]
else : 
	keywords = sys.argv[3:]
 
Topic = sys.argv[1]

nk = len(sys.argv[1:])
logic = sys.argv[1]
if nk > 1 :
	while  not logic in ['and','or']:
		logic = 'and'
		if not logic in ['and' , 'or'] :
			print("wrong input")
else :
	logic = "and"

def scrap_content(elem,keywords,logic= 'and') :
	results = []
	try :
		requests = RequestsTor(tor_ports=(9050,), tor_cport= 9051)
		r = requests.get(elem)
		if r.status_code == 200 :
			content = r.text
			if logic == 'and' :
				if all(keyword.lower() in content.lower() for keyword in keywords) : 
					
					results.append({
					'logic' : logic ,
					'url' : elem 
					})
			elif logic == 'or' :
				if all(keyword.lower() in content.lower() for keyword in keywords) : 
					results.append({
					'logic' : logic ,
					'url' : elem 
					})
	except Exception as e :
		pass
	return results

def scrap_site(url) :  
	requests = RequestsTor(tor_ports=(9050,), tor_cport= 9051)
	
	r = requests.get(url)
	
	soup = BeautifulSoup(r.text, 'html.parser')
	
	  
	sites_links = []
	
	links = soup.find_all('a', href = True)
	All_links = [link['href'] for link in links if link['href']]
	sites_links.append(All_links)
	return sites_links
	
		
def scrap_AHMIA(Topic,keywords) :
	url = 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q=' + Topic
	sites_links = scrap_site(url)
	for http_links in sites_links :
		for http_link in http_links :
			if http_link.startswith('/') :
				sites_links.append(http_link[(43 + len(Topic)):])
	for final_link in sites_links :
		results = scrap_content(final_link,keywords,logic=logic)
		if results :
			print("Ahmia " ,  results)


def scrap_Company_Leaks(Topic,keywords) :
	url = 'http://relateoak2hkvdty6ldp7x67hys7pzaeax3hwhidbqkjzva3223jpxqd.onion/' +  Topic + '/'
	sites_links = scrap_site(url)
	for elem in sites_links :
		for e in elem :
			e = ('http://relateoak2hkvdty6ldp7x67hys7pzaeax3hwhidbqkjzva3223jpxqd.onion' + e )
			results = scrap_content(e,keywords,logic=logic)
	if results :
		print("RelateList" )
	

def scrap_NOT_EVIL(Topic,keywords) :
	url = 'http://notevilmtxf25uw7tskqxj6njlpebyrmlrerfv5hc4tuq7c7hilbyiqd.onion/index.php?q=' + Topic
	sites_links = scrap_site(url)
	for http_links in sites_links :
		for http_link in http_links :
			if http_link.startswith('/ch'):
					sites_links.append(http_link[8:])
			elif http_link.startswith('/co'):
					sites_links.append(http_link[37:])
	for elem in sites_links[10:15] :
		results = scrap_content(elem,keywords,logic=logic)
		if results :
			print("NotEvil " , results) 

thread1 = threading.Thread(target=scrap_Company_Leaks(Topic,keywords))
thread2 = threading.Thread(target=scrap_NOT_EVIL(Topic,keywords))
thread3 = threading.Thread(target=scrap_AHMIA(Topic,keywords))


thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("All functions executed.")
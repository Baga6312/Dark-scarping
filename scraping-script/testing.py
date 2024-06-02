from requests_tor  import RequestsTor
from bs4 import BeautifulSoup  

request = RequestsTor(tor_ports=(9050,) , tor_cport=9051)

url ="http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion"

keyword ="actia"


def SCRAP_AHMIA (url , keyword) : 
    online_link = []
    rq = request.get(url+"/search/"+"?q="+keyword+"+")
    cite = BeautifulSoup(rq.text , 'html.parser').find_all('cite')  

    for site in cite : 
        online_link.append(site.get_text())
    
    for link in online_link : 
        print (link)
        rq1 = request.get("http://" +link)

        if str(rq1) == "<Response [200]>" : 
            soup = BeautifulSoup(rq1.text, 'html.parser')
            keyword_occ = soup.find(keyword)
    
            if keyword_occ  : 
                print (keyword + " found in " + link)
            else : 
                print ("not found ")
    
        elif str(rq1) == "<Response [200]>" : 
            print ("site is unreacheable")



def SCRAP_RELATE_LIST (url , keyword) : 
    rq = request.get(url+'/'+keyword+'/') 
    soup = BeautifulSoup(rq.text , 'html.parser').find_all("span" , class_="title")[0].get_text()

    if soup == "Nothing found for '"+keyword+"'" : 
        return "nothing to be found"
    else : 
        return "found in relateList"

SCRAP_AHMIA(url, keyword )

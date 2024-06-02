from requests_tor  import RequestsTor
from bs4 import BeautifulSoup  






request = RequestsTor(tor_ports=(9050,) , tor_cport=9051)

url ="http://notevilmtxf25uw7tskqxj6njlpebyrmlrerfv5hc4tuq7c7hilbyiqd.onion"
keyword ="actia"


def SCRAP_AHMIA (url , keyword) : 
    online_link = []
    rq = request.get(url+"/search/"+"?q="+keyword+"+")
    cite = BeautifulSoup(rq.text , 'html.parser').find_all('cite')  

    for site in cite : 
        online_link.append(site.get_text())
    
    for link in online_link : 
        rq = request.get("http://" +link)
        if rq == "<Response [200]>" : 
            soup = BeautifulSoup(rq.text, 'html.parser')
            keyword = soup.find(keyword)
    
            if keyword : 
                return keyword + " found in " + link
            else : 
                return "not found "
    
        elif rq != "<Response [200]>" : 
            print ("site is unreacheable")



def SCRAP_RELATE_LIST (url , keyword) : 
    rq = request.get(url+'/'+keyword+'/') 
    soup = BeautifulSoup(rq.text , 'html.parser').find_all("span" , class_="title")[0].get_text()

    if soup == "Nothing found for '"+keyword+"'" : 
        return "nothing to be found"
    else : 
        return "found in relateList"



# riglha mbaad ki yet7al 
def SCRAP_NOT_EVIL(url , keyword) : 

    rq = request.get(url) 
    soup = BeautifulSoup(rq.text , 'html.parser')
    print (soup)

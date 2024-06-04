from requests_tor  import RequestsTor
from bs4 import BeautifulSoup  

request = RequestsTor(tor_ports=(9050,) , tor_cport=9051)

url ="haystak2wfqmtftctncw7hj6p6glevgffy5b7uios7fypaocbucmehad.onion"

keyword ="actia"

          #######################
          ##                   ##
          ##        AHMIA      ##
          ##                   ##
          #######################

def SCRAP_AHMIA (url , keyword) : 
    online_link = []
    rq = request.get(url+"/search/"+"?q="+keyword+"+")
    cite = BeautifulSoup(rq.text , 'html.parser').find_all('cite')  

    for site in cite : 
        online_link.append(site.get_text())
    
    for link in online_link : 

        try : 

            rq1 = request.get("http://" +link)
            rq1.raise_for_status()
            soup = BeautifulSoup(rq1.text, 'html.parser')
            keyword_occ = soup.find(keyword)
    
            if keyword_occ  : 
                print ("found")
                break 
            else : 
                print ("not found")

        except Exception :
            print("site is unreachable")

         #######################
         ##                   ##
         ##    Relate_List    ##
         ##                   ##
         #######################    
       
def SCRAP_RELATE_LIST (url , keyword) : 

    try : 
        rq = request.get(url+'/'+keyword+'/') 
        soup = BeautifulSoup(rq.text , 'html.parser').find_all("span" , class_="title")[0].get_text()
    
        if str(soup) == "Nothing found for '"+keyword+"'" : 
            print ("not found")
        else : 
            print ("found")
    
    except Exception :
        print("site is unreachable")


         #######################
         ##                   ##
         ##    Ransom_EXX     ##
         ##                   ##
         #######################    

def SCRAP_RANSOM_EXX (url , keyword , pages , n ) : 

        try:
            urll ="http://" + url + pages + "/index.html"
            print (urll)
            rq = request.get(urll )
            soup = BeautifulSoup(rq.text, 'html.parser').find_all("a", href=True)
            print(rq)

            found = False
            for sip in soup:
                if sip.get_text() == keyword:
                    print("found")
                    found = True
                    break

            if not found:
                print("not found")

            n += 1
            pages = "/page/" + str(n)
            SCRAP_RANSOM_EXX(url, keyword, pages, n)

        except Exception as e:
            print("site is unreachable" , e)
    

         #######################
         ##                   ##
         #  Dark_Leak_Market  ##
         ##                   ##
         #######################

def SCRAP_DARK_LEAK_MARKET (url , keyword ) : 

    found_not_found = "not found"
    try : 
        rq = request.get("http://"+url)
        soup = BeautifulSoup(rq.text , 'html.parser').find_all("a" , href=True)   

        for sip in soup : 
            souper = sip.get_text()
            if keyword not in souper.split(" ") :
               pass 
            
            else  : 
                found_not_found = "found"
                break 

            
    except Exception : 
        print('site is unreachable')
    print(found_not_found)

         
         
        #######################
        ##                   ##
        ##  Hidden_Answer    ##
        ##                   ##
        #######################

def SCRAP_HAYSTAK(url , keyword  ) :

    try : 
        rq = request.get("http://"+url+"?q="+keyword)
        soup = BeautifulSoup(rq.text , 'html.parser').find_all("div" ,class_="result")

        if soup : 
            print ("found")
        else : 
            print ("not found")

    except Exception : 
        print("site is unreachable")


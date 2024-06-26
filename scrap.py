from requests_tor  import RequestsTor
from bs4 import BeautifulSoup  

request = RequestsTor(tor_ports=(9050,) , tor_cport=9051)

keyword = "esprit"

def SCRAP_ALL (siteName, url , key , tag , className , afterLink) :  

    try : 
        found_not_found = "not found"        
        urll = "http://"+url+afterLink + key  
        print (urll)
        rq = request.get(urll )
        soup = BeautifulSoup(rq.text , 'html.parser').find_all(tag , className)  


        for sip in soup : 

            if keyword in ((sip.get_text().lower()).split()) : 
                found_not_found = "found"
                break
            else : 
                pass 


        print(found_not_found + " in " + siteName)

    except Exception : 
        print ("site is unavailble")
    

# TODO
# do ur fking testing 

# SCRAP_ALL("juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion" , "actia" , "li" , "result" , "/search/?q=" )
# SCRAP_ALL("darkleakyqmv62eweqwy4dnhaijg4m4dkburo73pzuqfdumcntqdokyd.onion" , "" , "strong" , "" , "" )
# SCRAP_ALL("haystak2wfqmtftctncw7hj6p6glevgffy5b7uios7fypaocbucmehad.onion" , "actia" , "a" , "" , "/?q=" )
# SCRAP_ALL("relateoak2hkvdty6ldp7x67hys7pzaeax3hwhidbqkjzva3223jpxqd.onion" , "" , "a" , "" , "/"+keyword+"/" )

# sala7 torch , ali ta7t jomla hedhi 
# SCRAP_ALL("xmh57jrfg4ilgp2ci6nq3tyeapr4pbdepouxfpa6nuc364shsjyifgyd.onion" , "actia" , "small" , "" , "/cgi-bin/omega/omega?P=" )

# sala7 hedhi  maa lo5ra 
# SCRAP_ALL("2fd6cem3xk6fkkynap3ewhzy2rybrmeigu2lm2bxcoaayxfka2df7syd.onion" , "actia" , "p" , "  text-truncate" , "/search/")
# SCRAP_ALL("oniwayztpfv4wpawasbc7cavzjdvb3dwwtlizumjvcu7y3tqqic7dxqd.onion" , "actia" , "p" , "desc" , "/search.php?s=")
#SCRAP_ALL("orealmvo7j6kfixcz7x3yjmlc2szw3j3qugcfuwas2trtnt6mbp7v2ad.onion" , "" , "a" , "" , "/search?query="+keyword+"&action=search")
# SCRAP_ALL("darksidthvquha52o4fzvtap4ticaoh4sboobywadzkvcbjzhtapadyd.onion" , "actia" , "td" , "" , "/?k=")


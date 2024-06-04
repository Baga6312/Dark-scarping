import threading

from requests_tor  import RequestsTor
from bs4 import BeautifulSoup  
from testing import SCRAP_ALL 

request = RequestsTor(tor_ports=(9050,) , tor_cport=9051)
filename="data_leaks_sites.txt"

# getting onion sites from an external file 
def collect_sites (filename) : 
    arr = []
    with open(filename , 'r') as file : 
        lines = file.readlines()

    for line in lines : 
        arr += (line.split(';'))
    return arr 


# TODO : add methods here 
# scraping every specific site with its own scrapuing methode 
def selective_scrap (onion_name , onion_url) : 
    match onion_name : 
        case 'AHMIA' : 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return 
        case 'RelateList' : 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return 
        case 'Breached_Forum' : 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return 
        case 'Dar_Leak_Market' : 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return 
        case 'DeepPaste_V3' : 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return 
        case 'Snatch' : 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return 
        case 'RansomEXX': 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return ; 
        case 'Ragnar_Locker': 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return ; 
        case 'Quantum_Blog': 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return ; 
        case 'Hive_Leaks': 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return ; 
        case 'AvosLocker': 
            t = threading.Thread(target=SCRAP_ALL , )
            t = start()
            t = join()
            return ; 
        case _ : 
            return 'No website to scrap'; 



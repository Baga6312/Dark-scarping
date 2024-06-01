from requests_tor  import RequestsTor
from bs4 import BeautifulSoup  

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

# scraping every specific site with its own scrapuing methode 
def selective_scrap (onion_name , onion_url) : 
    match onion_name : 
        case 'AHMIA' : 
            return 
        case 'RelateList' : 
            return 
        case 'Breached_Forum' : 
            return 
        case 'Dar_Leak_Market' : 
            return 
        case 'DeepPaste_V3' : 
            return 
        case 'Snatch' : 
            return 
        case 'RansomEXX': 
            return ; 
        case 'Ragnar_Locker': 
            return ; 
        case 'Quantum_Blog': 
            return ; 
        case 'Hive_Leaks': 
            return ; 
        case 'AvosLocker': 
            return ; 
        case _ : 
            return 'No website to scrap'; 

def scrap_fine(url) :
    rq.get(url) 
    soup = BeautifulSoup(rq.text , 'html.parser')
    print(soup.find_all("a"))
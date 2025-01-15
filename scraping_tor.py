import threading
from requests_tor import RequestsTor
from scrap import SCRAP_ALL 

request = RequestsTor(tor_ports=(9050,), tor_cport=9051)
filename = "data_leaks_sites.txt"

def collect_sites(filename):
    arr = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        arr += (line.split(';'))
    return arr 

def scrape_ahmia(url):
    t = threading.Thread(target=SCRAP_ALL, args=("AHMIA", url, "keyword", "li", "result", "/search/?q="))
    t.start()
    t.join()

def scrape_relatelist(url):
    t = threading.Thread(target=SCRAP_ALL, args=("RelateList", url, "keyword", "a", "", "/"))
    t.start()
    t.join()

def selective_scrap(onion_name, onion_url):
    match onion_name:
        case 'AHMIA':
            scrape_ahmia(onion_url)
        case 'RelateList':
            scrape_relatelist(onion_url)
        case 'Breached_Forum':
            t = threading.Thread(target=SCRAP_ALL, args=(onion_name, onion_url, "keyword", "p", "desc", "/search.php?s="))
            t.start()
            t.join()
        case 'Dar_Leak_Market':
            t = threading.Thread(target=SCRAP_ALL, args=(onion_name, onion_url, "keyword", "td", "", "/?k="))
            t.start()
            t.join()
        case 'DeepPaste_V3':
            t = threading.Thread(target=SCRAP_ALL, args=(onion_name, onion_url, "keyword", "p", "text-truncate", "/search/"))
            t.start()
            t.join()
        case 'Snatch':
            t = threading.Thread(target=SCRAP_ALL, args=(onion_name, onion_url, "keyword", "a", "", "/search?query="))
            t.start()
            t.join()
        case 'RansomEXX':
            t = threading.Thread(target=SCRAP_ALL, args=(onion_name, onion_url, "keyword", "div", "post", "/search?q="))
            t.start()
            t.join()
        case 'Ragnar_Locker':
            t = threading.Thread(target=SCRAP_ALL, args=(onion_name, onion_url, "keyword", "div", "post-content", "/search?q="))
            t.start()
            t.join()
        case 'Quantum_Blog':
            t = threading.Thread(target=SCRAP_ALL, args=(onion_name, onion_url, "keyword", "article", "post", "/?s="))
            t.start()
            t.join()
        case 'Hive_Leaks':
            t = threading.Thread(target=SCRAP_ALL, args=(onion_name, onion_url, "keyword", "div", "entry-content", "/?s="))
            t.start()
            t.join()
        case 'AvosLocker':
            t = threading.Thread(target=SCRAP_ALL, args=(onion_name, onion_url, "keyword", "div", "post-content", "/search?q="))
            t.start()
            t.join()
        case _:
            return 'No website to scrap'

if __name__ == "__main__":
    sites = collect_sites(filename)
    for site in sites:
        onion_name, onion_url = site.split('=')
        selective_scrap(onion_name.strip(), onion_url.strip())

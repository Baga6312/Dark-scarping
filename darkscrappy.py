from scraping_tor import collect_sites, selective_scrap
import requests
from stem.control import Controller
import os 
from stem import Signal
from scraping_tor import collect_sites, selective_scrap
from tor_utils import get_tor_session, renew_tor_circuit


def get_tor_session():
    """Create a Tor session with circuit renewal"""
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    return session

def renew_tor_circuit():
    """Renew Tor circuit to get a new exit node"""
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_password")
        controller.signal(Signal.NEWNYM)

def search_leaks_on_sites(filename, keyword):
    sites = collect_sites(filename)

    for site in sites:
        # Handle both '=' and ';' separators
        if '=' in site:
            onion_name, onion_url = site.split('=', 1)
        elif ';' in site:
            onion_name, onion_url = site.split(';', 1)
        else:
            print(f"Skipping invalid site entry: {site}")
            continue

        onion_name = onion_name.strip()
        onion_url = onion_url.strip()

        print(f"Searching for '{keyword}' on {onion_name}...")
        selective_scrap(onion_name, onion_url, keyword)



def main():
    print("Dark Web Data Leak Search Tool")
    print("===============================")

    keyword = input("Enter the keyword to search for: ").strip()
    filename = os.path.join("onion_sites", "data_leaks_sites.txt")
    search_leaks_on_sites(filename, keyword)

if __name__ == "__main__":
    main()

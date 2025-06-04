# scraping_tor.py
import time
import requests
import os
from tor_utils import get_tor_session, renew_tor_circuit
from scrap import SCRAP_ALL 

def collect_sites(filename):
    arr = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    arr.append(line)
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    return arr

def selective_scrap(onion_name, onion_url, keyword):
    try:
        # Define endpoint
        if onion_name == "AHMIA":
            end_point = "/search/?q={keyword}"
        elif onion_name == "RelateList":
            end_point = "/search?query={keyword}"
        elif onion_name == "RansomEXX":
            end_point = "/search?q={keyword}"
        elif onion_name == "Dark_Leak_Market":
            end_point = "/search?term={keyword}"
        elif onion_name == "hayStak":
            end_point = "/search?q={keyword}"
        elif onion_name == "Torch":
            end_point = "/search?query={keyword}"
        elif onion_name == "EXCAVATOR":
            end_point = "/search?q={keyword}"
        elif onion_name == "OnionWay":
            end_point = "/search?q={keyword}"
        elif onion_name == "ouRealm":
            end_point = "/search?term={keyword}"
        elif onion_name == "Dark_Side":
            end_point = "/search?q={keyword}"
        else:
            end_point = "/search?q={keyword}"
        
        # Call the SCRAP_ALL function
        SCRAP_ALL(onion_name, onion_url, end_point, keyword)
        
    except Exception as e:
        print(f"Error in selective_scrap: {str(e)}")

if __name__ == "__main__":
    filename = "data_leaks_sites.txt"
    sites = collect_sites(filename)
    for site in sites:
        if '=' in site:
            parts = site.split('=', 1)
        elif ';' in site:
            parts = site.split(';', 1)
        else:
            continue
            
        if len(parts) == 2:
            onion_name, url = parts
            selective_scrap(onion_name.strip(), url.strip(), "test")

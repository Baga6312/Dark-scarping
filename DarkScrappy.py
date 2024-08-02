from scraping_tor import collect_sites, selective_scrap

def main():
    keyword = input("Enter the keyword to search for: ")
    filename = "data_leaks_sites.txt"
    sites = collect_sites(filename)
    
    for site in sites:
        onion_name, onion_url = site.split('=')
        print(f"Searching {onion_name}...")
        selective_scrap(onion_name.strip(), onion_url.strip())

if __name__ == "__main__":
    main()

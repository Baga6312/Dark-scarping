from scraping_tor import collect_sites, selective_scrap

def search_leaks_on_sites(filename, keyword):
  
    sites = collect_sites(filename)
    
    for site in sites:
        # Split the site entry into name and URL
        onion_name, onion_url = site.split('=')
        onion_name = onion_name.strip()
        onion_url = onion_url.strip()

        print(f"Searching for '{keyword}' on {onion_name}...")
        selective_scrap(onion_name, onion_url, keyword)

def main():
    ##main function that handles user input and initiates the search process.

    print("Dark Web Data Leak Search Tool")
    print("===============================")
    
    # prompt user for the keyword and the filename containing site URLs
    keyword = input("Enter the keyword to search for: ").strip()
    filename = "onion_sites/data_leaks_sites.txt"

    # start searching through the sites
    search_leaks_on_sites(filename, keyword)

if __name__ == "__main__":
    main()

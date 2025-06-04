# scrap.py
from bs4 import BeautifulSoup
import time
import requests
from tor_utils import get_tor_session, renew_tor_circuit

def SCRAP_ALL(onion_name, onion_url, end_point, keyword):
    try:
        session = get_tor_session()
        base_url = f"http://{onion_url}"
        full_url = base_url + end_point.replace("{keyword}", keyword)

        print(f"Fetching URL: {full_url}")

        # Add retry logic
        for attempt in range(3):
            try:
                response = session.get(full_url, timeout=60)
                response.raise_for_status()
                html = response.text
                break  # Exit loop if successful
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt+1} failed: {str(e)}")
                if attempt < 2:
                    print("Renewing Tor circuit and retrying...")
                    renew_tor_circuit()
                    time.sleep(5)
                else:
                    print(f"All attempts failed for {onion_name}")
                    return

        # Parse HTML and extract results
        soup = BeautifulSoup(html, 'html.parser')
        
        # Try different class names if 'result' doesn't work
        results = soup.find_all('div', class_='result') or \
                  soup.find_all('div', class_='search-result') or \
                  soup.find_all('div', class_='item') or \
                  soup.find_all('article')

        if not results:
            print(f"No results found for '{keyword}' on {onion_name}")
            return

        print(f"Found {len(results)} results for '{keyword}' on {onion_name}")
        for result in results:
            title = None
            link = None
            
            # Try to find title
            title_elem = result.find('a') or result.find('h2') or result.find('h3')
            if title_elem:
                title = title_elem.text.strip()
                
            # Try to find link
            link_elem = result.find('a')
            if link_elem and 'href' in link_elem.attrs:
                link = link_elem['href'].strip()
                if not link.startswith('http'):
                    link = base_url + link
                    
            if title and link:
                print(f"Title: {title}\nLink: {link}\n")
            else:
                print("Skipping result - missing title or link")

    except Exception as e:
        print(f"Error scraping {onion_url}: {str(e)}")

from requests_tor import RequestsTor

request = RequestsTor(tor_ports=(9050,), tor_cport=9051)

def SCRAP_ALL (onion_name ,onion_url ,keyword ,tag ,class_name ,end_point) : 
    html = request.get(onion_ur+end_point+onion_url).text

    soup=bs(html, 'html.parser') 

    ## reshaping the keyword 
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    check_email_pattern = bool(re.search(email_pattern, keyword))

    new_words = re.findall(r'\b[a-zA-Z]+\b', keyword)
    cleaned = ' '.join(new_words)

    for word in soup.find_all(tag , class_=class_name): 

        if check_email_pattern : 
            
            ## refining the word 
            words = re.findall(r'\b[a-zA-Z]+\b', cleaned)
            for word in words :

                if word : 
                    print("found on " + onion_name)
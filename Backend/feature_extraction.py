import re, socket, random, ssl, socket, whois
from urllib.parse import urlparse
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from typing import Any


def having_IP_Addreess(url):
    try:
        host = urlparse(url).netloc
        socket.inet_aton(host)
        return -1
    except:
        return 1
    
def url_length(url):
    return -1 if len(url) >= 75 else (0 if 54 <= len(url)  < 75 else 1)

def shortening_service(url):
    pattern = r"(bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|tinyurl|tr\.im|is\.gd|cli\.gs|yfrog\.com|migre\.me|ff\.m|tiny.cc)"
    return -1 if re.search(pattern, url) else 1

def having_at_symbol(url):
    return -1 if "@" in url else 1

def double_slash_redirecting(url):
    last_double_slash = url.rfind('//')
    return -1 if last_double_slash > 6 else 1

def prefix_suffix(url):
    domain = urlparse(url).netloc
    return -1 if '-' in domain else 1

def sub_domain(url):
    domain = urlparse(url).netloc
    dots = domain.split('.')
    if len(dots) < 3:
        return 1
    elif len(dots) == 3:
        return 0
    else:
        return -1
    
def get_user_agent():
    agents = [
        # Chrome (Windows)
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36)",
        # Chrome (Mac Intel)
        "Mozilla/5.0 (Macintosh; Intel Max os X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36",
        # FireFax (Windows)
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Geck0/201000101 Firebox/117.0"
        # Safari (IPhone)
        "Mozilla/5.0 (IPhone; CPU IPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/1SE148 Safari/604.1"
        # Android Chrome
        "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36"
    ]
    return agents
    
def get_soup(url) -> Any:
    try:
        headers = {
            "User-Agent": random.choice(get_user_agent())
        }
        response = requests.get(url, headers=headers, timeout=10)
        return BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        print(f"Error fetching response: {e}")
        return None

def ssl_state(url):
    try:
        domain = urlparse(url).netloc
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                issuer = dict(x[0] for x in cert['issuer']) # type: ignore
                start_date = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z") # type: ignore
                age = (datetime.now() - start_date).days
                trusted = ["Google", "Let's Encrypt", "DigiCert", "Cloudflare"]
                return 1 if any(t in issuer.get('O', '') for t in trusted) and age >= 365 else 0 # type: ignore
    except:
        return -1

def check_favicon(soup:BeautifulSoup, url):
    try:
        for link in soup.find_all("link", rel='icon'):
            href = link.get('href', "") # type: ignore
            if urlparse(href).netloc and urlparse(href).netloc not in url: # type: ignore
                return -1
            return 1
    except:
        return -1
    
def check_port(url):
    try:
        domain = urlparse(url).netloc
        for port in [80, 443]:
            try:
                with socket.create_connection((domain, port), timeout=2):
                    return 1
            except:
                continue
        return -1
    except:
        return -1

def https_token(url):
    try:
        domain = urlparse(url).netloc.lower()
        return -1 if 'https' in domain.replace("https://", "") else 1
    except:
        return -1
    
def request_url(soup:BeautifulSoup, url):
    try:
        total, external = 0, 0
        for tag in soup.find_all(['img', 'audio', 'embed', 'iframe']):
            src = tag.get("src", "") #type:ignore
            if src:
                total += 1
                if urlparse(src).netloc and urlparse(src).netloc not in urlparse(url).netloc: #type:ignore
                    external += 1
        if total == 0:
            return 1
        percent = external / total * 100
        return 1 if percent < 22 else (0 if percent <= 61 else -1)
    except:
        return -1
    
def url_of_anchor(soup:BeautifulSoup, url:str):
    try:
        total, unsafe = 0, 0
        for tag in soup.find_all("a"):
            href = tag.get("href", "") # type:ignore
            if href:
                total += 1
                if '#' in href or 'javascript' in href.lower() or 'mailto' in href.lower(): #type:ignore
                    unsafe += 1
                elif urlparse(href).netloc and urlparse(href).netloc not in urlparse(url).netloc: #type:ignore
                    unsafe += 1
        if total == 0:
            return 1
        percent = unsafe / total * 100
        return 1 if percent < 31 else (0 if percent <= 67 else -1)
    except:
        return -1

def links_in_tags(soup:BeautifulSoup, url:str):
    try:
        total, external = 0, 0
        for tag in soup.find_all(['meta', 'script', 'link']):
            href = tag.get("href", "") or tag.get("src", "") #type:ignore
            if href:
                total += 1
                if urlparse(href).netloc and urlparse(href).netloc not in urlparse(url).netloc: #type:ignore
                    external += 1
        if total == 0:
            return 1
        percent = external / total * 100
        return 1 if percent < 17 else (0 if percent <= 81 else -1)
    except:
        return -1
    
def sfh(soup:BeautifulSoup, url:str):
    try:
        for form in soup.find_all('form'):
            action = form.get('action', '') #type:ignore
            if action == "" or action == "about:blank":
                return -1
            elif urlparse(action).netloc and urlparse(action).netloc not in urlparse(url).netloc: # type:ignore
                return 0
        return 1
    except:
        return -1
    


def submitting_to_email(soup:BeautifulSoup):
    try:
        for form in soup.find_all("form"):
            if 'mailto' in str(form.get("action", "")).lower(): #type:ignore
                return -1
        return 1
    except:
        return -1
    
def domain_registration_length(url):
    try:
        domain = urlparse(url).netloc
        w = whois.whois(domain)
        creation_date = w.creation_date
        expiration_date = w.expiration_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        if not creation_date or not expiration_date:
            return -1
        registration_period = (expiration_date - creation_date).days
        return 1 if int(registration_period) > 356 else -1
    except Exception as e:
        print(f"Whois Error: {e}")
        return -1

def redirect_feature(url):
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        if len(response.history) <= 1:
            return 1
        elif len(response.history) <= 4:
            return 0
        else:
            return -1
    except:
        return -1
    
def on_mouse_over(soup:BeautifulSoup):
    script_content = soup.get_text().lower() if not None else ""
    return -1 if "onmouseover" in script_content else 1

def right_click_disabled(soup:BeautifulSoup):
    script_content = soup.get_text().lower()
    if "event.button==2" in script_content:
        return -1
    return 1

def popup_window(soup:BeautifulSoup):
    script_content = soup.get_text().lower()
    return -1 if "alert(" in script_content or "popup" in script_content else 1

def iframe_feature(soup:BeautifulSoup):
    iframes = soup.find_all('iframe') if not None else ""
    for iframe in iframes:
        if iframe.get('width') == "0" or iframe.get('height') == '0' or 'display:none' in iframe.get('style', ''): #type:ignore
            return -1
    return 1

def doamin_age(url):
    try:
        domain = urlparse(url).netloc
        w = whois.whois(domain)
        creation = w.creation_date

        if isinstance(creation, list):
            creation = creation[0]
        if not creation:
            return -1
        
        age_days = (datetime.now() - creation).days
        return 1 if age_days >= 180 else -1
    except:
        return -1
    
def dns_record_check(url):
    try:
        domain = urlparse(url).netloc
        socket.gethostbyname(domain)
        return 1
    except:
        return -1
    
def abnormal_url(soup:BeautifulSoup, url:str):
    domain = urlparse(url).netloc
    if soup and domain in soup.text:
        return 1
    return -1

    
def features(url):
    soup = get_soup(url)
    return [
        having_IP_Addreess(url), url_length(url), 
        shortening_service(url), having_at_symbol(url), 
        double_slash_redirecting(url), prefix_suffix(url), 
        sub_domain(url), ssl_state(url),
        domain_registration_length(url),
        check_favicon(soup, url), check_port(url),
        https_token(url), request_url(soup, url),
        url_of_anchor(soup, url), links_in_tags(soup, url),
        sfh(soup, url), 
        submitting_to_email(soup), abnormal_url(soup, url), redirect_feature(url),
        -1, -1,
        -1, -1,
        doamin_age(url), dns_record_check(url),0,0,0,0,-1
        
    ]

if __name__ == '__main__':
    url = 'http:////google.com'
    print(features(url))
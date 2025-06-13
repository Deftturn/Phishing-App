import re, socket, random
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


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
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko Chrome/114.0.0.0 Safari/537.36)",
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
    
def get_soup(url):
    try:
        headers = {
            "User-Agent": random.choice(get_user_agent())
        }
        response = requests.get(url, headers=headers, timeout=10)
        print(BeautifulSoup(response.content, 'html.parser'))
    except Exception as e:
        print(f"Error fetching response: {e}")


    
def features(url):
    return [
        having_IP_Addreess(url), url_length(url), shortening_service(url), having_at_symbol(url), double_slash_redirecting(url), prefix_suffix(url), sub_domain(url)
    ]

if __name__ == '__main__':
    url = 'https://google.com'
    
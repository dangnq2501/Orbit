import requests
import time
import random

USER_AGENTS = [
    # Chrome trên Windows 10
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",

    # Firefox trên Windows 10
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) "
    "Gecko/20100101 Firefox/115.0",

    # Edge trên Windows 10
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36 Edg/114.0.1823.82",

    # Safari trên macOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",

    # Chrome trên Android
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Mobile Safari/537.36",

    # Firefox trên Android
    "Mozilla/5.0 (Android 13; Mobile; rv:115.0) "
    "Gecko/115.0 Firefox/115.0",

    # Chrome trên iPhone/iOS
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.5735.199 Mobile/15E148 Safari/604.1"
]

ACCEPT_LANGUAGES = [
    "en-US,en;q=0.9",
    "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    "en-GB,en;q=0.9",
    "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
]

PROXIES = [
      {"http":"http://nvztdgdw:ejg0ldanc5yr@104.239.105.125:6655"},
      {"http":"http://nvztdgdw:ejg0ldanc5yr@142.147.128.93:6593"},
      {"http":"http://nvztdgdw:ejg0ldanc5yr@64.64.118.149:6732"},
      {"http":"http://nvztdgdw:ejg0ldanc5yr@136.0.207.84:6661"},
      {"http":"http://nvztdgdw:ejg0ldanc5yr@216.10.27.159:6837"},
      {"http":"http://nvztdgdw:ejg0ldanc5yr@23.94.138.75:6349"},
      ]
def make_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": random.choice(ACCEPT_LANGUAGES),
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive",
    }
def requester(url):
	time.sleep(3)
	headers = make_random_headers()
	proxy = random.choice(PROXIES)
	return requests.get('https://blockchain.info/rawaddr/'+url, proxies=proxy, headers=headers).text
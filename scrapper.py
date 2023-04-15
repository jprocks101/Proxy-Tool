import requests
from colorama import Fore, Style

url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'

response = requests.get(url)

if response.status_code == 200:
    proxies = response.text.split('\n')
    with open('proxies.txt', 'w') as f:
        for proxy in proxies:
            f.write(proxy + '\n')
            print(Fore.GREEN + '[+] Scrapped HTTP Proxy: ' + proxy.strip() + Style.RESET_ALL)
    print(Fore.GREEN + 'Successfully scraped proxies and wrote them to proxies.txt' + Style.RESET_ALL)
else:
    print(Fore.RED + 'Failed to scrape proxies. Status code:', response.status_code + Style.RESET_ALL)

input(Fore.YELLOW + '\nPress enter to exit.' + Style.RESET_ALL)
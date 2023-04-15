import requests
from colorama import Fore, Style, init

init()  # initialize colorama

def check_proxy(proxy):
    try:
        response = requests.get('https://httpbin.org/get', proxies={'http': proxy, 'https': proxy}, timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    while True:
        print(Fore.MAGENTA + '\nMade by jpz#0001' + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT + "===== Proxy Shitty Menu =====" + Style.RESET_ALL)
        print(Fore.BLUE + "1: Scrape Proxies")
        print("2: Check Proxies")
        print("0: Exit" + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT + "===== Proxy Shitty Menu =====" + Style.RESET_ALL)
        
        choice = input(Fore.YELLOW + "\nEnter your choice: " + Style.RESET_ALL)

        if choice == "1":
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

        elif choice == "2":
            try:
                with open('proxies.txt', 'r') as f:
                    proxies = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(Fore.RED + 'No proxies found. Please scrape proxies first.' + Style.RESET_ALL)
                continue

            valid_proxies = []
            invalid_proxies = []

            for proxy in proxies:
                if check_proxy(proxy):
                    valid_proxies.append(proxy)
                    print(Fore.GREEN + f'{proxy} is valid' + Style.RESET_ALL)
                else:
                    invalid_proxies.append(proxy)
                    print(Fore.RED + f'{proxy} is invalid' + Style.RESET_ALL)

            while True:
                output_file = input(Fore.YELLOW + 'Enter output file path: ' + Style.RESET_ALL).strip()
                if not output_file:
                    print('Please enter a valid file path')
                else:
                    try:
                        with open(output_file, 'w') as f:
                            f.write('\n'.join(valid_proxies))
                        print(Fore.GREEN + f'Valid proxies written to {output_file}' + Style.RESET_ALL)
                        break
                    except Exception as e:
                        print(f'Error writing to file: {e}')

        elif choice == "0":
            print(Fore.YELLOW + Style.BRIGHT + "\nExiting..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nInvalid choice. Please try again." + Style.RESET_ALL)

    print(Fore.BLUE + "\nProxy Checker made by jpz#0001. Goodbye!" + Style.RESET_ALL)


if __name__ == '__main__':
    main()
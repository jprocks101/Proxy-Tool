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
    with open('proxies.txt', 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]

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

    input(Fore.YELLOW + 'Press Enter to exit' + Style.RESET_ALL)

if __name__ == '__main__':
    main()
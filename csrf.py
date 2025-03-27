import requests
from colorama import Fore, init
init(autoreset=True)

def get_csrf_token():
    try:
        session = requests.Session()
        response = session.get("https://www.instagram.com/data/shared_data/")
        csrf_token = response.json().get('config', {}).get('csrf_token', '')
        print(Fore.GREEN + f"\n[+] CSRF Token başarıyla oluşturuldu!")
        return csrf_token
    except Exception as e:
        print(Fore.RED + f"\n[!] Hata: {str(e)}")
        return ""

if __name__ == "__main__":
    token = get_csrf_token()
    if token:
        print(token)

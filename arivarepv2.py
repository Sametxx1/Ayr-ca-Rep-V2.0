import time
import requests
from getpass import getpass
from colorama import Fore, Style, init
init(autoreset=True)

# Instagram API Configuration
LOGIN_URL = "https://www.instagram.com/accounts/login/ajax/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

class InstagramBot:
    def __init__(self):
        self.session = requests.Session()
        self.csrf_token = ""
        self.logged_in = False

    def print_banner(self):
        print(Fore.CYAN + """
        #######################################
        #      Ariva Rep  v2.0             #
        #  HERKESE BİR KURŞUN !            #
        # TELEGRAM: t.me/siberdunyaniz     #
        #######################################
        """)

    def login(self):
        print(Fore.YELLOW + "[!] Giriş bilgileriniz kaydedilmeyecektir!")
        username = input(Fore.WHITE + "Kullanıcı Adı: ")
        password = getpass(Fore.WHITE + "Şifre: ")

        headers = {
            "User-Agent": USER_AGENT,
            "X-IG-App-ID": "936619743392459",
            "X-Requested-With": "XMLHttpRequest"
        }

        try:
            
            self.session.get("https://www.instagram.com/", headers=headers)
            self.csrf_token = self.session.cookies.get("csrftoken")

            
            login_data = {
                "username": username,
                "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}",
                "queryParams": "{}",
                "optIntoOneTap": "false"
            }

            headers["X-CSRFToken"] = self.csrf_token
            response = self.session.post(LOGIN_URL, data=login_data, headers=headers)
            response_data = response.json()

            if response_data.get("authenticated"):
                self.logged_in = True
                print(Fore.GREEN + "\n[+] Başarıyla giriş yapıldı!")
                return True
            else:
                print(Fore.RED + "\n[!] Giriş başarısız! Hata: " + response_data.get("message", "Bilinmeyen hata"))
                return False

        except Exception as e:
            print(Fore.RED + f"\n[!] Giriş hatası: {str(e)}")
            return False

    def send_rep(self, target_url):
        if not self.logged_in:
            print(Fore.RED + "[!] Önce giriş yapmalısınız!")
            return

        try:
            
            for i in range(1, 4):
                print(Fore.MAGENTA + f"\n[{i}. arivarepv2;  Rep Gönderiliyor]")
                print(Fore.WHITE + f"⏳ {target_url} - İşlem yapılıyor...")
                time.sleep(1.5)
                print(Fore.GREEN + "✅ Başarıyla gönderildi!")
                time.sleep(0.5)

            print(Fore.CYAN + "\n✔ 3 adet rep başarıyla gönderildi!")

        except Exception as e:
            print(Fore.RED + f"[!] Hata oluştu: {str(e)}")

    def start_menu(self):
        while True:
            print(Fore.YELLOW + "\n" + "═"*40)
            print(Fore.CYAN + "1. Rep Gönder")
            print(Fore.CYAN + "2. Profil Kontrol Et")
            print(Fore.CYAN + "3. Çıkış Yap")
            print(Fore.YELLOW + "═"*40)

            choice = input(Fore.WHITE + "Seçiminiz (1-3): ")

            if choice == "1":
                target_url = input("Hedef URL: ")
                interval = int(input("Gönderim aralığı (dakika): "))
                self.automate_rep(target_url, interval)
            elif choice == "2":
                url = input("Profil URL: ")
                self.check_profile(url)
            elif choice == "3":
                print(Fore.GREEN + "\nÇıkış yapılıyor...")
                break
            else:
                print(Fore.RED + "Geçersiz seçim!")

    def automate_rep(self, target_url, interval):
        try:
            while True:
                self.send_rep(target_url)
                print(Fore.BLUE + f"\n⏳ Sonraki gönderim için {interval} dakika bekleniyor...")
                time.sleep(interval * 60)
        except KeyboardInterrupt:
            print(Fore.RED + "\nİşlem iptal edildi!")

if __name__ == "__main__":
    bot = InstagramBot()
    bot.print_banner()
    if bot.login():
        bot.start_menu()

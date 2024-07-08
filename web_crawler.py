import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys

# Renkli çıktılar için ANSI renk kodları
class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

# Başlangıç URL'sini kullanıcıdan alın
start_url = input("Başlangıç URL'sini giriniz: ")

# Başlangıç URL'sini parse edin
parsed_url = urlparse(start_url)

# Ziyaret edilen URL'leri izlemek için küme oluşturun
visited_urls = set()

def crawl(url):
    try:
        if url in visited_urls:
            return
        visited_urls.add(url)

        print(colors.GREEN + f"URL aktif: {url}" + colors.END)

        # URL üzerinde istek yapın
        r = requests.get(url)
        r.raise_for_status()

        # BeautifulSoup kullanarak HTML içeriğini analiz edin
        soup = BeautifulSoup(r.content, 'html.parser')

        # Tüm <a> etiketlerini bulun ve içindeki URL'leri alın
        for link in soup.find_all('a', href=True):
            url_found = link.get('href')
            absolute_url = urljoin(url, url_found)  # Bağlantıyı mutlak URL'ye dönüştürün

            # Mutlak URL, başlangıç URL'sinin bir parçası mı diye kontrol edin
            if absolute_url.startswith(parsed_url.scheme + "://" + parsed_url.netloc):
                crawl(absolute_url)

    except requests.exceptions.RequestException as e:
        print(colors.RED + f"Hata oluştu ({e}): {url}" + colors.END)
    except KeyboardInterrupt:
        sys.exit()

# Başlatma fonksiyonunu çağırın
crawl(start_url)

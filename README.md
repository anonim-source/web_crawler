# Web Crawler

### Bu Python betiği, belirtilen başlangıç URL'sinden başlayarak web sitelerini dolaşarak içerdikleri bağlantıları keşfeder.

## Gereksinimler

- ##### Python 3.x
- ##### requests kütüphanesi
- ##### BeautifulSoup kütüphanesi
##### Gereksinimleri yüklemek için terminal veya komut istemcisinde aşağıdaki komutları kullanabilirsiniz:


`pip install requests`
`pip install beautifulsoup4`
## Kullanım

1. #### web_crawler.py dosyasını bilgisayarınıza indirin veya kopyalayın.

2. #### Terminal veya komut istemcisinde web_crawler.py dosyasının bulunduğu dizine gidin.

3. #### web_crawler.py dosyasını bilgisayarınıza indirin veya kopyalayın.

4. ## Terminal veya komut istemcisinde web_crawler.py dosyasının bulunduğu dizine gidin.



`python3 web_crawler.py`
1. #### Program başladığında size başlangıç URL'sini girmenizi isteyecektir.
2. #### Başlangıç URL'si, programın web sitesi gezginine başlayacağı adres olacaktır.
3. #### Program, başlangıç URL'sinden başlayarak web sayfalarını dolaşacak ve içerdikleri bağlantıları keşfedecektir.

4. #### Gezilen URL'ler ve hatalar, terminalde canlı olarak gösterilecektir.


5. ### Örneğin, programı çalıştırdığınızda aşağıdaki gibi bir çıktı alabilirsiniz:


##### Başlangıç URL'sini giriniz: https://www.example.com
##### URL aktif: https://www.example.com
##### URL aktif: https://www.example.com/page1
##### URL aktif: https://www.example.com/page2
##### Hata oluştu (404 Not Found): https://www.example.com/missing-page


- #### Program, HTTP ve HTTPS protokollerini destekler.
- ####Eğer program bir hata alırsa (örneğin, 404 Not Found gibi), hata mesajı kırmızı renkte gösterilecektir.
- #### Program, HTTP ve HTTPS protokollerini destekler.
- ####Eğer program bir hata alırsa (örneğin, 404 Not Found gibi), hata mesajı kırmızı renkte gösterilecektir.
- ####Programı durdurmak için Ctrl+C kombinasyonunu kullanabilirsiniz.Programı durdurmak için Ctrl+C kombinasyonunu kullanabilirsiniz.

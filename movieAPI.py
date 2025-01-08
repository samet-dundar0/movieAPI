import requests  # requests kütüphanesini import ediyoruz, API ile HTTP istekleri yapmak için kullanılır.


class TheMovieDB:
    # TheMovieDB sınıfı, TMDb API'sine yapılacak istekleri tanımlar.

    def __init__(self, url, key):
        """
        Sınıfın başlatıcı fonksiyonu, URL ve API anahtarını alır.
        """
        self.url = url  # TMDb API URL'sini alır
        self.key = key  # API anahtarını alır
    
    def popularMovie(self):
        """
        Popüler filmleri almak için API'den veri çeker.
        """
        # 'movie/popular' endpoint'ine HTTP GET isteği gönderiyor.
        response = requests.get(
            f"{self.url}movie/popular",  # API URL'si ve endpoint
            params={"api_key": self.key, "language": "en-US", "page": 1},  # Parametreler
        )
        return response.json() 

    def nowPlayingMovie(self):
        """
        Şu anda gösterimde olan filmleri almak için API'den veri çeker.
        """
        response = requests.get(
            f"{self.url}movie/now_playing",
            params={"api_key": self.key, "language": "en-US", "page": 1},
        )
        return response.json()

    def upcomingMovie(self):
        """
        Yakında çıkacak filmleri almak için API'den veri çeker.
        """
        response = requests.get(
            f"{self.url}movie/upcoming",
            params={"api_key": self.key, "language": "en-US", "page": 1},
        )
        return response.json()

    def topRatedMovie(self):
        """
        En yüksek puanlı filmleri almak için API'den veri çeker.
        """
        response = requests.get(
            f"{self.url}movie/top_rated",
            params={"api_key": self.key, "language": "en-US", "page": 1},
        )
        return response.json()



url = "https://api.themoviedb.org/3/"  # TMDb API URL'si
key = "699895881858120d2189b9c424f9b05b"  # API anahtarı (kişisel anahtarınızı burada kullanmalısınız)

# TheMovieDB sınıfını başlatıyoruz
movie = TheMovieDB(url, key)

# Popüler, şu anda oynayan, yakında çıkacak ve en çok oylanan filmleri alıyoruz
popularMovie = movie.popularMovie()
nowPlayingMovie = movie.nowPlayingMovie()
upcomingMovie = movie.upcomingMovie()
topRatedMovie = movie.topRatedMovie()


while True:
    
    secim = input("1-Popüler filmler\n2-Yeni filmler\n3-Yakında çıkacak Filmler\n4-En çok oylanan filmler\n5-Çıkış\nSeçim yapınız (1-5 arası kabul edilmektedir):")
    
    try:
        # Kullanıcıdan alınan değeri int'e dönüştürüp hangi kategoriye bakmak istediğini belirliyoruz.
        if int(secim) == 1:
            # Popüler filmler listesini yazdırıyoruz
            for movie in popularMovie["results"]:
                # Her bir filmin adını, IMDb puanını ve çıkış tarihini yazdırıyoruz
                print(f"Film adı: {movie['title']} IMDb: {movie['vote_average']} Tarih: {movie['release_date']}")
        elif int(secim) == 2:
            # Şu anda gösterimde olan filmleri yazdırıyoruz
            for movie in nowPlayingMovie["results"]:
                print(f"Film adı: {movie['title']} IMDb: {movie['vote_average']} Tarih: {movie['release_date']}")
        elif int(secim) == 3:
            # Yakında çıkacak filmleri yazdırıyoruz
            for movie in upcomingMovie["results"]:
                print(f"Film adı: {movie['title']} IMDb: {movie['vote_average']} Tarih: {movie['release_date']}")
        elif int(secim) == 4:
            # En çok oylanan filmleri yazdırıyoruz
            for movie in topRatedMovie["results"]:
                print(f"Film adı: {movie['title']} IMDb: {movie['vote_average']} Tarih: {movie['release_date']}")
        elif int(secim) == 5:
            # Programdan çıkmak için döngüyü sonlandırıyoruz
            break
        else:
            # Geçersiz seçim yapıldığında hata mesajı veriyoruz
            print("Lütfen 1-5 arası bir sayı girin.")
    
    except:
        # Kullanıcı geçersiz bir giriş yaptığında hata mesajı veriyoruz
        print("Lütfen 1-5 arası bir sayı girin.")


      

       
        
        
    
    







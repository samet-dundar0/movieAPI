import requests


class TheMovieDB:
    def __init__(self, url, key):
        self.url = url
        self.key = key

    def popularMovie(self):
        response = requests.get(
            f"{self.url}movie/popular",
            params={"api_key": self.key, "language": "en-US", "page": 1},
        )
        return response.json()
    
    def nowPlayingMovie(self):
        response = requests.get(
            f"{self.url}movie/now_playing",
            params={"api_key": self.key, "language": "en-US", "page": 1},
        )
        return response.json()
    
    def upcomingMovie(self):
        response = requests.get(
            f"{self.url}movie/upcoming",
            params={"api_key": self.key, "language": "en-US", "page": 1},
        )
        return response.json()
    
    def topRatedMovie(self):
        response = requests.get(
            f"{self.url}movie/top_rated",
            params={"api_key": self.key, "language": "en-US", "page": 1},
        )
        return response.json()


url = "https://api.themoviedb.org/3/"
key = "699895881858120d2189b9c424f9b05b"
movie = TheMovieDB(url, key)
popularMovie = movie.popularMovie()
nowPlayingMovie=movie.nowPlayingMovie()
upcomingMovie=movie.upcomingMovie()
topRatedMovie=movie.topRatedMovie()




while True:
    
    secim=input("1-Popüler filmler\n2-Yeni filmler\n3-Yakında çıkacak Filmler\n4-En çok oynlana filmler\n5-çıkış\nseçim yapınız(1-5 arası kabul edilmektedir):")
    
    try:
    
        if int(secim)==1:
            for movie in popularMovie["results"]:
                    print(f"film adı: {movie["title"]} İMDb:{movie["vote_average"]}  Tarih={movie["release_date"]}")
        elif int(secim)==2:
            for movie in nowPlayingMovie["results"]:
                    print(f"film adı: {movie["title"]} İMDb:{movie["vote_average"]} Tarih={movie["release_date"]}")
        elif int(secim)==3:
            for movie in upcomingMovie["results"]:
                    print(f"film adı: {movie["title"]} İMDb:{movie["vote_average"]} Tarih={movie["release_date"]}")
        elif int(secim)==4:
            for movie in topRatedMovie["results"]:
                    print(f"film adı: {movie["title"]} İMDb:{movie["vote_average"]} Tarih={movie["release_date"]}")
        elif int(secim)==5:
            break
        else:
            print("lütfen 1-5 arası sayı girin")
            
    except:
        print("lütfen 1-5 arası sayı girin")
        
        
    

      

       
        
        
    
    







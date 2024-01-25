from abc import ABC,abstractmethod


class Data_Fetcher(ABC):
    @abstractmethod
    def fetch_Data(self,url):
        pass

class ServerDataFetcher(Data_Fetcher):
    
    def fetch_Data(self, url):
        print("Data from server")
        return f"Data for {url}"
    
class CacheDataFetcher(Data_Fetcher):
    
    def __init__(self,data_fetcher) :
        self.data_fetcher=data_fetcher
        self.cache={}
        
    def fetch_Data(self, url):
        print("Data from cache")
        
        if url in self.cache:
            return f"Data for {url}"
        else:
            data = self.data_fetcher.fetch_Data(url)
            self.cache[url]=data
            return data

server = ServerDataFetcher()
cache = CacheDataFetcher(server)

print(cache.fetch_Data("Www.facebook.com"))
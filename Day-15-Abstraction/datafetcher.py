from abc import ABC,abstractmethod

class Datafetcher(ABC):
    
    @abstractmethod
    def fetch_data(self,url):
        pass
    
    
    
class ServerDataFetcher(Datafetcher):
    
    def fetch_data(self, url):
        print("fetching data from server")
        return f"Network data for {url}"
    
    
class CacheDataFetcher(Datafetcher): 
    
    def __init__(self,data_fetcher) :
        self.data_fetcher=data_fetcher
        self.cache={}
    
    def fetch_data(self, url):
        print("fetching data from cache")
        
        if url in self.cache:
            return self.cache[url]
        else:
            data= self.data_fetcher.fetch_data(url)
            self.cache[url]=data
            return data
        

server = ServerDataFetcher()
cache = CacheDataFetcher(server)

print(cache.fetch_data("www.facboook.com/posts"))
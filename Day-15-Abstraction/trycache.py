from abc import ABC,abstractmethod

class DataFetcher(ABC):
    
    @abstractmethod
    def data_Fetcher(self,url):
        pass
    
class ServerDataFetcher(DataFetcher):
    
    def data_Fetcher(self,url):
        print("Data from server");
        return f"Data for {url}"
    
class CacheDataFetcher(DataFetcher):
    
    def __init__(self,data_fetcher) :
        self.data_fetcher=data_fetcher
        self.cache={}
        
        
    
    def data_Fetcher(self,url):
        print("Data from Cache")
        
        if url in self.cache:
            return f"data for {url}"
        else:
            data = self.data_fetcher.data_Fetcher(url)
            self.cache[url]=data
            return data
    
    
server =  ServerDataFetcher()
cache = CacheDataFetcher(server)

print(cache.data_Fetcher("www.facebook.com"))
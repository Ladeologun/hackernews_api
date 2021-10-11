import requests

class Service:
    baseUrl = 'https://hacker-news.firebaseio.com/v0'
    newStoriesUrl = f"{baseUrl}/topstories.json"
    itemUrl = f"{baseUrl}/item/"
    
    def getstories(self):
        api_request = requests.get(self.newStoriesUrl)
        try:
            api_request.raise_for_status()
            return api_request.json()
        except:
            return None
    
    def getstory(self,storyId):
        res = requests.get(f"{self.itemUrl}{storyId}.json")
        try:
            res.raise_for_status()
            return res.json()
        except:
            return None
          
    def getcomment(self,commentId):
        res = requests.get(f"{self.itemUrl}{commentId}.json")
        try:
            res.raise_for_status()
            return res.json()
        except:
            return None

import requests

def getImageUrlFrom(query):
    endpoint = f"https://api.giphy.com/v1/gifs/search?api_key=exHS1nJ3klGJWrcjl08Fk2Ejl3LF5WCT&q={query}&limit=25&offset=0&rating=g&lang=en"
    response = requests.get(endpoint).json()
    # print(response["data"][0]["images"]["fixed_height"]["url"])
    return response["data"][0]["images"]["fixed_height"]["url"]
import requests
"""
#response = requests.get('https://api.tvmaze.com/search/shows?q=girls')
response = requests.get('https://api.tvmaze.com/shows/1/episodes')
print(response)
print(type(response.json()))
show = response.json()
print(show)
"""

joke = requests.get('https://api.chucknorris.io/jokes/random')
joke = joke.json()
print(joke["value"])
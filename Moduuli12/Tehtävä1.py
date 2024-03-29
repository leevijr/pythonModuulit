import requests



#response = requests.get('https://api.tvmaze.com/search/shows?q=girls')
response = requests.get('https://api.tvmaze.com/shows/1/episodes')
print(response)
show = response.json()
print(show)
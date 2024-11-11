import requests
import requests.exceptions
import os

from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')

access_token = os.getenv('ACCESS_TOKEN')

def search_song(query):

    # Genius API endpoint for search
    url = 'https://api.genius.com/search'

    headers = {
        'Authorization' : f'Bearer {access_token}'
    }

    # Parameters for the search query
    params = {
        'q' : query
    }

    # perform the search

    response = requests.get(url, headers=headers, params=params)

    search_results = response.json()

    if search_results['response']['hits']:
        # get the first result
        hit = search_results['response']['hits'][0]['result']
        return f"\n title : {hit['title']} \n artist : {hit['primary_artist']['name']} \n url : {hit['url']}"
    else:
        return "Sorry, I couldn't find that song."

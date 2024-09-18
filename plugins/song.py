import requests
import requests.exceptions

client_id = "LiWRr4ql7dATqK_MKITyc6fRAGKju3xdaGEE0cEA_wslFFyyY8pk4kGeEQA342Mo"

access_token = "mcASXxUdh5U2NhoBIyx1J9dwzdEdMuQ8-OwHVoyyC4japRjBiTD7y4fKMM36LHKC"

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

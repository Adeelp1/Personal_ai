import requests
import requests.exceptions

def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {'Accept': 'application/json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['joke']
    return "Sorry, I couldn't fetch a joke right now."
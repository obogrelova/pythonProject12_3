import requests

def get_cat_image():
    url = f'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

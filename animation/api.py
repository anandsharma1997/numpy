import requests

def fetch_data_from_api(request):
    response = requests.get("https://run.mocky.io/v3/a2fa8bc6-d43d-410f-97a7-7025ca8b792f")
    return response.json()
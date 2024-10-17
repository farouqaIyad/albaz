import requests

def get_tashkeel(input_text):
    # Base URL for the tashkeel operation
    url = 'https://tahadz.com/mishkal/ajaxGet'
    
    # Parameters required by the GET request
    params = {
        'text': input_text,
        'action': 'TashkeelText'
    }
    
    # Make the GET request
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # The response should contain the diacritized text
        return response.text.strip()
    else:
        return f"Error: {response.status_code}"



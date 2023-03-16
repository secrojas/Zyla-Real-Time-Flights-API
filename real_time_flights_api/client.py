import requests

class FlightLabsClient:
    
    def __init__(self, access_key: str):
        self.access_key = access_key
    
    def get_flights(self):        
        URL = "https://app.goflightlabs.com/flights"
        
        params = {'access_key': self.access_key}

        request = requests.get(url = URL, params=params)
        
        data = request.json()    
        
        return data
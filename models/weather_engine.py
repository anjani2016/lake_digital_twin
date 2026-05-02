import requests

def get_forecasted_rainfall(api_key, city="Aurora,CA"):
    """
    Fetches the predicted rainfall for the next 24 hours.
    Used to drive the 'Influent Volume' simulation.
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    
    # Sum up the predicted rainfall for the next 8 intervals (24 hours)
    total_rain = 0
    if 'list' in response:
        for period in response['list'][:8]:
            total_rain += period.get('rain', {}).get('3h', 0)
    
    return total_rain
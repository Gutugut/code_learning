import requests
def get_weather(city, units="metric", lang='zh_cn'):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": "c5bf5e7a1e3ee1e6e0f2a91b03ac3fd2",
        "units": "metric",
        "lang": "zh_cn"
        
    }
    
    try:
        response = requests.get(base_url, params = params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"error:{e}")
        return None
    
if __name__ == "__main__":
    city = input("请输入城市名称:")
    weather_data = get_weather(city)
    print(weather_data)
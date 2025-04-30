import requests

def get_weather(city):
    api_key = "1a50cc079a3d0f9f124b125c04716d74"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Celsius
        "lang": "tr"
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"{city} için hava durumu: {desc}, Sıcaklık: {temp}°C")
    else:
        print("Şehir bulunamadı veya hata oluştu.")

# Şehir sabit: İstanbul
get_weather("İstanbul")

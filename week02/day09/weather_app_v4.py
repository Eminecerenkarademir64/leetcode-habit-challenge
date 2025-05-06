import requests
from datetime import datetime

api_key = "1a50cc079a3d0f9f124b125c04716d74"
base_url = "https://api.openweathermap.org/data/2.5/weather"
log_file = "log.txt"

def get_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "tr"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\n{city.title()} için hava durumu: {desc}, Sıcaklık: {temp}°C")

        with open(log_file, "a", encoding="utf-8") as file:
            file.write(f"[{now}] {city.title()}: {desc}, {temp}°C\n")

    except requests.exceptions.HTTPError:
        print("\n❌ Şehir bulunamadı.")
    except Exception as e:
        print("\n⚠️ Hata oluştu:", str(e))

def main():
    while True:
        city = input("\nŞehir adı (çıkmak için 'q'): ").strip()

        if city.lower() == "q":
            print("Çıkılıyor... 👋")
            break
        elif not city:
            print("⚠️ Lütfen boş bırakmayın.")
        else:
            get_weather(city)

if __name__ == "__main__":
    main()

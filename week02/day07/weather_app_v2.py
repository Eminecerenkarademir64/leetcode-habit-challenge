import requests

def get_weather(city):
    api_key = "1a50cc079a3d0f9f124b125c04716d74"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

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
        print(f"\n{city.title()} için hava durumu: {desc}, Sıcaklık: {temp}°C")

    except requests.exceptions.HTTPError:
        print("\n❌ Şehir bulunamadı. Lütfen geçerli bir şehir adı girin.")
    except Exception as e:
        print("\n⚠️ Bir hata oluştu:", str(e))

def main():
    while True:
        city = input("\nHava durumunu öğrenmek istediğiniz şehir (çıkmak için 'q'): ").strip()

        if city.lower() == "q":
            print("Programdan çıkılıyor. 👋")
            break
        elif not city:
            print("⚠️ Lütfen bir şehir adı girin.")
        else:
            get_weather(city)

if __name__ == "__main__":
    main()

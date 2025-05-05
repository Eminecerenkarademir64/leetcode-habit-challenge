import requests

api_key = "1a50cc079a3d0f9f124b125c04716d74"
base_url = "https://api.openweathermap.org/data/2.5/weather"

favorite_cities = ["İstanbul", "Ankara", "İzmir", "Antalya", "Bursa"]

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
        print(f"\n{city.title()} için hava durumu: {desc}, Sıcaklık: {temp}°C")

    except requests.exceptions.HTTPError:
        print("\n❌ Şehir bulunamadı. Lütfen geçerli bir şehir adı girin.")
    except Exception as e:
        print("\n⚠️ Bir hata oluştu:", str(e))

def main():
    while True:
        print("\n--- Hava Durumu Uygulaması ---")
        print("1. Şehir ismi girerek sorgula")
        print("2. Favori şehirlerden birini seç")
        print("3. Çıkış")

        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            city = input("Şehir adı girin: ").strip()
            if city:
                get_weather(city)
            else:
                print("⚠️ Boş şehir ismi girilemez.")
        elif choice == "2":
            print("\nFavori Şehirler:")
            for i, city in enumerate(favorite_cities, 1):
                print(f"{i}. {city}")
            try:
                index = int(input("Seçmek istediğiniz şehir numarası: ")) - 1
                if 0 <= index < len(favorite_cities):
                    get_weather(favorite_cities[index])
                else:
                    print("⚠️ Geçersiz numara.")
            except ValueError:
                print("⚠️ Sayı girmeniz gerekiyor.")
        elif choice == "3":
            print("Çıkılıyor... 👋")
            break
        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

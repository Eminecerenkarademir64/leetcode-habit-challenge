import requests
import json
from datetime import datetime
import os

api_key = "1a50cc079a3d0f9f124b125c04716d74"
base_url = "https://api.openweathermap.org/data/2.5/weather"
log_file = "log.txt"
favorites_file = "favorites.json"

def load_favorites():
    if os.path.exists(favorites_file):
        with open(favorites_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_favorites(favorites):
    with open(favorites_file, "w", encoding="utf-8") as file:
        json.dump(favorites, file, ensure_ascii=False, indent=4)

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

def add_favorite(city):
    favorites = load_favorites()
    if city not in favorites:
        favorites.append(city)
        save_favorites(favorites)
        print(f"✅ {city.title()} favorilere eklendi.")
    else:
        print("⚠️ Bu şehir zaten favorilerde.")

def main():
    while True:
        print("\n--- Hava Durumu Uygulaması ---")
        print("1. Şehir ismi girerek sorgula")
        print("2. Favori şehirlerden birini seç")
        print("3. Favori şehri kaydet")
        print("4. Çıkış")

        choice = input("Seçiminiz: ").strip()

        if choice == "1":
            city = input("Şehir adı girin: ").strip()
            if city:
                get_weather(city)
            else:
                print("⚠️ Boş şehir ismi girilemez.")

        elif choice == "2":
            favorites = load_favorites()
            if not favorites:
                print("⚠️ Henüz favori şehir eklenmemiş.")
            else:
                print("\nFavori Şehirler:")
                for i, city in enumerate(favorites, 1):
                    print(f"{i}. {city.title()}")
                try:
                    index = int(input("Seçmek istediğiniz şehir numarası: ")) - 1
                    if 0 <= index < len(favorites):
                        get_weather(favorites[index])
                    else:
                        print("⚠️ Geçersiz numara.")
                except ValueError:
                    print("⚠️ Sayı girmeniz gerekiyor.")

        elif choice == "3":
            city = input("Favori olarak kaydetmek istediğiniz şehir: ").strip()
            if city:
                add_favorite(city)
            else:
                print("⚠️ Boş şehir ismi girilemez.")

        elif choice == "4":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

from datetime import datetime

movies = []

def add_movie(title, genre):
    date = datetime.now().strftime("%Y-%m-%d")
    movies.append({"title": title, "genre": genre, "date": date, "favorite": False})
    print(f"🎬 '{title}' filmi eklendi! Tür: {genre} - Tarih: {date}")

def list_movies():
    if not movies:
        print("📂 Henüz film eklenmemiş.")
    else:
        print("\n🎥 İzlenen Filmler:")
        for i, movie in enumerate(movies, 1):
            fav = "🌟" if movie["favorite"] else ""
            print(f"{i}. {movie['title']} - Tür: {movie['genre']} - Tarih: {movie['date']} {fav}")

def list_favorites():
    favorites = [movie for movie in movies if movie["favorite"]]
    if not favorites:
        print("💔 Henüz favori film yok.")
    else:
        print("\n💖 Favori Filmler:")
        for i, movie in enumerate(favorites, 1):
            print(f"{i}. {movie['title']} - Tür: {movie['genre']} - Tarih: {movie['date']} 🌟")

def mark_as_favorite():
    list_movies()
    try:
        index = int(input("\nFavori olarak işaretlemek istediğiniz film numarası: ")) - 1
        if 0 <= index < len(movies):
            movies[index]["favorite"] = True
            print(f"✅ '{movies[index]['title']}' favorilere eklendi!")
        else:
            print("⚠️ Geçersiz numara.")
    except ValueError:
        print("⚠️ Lütfen geçerli bir sayı girin.")

def list_movies_by_date():
    date = input("\nHangi tarihte izlenen filmleri görmek istiyorsunuz? (YYYY-MM-DD): ").strip()
    filtered = [movie for movie in movies if movie["date"] == date]
    if not filtered:
        print(f"❌ {date} tarihinde izlenen film bulunamadı.")
    else:
        print(f"\n📅 {date} Tarihinde İzlenen Filmler:")
        for i, movie in enumerate(filtered, 1):
            print(f"{i}. {movie['title']} - Tür: {movie['genre']}")

def main():
    while True:
        print("\n--- Film İzleme Günlüğü (v4) ---")
        print("1. Film Ekle")
        print("2. İzlenen Filmleri Listele")
        print("3. Favori Filmleri Listele")
        print("4. Filmi Favori Olarak İşaretle")
        print("5. Belirli Bir Tarihte İzlenen Filmleri Gör")
        print("6. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            title = input("Film Adı: ").strip()
            genre = input("Film Türü: ").strip()
            if title and genre:
                add_movie(title, genre)
            else:
                print("⚠️ Film adı ve türü boş bırakılamaz.")

        elif choice == "2":
            list_movies()

        elif choice == "3":
            list_favorites()

        elif choice == "4":
            mark_as_favorite()

        elif choice == "5":
            list_movies_by_date()

        elif choice == "6":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

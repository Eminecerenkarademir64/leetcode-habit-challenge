movies = []

def add_movie(title, genre):
    movies.append({"title": title, "genre": genre, "favorite": False})
    print(f"🎬 '{title}' filmi eklendi! Tür: {genre}")

def list_movies():
    if not movies:
        print("📂 Henüz film eklenmemiş.")
    else:
        print("\n🎥 İzlenen Filmler:")
        for i, movie in enumerate(movies, 1):
            fav = "🌟" if movie["favorite"] else ""
            print(f"{i}. {movie['title']} - Tür: {movie['genre']} {fav}")

def list_favorites():
    favorites = [movie for movie in movies if movie["favorite"]]
    if not favorites:
        print("💔 Henüz favori film yok.")
    else:
        print("\n💖 Favori Filmler:")
        for i, movie in enumerate(favorites, 1):
            print(f"{i}. {movie['title']} - Tür: {movie['genre']} 🌟")

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

def main():
    while True:
        print("\n--- Film İzleme Günlüğü (v3) ---")
        print("1. Film Ekle")
        print("2. İzlenen Filmleri Listele")
        print("3. Favori Filmleri Listele")
        print("4. Filmi Favori Olarak İşaretle")
        print("5. Çıkış")

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
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

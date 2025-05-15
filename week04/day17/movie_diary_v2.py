movies = []

def add_movie(title, genre):
    movies.append({"title": title, "genre": genre})
    print(f"🎬 '{title}' filmi eklendi! Tür: {genre}")

def list_movies():
    if not movies:
        print("📂 Henüz film eklenmemiş.")
    else:
        print("\n🎥 İzlenen Filmler:")
        for i, movie in enumerate(movies, 1):
            print(f"{i}. {movie['title']} - Tür: {movie['genre']}")

def list_movies_by_genre():
    genre = input("Aramak istediğiniz tür: ").strip()
    filtered = [movie for movie in movies if movie["genre"].lower() == genre.lower()]
    if not filtered:
        print(f"❌ '{genre}' türünde film bulunamadı.")
    else:
        print(f"\n🎭 '{genre.title()}' Türündeki Filmler:")
        for i, movie in enumerate(filtered, 1):
            print(f"{i}. {movie['title']}")

def search_movie():
    keyword = input("Aramak istediğiniz film adı: ").strip()
    results = [movie for movie in movies if keyword.lower() in movie["title"].lower()]
    if not results:
        print(f"❌ '{keyword}' kelimesini içeren film bulunamadı.")
    else:
        print(f"\n🔍 '{keyword}' İçeren Filmler:")
        for i, movie in enumerate(results, 1):
            print(f"{i}. {movie['title']} - Tür: {movie['genre']}")

def main():
    while True:
        print("\n--- Film İzleme Günlüğü (v2) ---")
        print("1. Film Ekle")
        print("2. İzlenen Filmleri Listele")
        print("3. Türe Göre Filmleri Listele")
        print("4. Film Adı ile Arama Yap")
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
            list_movies_by_genre()

        elif choice == "4":
            search_movie()

        elif choice == "5":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()


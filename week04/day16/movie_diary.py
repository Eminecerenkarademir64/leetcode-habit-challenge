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

def main():
    while True:
        print("\n--- Film İzleme Günlüğü ---")
        print("1. Film Ekle")
        print("2. İzlenen Filmleri Listele")
        print("3. Çıkış")

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
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

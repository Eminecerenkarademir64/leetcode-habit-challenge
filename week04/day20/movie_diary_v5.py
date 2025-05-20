from datetime import datetime
import csv

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

def export_to_txt():
    filename = "all_movies.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for movie in movies:
            fav = " (Favori)" if movie["favorite"] else ""
            file.write(f"{movie['title']} - {movie['genre']} - {movie['date']}{fav}\n")
    print(f"📄 Filmler '{filename}' dosyasına kaydedildi.")

def export_favorites_to_csv():
    filename = "favorite_movies.csv"
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Film Adı", "Tür", "Tarih"])
        for movie in movies:
            if movie["favorite"]:
                writer.writerow([movie["title"], movie["genre"], movie["date"]])
    print(f"📁 Favori filmler '{filename}' dosyasına kaydedildi.")

def main():
    while True:
        print("\n--- Film İzleme Günlüğü (v5) ---")
        print("1. Film Ekle")
        print("2. Filmleri Listele")
        print("3. Filmi Favori Olarak İşaretle")
        print("4. Filmleri TXT Dosyasına Kaydet")
        print("5. Favori Filmleri CSV Dosyasına Kaydet")
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
            mark_as_favorite()

        elif choice == "4":
            export_to_txt()

        elif choice == "5":
            export_favorites_to_csv()

        elif choice == "6":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
     main()
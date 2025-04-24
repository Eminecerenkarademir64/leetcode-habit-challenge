def main():
    todo_list = []

    while True:
        print("\n--- Görev Takip Uygulaması ---")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            task = input("Yeni görevi girin: ")
            todo_list.append(task)
            print("Görev eklendi.")

        elif choice == "2":
            if not todo_list:
                print("Henüz hiç görev eklenmemiş.")
            else:
                print("\n--- Görev Listesi ---")
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task}")

        elif choice == "3":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

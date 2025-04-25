def main():
    todo_list = []

    while True:
        print("\n--- Görev Takip Uygulaması v2 ---")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görevi Tamamlandı Olarak İşaretle")
        print("4. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            task = input("Yeni görevi girin: ")
            todo_list.append({"title": task, "done": False})
            print("Görev eklendi.")

        elif choice == "2":
            if not todo_list:
                print("Henüz hiç görev eklenmemiş.")
            else:
                print("\n--- Görev Listesi ---")
                for i, task in enumerate(todo_list, 1):
                    status = "✓" if task["done"] else "✗"
                    print(f"{i}. [{status}] {task['title']}")

        elif choice == "3":
            if not todo_list:
                print("Tamamlanacak görev yok.")
            else:
                for i, task in enumerate(todo_list, 1):
                    print(f"{i}. {task['title']}")
                try:
                    index = int(input("Hangi görevi tamamladınız (numara girin): ")) - 1
                    if 0 <= index < len(todo_list):
                        todo_list[index]["done"] = True
                        print("Görev tamamlandı olarak işaretlendi.")
                    else:
                        print("Geçersiz numara.")
                except ValueError:
                    print("Lütfen geçerli bir sayı girin.")

        elif choice == "4":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

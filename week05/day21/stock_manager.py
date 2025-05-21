inventory = []

def add_product(name, quantity):
    inventory.append({"name": name, "quantity": quantity})
    print(f"✅ {name} ürünü eklendi. Adet: {quantity}")

def list_inventory():
    if not inventory:
        print("📦 Stokta ürün yok.")
    else:
        print("\n📋 Stoktaki Ürünler:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item['name']} - Adet: {item['quantity']}")

def main():
    while True:
        print("\n--- Stok Takip Uygulaması ---")
        print("1. Ürün Ekle")
        print("2. Stoktaki Ürünleri Listele")
        print("3. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Ürün adı: ").strip()
            try:
                quantity = int(input("Ürün adedi: "))
                add_product(name, quantity)
            except ValueError:
                print("⚠️ Lütfen geçerli bir sayı girin.")

        elif choice == "2":
            list_inventory()

        elif choice == "3":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()
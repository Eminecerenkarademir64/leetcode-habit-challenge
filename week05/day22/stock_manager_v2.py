inventory = []
critical_limit = 5  # Kritik stok eşiği

def add_product(name, quantity):
    inventory.append({"name": name, "quantity": quantity})
    print(f"✅ {name} ürünü eklendi. Adet: {quantity}")

def list_inventory():
    if not inventory:
        print("📦 Stokta ürün yok.")
    else:
        print("\n📋 Stoktaki Ürünler:")
        for i, item in enumerate(inventory, 1):
            alert = " 🚨 KRİTİK!" if item["quantity"] <= critical_limit else ""
            print(f"{i}. {item['name']} - Adet: {item['quantity']}{alert}")

def update_stock():
    list_inventory()
    try:
        index = int(input("\nHangi ürünün stok miktarını değiştirmek istiyorsunuz (numara girin): ")) - 1
        if 0 <= index < len(inventory):
            change = int(input("Kaç adet eklemek (+) ya da çıkarmak (-) istiyorsunuz: "))
            inventory[index]["quantity"] += change
            print(f"🔄 '{inventory[index]['name']}' güncellendi. Yeni miktar: {inventory[index]['quantity']}")
        else:
            print("⚠️ Geçersiz ürün numarası.")
    except ValueError:
        print("⚠️ Lütfen geçerli bir sayı girin.")

def main():
    while True:
        print("\n--- Stok Takip Uygulaması (v2) ---")
        print("1. Ürün Ekle")
        print("2. Stoktaki Ürünleri Listele")
        print("3. Stok Giriş/Çıkış Yap")
        print("4. Çıkış")

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
            update_stock()

        elif choice == "4":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

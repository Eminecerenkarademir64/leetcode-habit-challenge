inventory = []
critical_limit = 5

def add_product(name, quantity):
    inventory.append({"name": name.lower(), "quantity": quantity})
    print(f"✅ '{name}' ürünü eklendi. Adet: {quantity}")

def list_inventory():
    if not inventory:
        print("📦 Stokta ürün yok.")
    else:
        print("\n📋 Stoktaki Ürünler:")
        for i, item in enumerate(inventory, 1):
            alert = " 🚨 KRİTİK!" if item["quantity"] <= critical_limit else ""
            print(f"{i}. {item['name'].title()} - Adet: {item['quantity']}{alert}")

def update_stock():
    list_inventory()
    try:
        index = int(input("\nHangi ürünün stok miktarını değiştirmek istiyorsunuz (numara): ")) - 1
        if 0 <= index < len(inventory):
            change = int(input("Kaç adet eklemek (+) ya da çıkarmak (-): "))
            inventory[index]["quantity"] += change
            print(f"🔄 '{inventory[index]['name'].title()}' güncellendi. Yeni miktar: {inventory[index]['quantity']}")
        else:
            print("⚠️ Geçersiz ürün numarası.")
    except ValueError:
        print("⚠️ Lütfen geçerli bir sayı girin.")

def delete_product():
    list_inventory()
    try:
        index = int(input("\nSilmek istediğiniz ürünün numarası: ")) - 1
        if 0 <= index < len(inventory):
            removed = inventory.pop(index)
            print(f"🗑️ '{removed['name'].title()}' stoğundan silindi.")
        else:
            print("⚠️ Geçersiz ürün numarası.")
    except ValueError:
        print("⚠️ Lütfen geçerli bir sayı girin.")

def search_product():
    keyword = input("Aramak istediğiniz ürün adını girin: ").lower().strip()
    found = [item for item in inventory if keyword in item["name"]]
    if not found:
        print("🔍 Aradığınız ürüne ait sonuç bulunamadı.")
    else:
        print(f"\n🔎 '{keyword}' için eşleşen ürünler:")
        for item in found:
            print(f"- {item['name'].title()} ({item['quantity']} adet)")

def main():
    while True:
        print("\n--- Stok Takip Uygulaması (v3) ---")
        print("1. Ürün Ekle")
        print("2. Stoktaki Ürünleri Listele")
        print("3. Stok Giriş/Çıkış Yap")
        print("4. Ürün Sil")
        print("5. Ürün Ara")
        print("6. Çıkış")

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
            delete_product()
        elif choice == "5":
            search_product()
        elif choice == "6":
            print("Çıkılıyor... 👋")
            break
        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

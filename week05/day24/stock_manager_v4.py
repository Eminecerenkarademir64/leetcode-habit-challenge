import csv
import os

inventory = []
csv_file = "inventory.csv"
critical_limit = 5

def load_inventory():
    if os.path.exists(csv_file):
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory.append({
                    "name": row["name"],
                    "quantity": int(row["quantity"])
                })

def save_inventory():
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["name", "quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in inventory:
            writer.writerow(item)

def add_product(name, quantity):
    inventory.append({"name": name.lower(), "quantity": quantity})
    save_inventory()
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
        index = int(input("\nStok güncellenecek ürün numarası: ")) - 1
        if 0 <= index < len(inventory):
            change = int(input("Stok değişimi (+/-): "))
            inventory[index]["quantity"] += change
            save_inventory()
            print(f"🔄 '{inventory[index]['name'].title()}' güncellendi.")
        else:
            print("⚠️ Geçersiz ürün numarası.")
    except ValueError:
        print("⚠️ Lütfen geçerli bir sayı girin.")

def delete_product():
    list_inventory()
    try:
        index = int(input("\nSilinecek ürün numarası: ")) - 1
        if 0 <= index < len(inventory):
            removed = inventory.pop(index)
            save_inventory()
            print(f"🗑️ '{removed['name'].title()}' silindi.")
        else:
            print("⚠️ Geçersiz ürün numarası.")
    except ValueError:
        print("⚠️ Lütfen geçerli bir sayı girin.")

def search_product():
    keyword = input("Ürün adıyla ara: ").lower().strip()
    found = [item for item in inventory if keyword in item["name"]]
    if not found:
        print("🔍 Ürün bulunamadı.")
    else:
        print(f"\n🔎 '{keyword}' için eşleşmeler:")
        for item in found:
            print(f"- {item['name'].title()} ({item['quantity']} adet)")

def main():
    load_inventory()

    while True:
        print("\n--- Stok Takip Uygulaması (v4) ---")
        print("1. Ürün Ekle")
        print("2. Stoktaki Ürünleri Listele")
        print("3. Stok Giriş/Çıkış")
        print("4. Ürün Sil")
        print("5. Ürün Ara")
        print("6. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Ürün adı: ").strip()
            try:
                quantity = int(input("Adet: "))
                add_product(name, quantity)
            except ValueError:
                print("⚠️ Sayı girin.")
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

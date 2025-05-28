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
                    "quantity": int(row["quantity"]),
                    "category": row["category"]
                })

def save_inventory():
    with open(csv_file, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["name", "quantity", "category"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in inventory:
            writer.writerow(item)

def add_product(name, quantity, category):
    inventory.append({
        "name": name.lower(),
        "quantity": quantity,
        "category": category.lower()
    })
    save_inventory()
    print(f"✅ '{name}' ürünü ({category}) eklendi. Adet: {quantity}")

def list_inventory():
    if not inventory:
        print("📦 Stokta ürün yok.")
    else:
        print("\n📋 Tüm Ürünler:")
        for i, item in enumerate(inventory, 1):
            alert = " 🚨 KRİTİK!" if item["quantity"] <= critical_limit else ""
            print(f"{i}. {item['name'].title()} - Adet: {item['quantity']} - Kategori: {item['category'].title()}{alert}")

def list_by_category():
    target = input("Listelemek istediğiniz kategori: ").lower().strip()
    filtered = [item for item in inventory if item["category"] == target]

    if not filtered:
        print(f"🔍 '{target}' kategorisinde ürün bulunamadı.")
    else:
        print(f"\n📂 {target.title()} Kategorisindeki Ürünler:")
        for item in filtered:
            print(f"- {item['name'].title()} ({item['quantity']} adet)")

def main():
    load_inventory()
    while True:
        print("\n--- Stok Takip Uygulaması (v7) ---")
        print("1. Ürün Ekle")
        print("2. Tüm Ürünleri Listele")
        print("3. Kategoriye Göre Listele")
        print("4. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Ürün adı: ").strip()
            category = input("Kategori: ").strip()
            try:
                quantity = int(input("Adet: "))
                add_product(name, quantity, category)
            except ValueError:
                print("⚠️ Sayı girin.")
        elif choice == "2":
            list_inventory()
        elif choice == "3":
            list_by_category()
        elif choice == "4":
            print("Çıkılıyor... 👋")
            break
        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

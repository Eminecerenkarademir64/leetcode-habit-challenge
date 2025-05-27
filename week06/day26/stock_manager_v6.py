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
        print("\n📋 Stoktaki Ürünler:")
        for i, item in enumerate(inventory, 1):
            alert = " 🚨 KRİTİK!" if item["quantity"] <= critical_limit else ""
            print(f"{i}. {item['name'].title()} - Adet: {item['quantity']} - Kategori: {item['category'].title()}{alert}")

def main():
    load_inventory()
    while True:
        print("\n--- Stok Takip Uygulaması (v6) ---")
        print("1. Ürün Ekle (kategori dahil)")
        print("2. Ürünleri Listele")
        print("3. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("Ürün adı: ").strip()
            category = input("Kategori (örnek: temizlik, kırtasiye, yiyecek): ").strip()
            try:
                quantity = int(input("Adet: "))
                add_product(name, quantity, category)
            except ValueError:
                print("⚠️ Sayı girin.")
        elif choice == "2":
            list_inventory()
        elif choice == "3":
            print("Çıkılıyor... 👋")
            break
        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

balance = 0
transactions = []

def add_income(amount):
    global balance
    balance += amount
    transactions.append(f"Gelir: +{amount} TL")
    print(f"✅ {amount} TL gelir eklendi. Güncel bakiye: {balance} TL")

def add_expense(amount):
    global balance
    balance -= amount
    transactions.append(f"Gider: -{amount} TL")
    print(f"❌ {amount} TL gider eklendi. Güncel bakiye: {balance} TL")

def show_balance():
    print(f"\n🔍 Güncel Bakiye: {balance} TL")

def show_transactions():
    print("\n📋 Tüm İşlemler:")
    for transaction in transactions:
        print(f"- {transaction}")

def main():
    while True:
        print("\n--- Kişisel Finans Uygulaması ---")
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Bakiye Görüntüle")
        print("4. Tüm İşlemleri Görüntüle")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            try:
                amount = float(input("Gelir miktarını girin: "))
                add_income(amount)
            except ValueError:
                print("⚠️ Lütfen geçerli bir sayı girin.")
                
        elif choice == "2":
            try:
                amount = float(input("Gider miktarını girin: "))
                add_expense(amount)
            except ValueError:
                print("⚠️ Lütfen geçerli bir sayı girin.")

        elif choice == "3":
            show_balance()

        elif choice == "4":
            show_transactions()

        elif choice == "5":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

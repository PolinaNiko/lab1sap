toy_store = {
    "Мяч": ['Мяч "Божья коровка на поле", 14 см', 2.58, 49],
    "ЛОЛ Кукла-сюрприз": ["ЛОЛ Кукла-сюрприз серия Путешествия", 37.50, 23],
    "Тесто-пластилин": ['Тесто-пластилин Genio Kids Набор "Студия причесок"', 22.63, 15],
    "Конструктор": ["Конструктор LEGO Super Mario", 274.32, 5],
    "Планшет графический": ["Планшет графический для рисования", 34.58, 8],
    "3D-ручка" : ["3D-ручка", 55.70, 9]
}

while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        toy_name = input("Введите название игрушки: ")
        if toy_name in toy_store:
            print(toy_name, ":", toy_store[toy_name][0])
        else:
            print("Такой игрушки нет в магазине")

    elif choice == "2":
        toy_name = input("Введите название игрушки: ")
        if toy_name in toy_store:
            print(toy_name, ":", toy_store[toy_name][1], "BYN")
        else:
            print("Такой игрушки нет в магазине")

    elif choice == "3":
        toy_name = input("Введите название игрушки: ")
        if toy_name in toy_store:
            print(toy_name, ":", toy_store[toy_name][2], "штук")
        else:
            print("Такой игрушки нет в магазине")

    elif choice == "4":
        print("\nИнформация о товарах в магазине:")
        for toy_name, toy_info in toy_store.items():
            print(toy_name, ":", toy_info[0], ", Цена: ", toy_info[1], " рублей, Количество: ", toy_info[2], " штук")

    elif choice == "5":
        total_cost = 0
        while True:
            toy_name = input("Введите название игрушки (0 - выход): ")
            if toy_name == "0":
                break
            if toy_name in toy_store:
                quantity = int(input(f"Введите количество {toy_name}: "))
                if quantity <= toy_store[toy_name][2]:
                    total_cost += toy_store[toy_name][1] * quantity
                    toy_store[toy_name][2] -= quantity
                else:
                    print("Недостаточно товара в магазине")
            else:
                print("Такой игрушки нет в магазине")
        print("Общая стоимость покупки: ", total_cost, " рублей")

    elif choice == "6":
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте еще раз.")
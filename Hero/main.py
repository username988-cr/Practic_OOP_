from classes import Rogue, Warrior, Mage, Universal, Enemy, Shop, battle


def choose_hero():
    print("\nВыбери героя:")
    print("1. Ловкач")
    print("2. Силовик")
    print("3. Маг")
    print("4. Универсальный\n")

    while True:
        c = input("> ").strip()
        if c == "1":
            return Rogue()
        if c == "2":
            return Warrior()
        if c == "3":
            return Mage()
        if c == "4":
            return Universal()
        print("\nНеверный выбор.\n")


def main():
    hero = choose_hero()
    shop = Shop()

    print("\nИгра началась!\n")
    hero.show_stats()

    while True:
        enemy = Enemy()
        win = battle(hero, enemy)
        if not win:
            break

        while True:
            print("\nЧто дальше?")
            print("1. Идти дальше")
            print("2. Магазин")
            print("3. Выход\n")

            cmd = input("> ").strip()
            if cmd == "1":
                break
            if cmd == "2":
                shop.open(hero)
                continue
            if cmd == "3":
                print("\nВыход из игры.\n")
                return
            print("\nНеверная команда.\n")

    print("\nКонец игры!\n")


if __name__ == "__main__":
    main()

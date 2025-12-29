import random
from abc import ABC, abstractmethod


# -------------------- MAGIC --------------------

class Magic(ABC):
    def __init__(self, name, mana_cost):
        self.name = name
        self.mana_cost = mana_cost

    @abstractmethod
    def apply(self, hero, enemy):
        pass


class Fireball(Magic):
    def __init__(self):
        super().__init__("Огненный шар", 10)

    def apply(self, hero, enemy):
        dmg = 35 + hero.magic_power
        enemy.hp -= dmg
        print(f"\n{hero.name} кастует '{self.name}' и наносит {dmg} урона!\n")


class Heal(Magic):
    def __init__(self):
        super().__init__("Лечение", 10)

    def apply(self, hero, enemy):
        heal = 25 + hero.magic_power
        hero.hp += heal
        if hero.hp > 100:
            hero.hp = 100
        print(f"\n{hero.name} использует '{self.name}' и лечится на {heal} HP!\n")


# -------------------- ITEMS --------------------

class Item:
    def __init__(self, name, price, kind, value):
        self.name = name
        self.price = price
        self.kind = kind      # hp / mana / dmg
        self.value = value

    def use(self, hero):
        if self.kind == "hp":
            hero.hp += self.value
            if hero.hp > 100:
                hero.hp = 100
            print(f"\n{hero.name} использовал {self.name} (+{self.value} HP)\n")

        elif self.kind == "mana":
            hero.mana += self.value
            print(f"\n{hero.name} использовал {self.name} (+{self.value} MANA)\n")

        elif self.kind == "dmg":
            hero.damage += self.value
            print(f"\n{hero.name} усилил урон (+{self.value} DMG)\n")


class Shop:
    def __init__(self):
        self.items = [
            Item("Эликсир HP", 20, "hp", 35),
            Item("Эликсир MANA", 20, "mana", 20),
            Item("Точильный камень", 30, "dmg", 3),
        ]

    def open(self, hero):
        while True:
            print("\n====================")
            print("       МАГАЗИН")
            print("====================")
            print(f"Монеты: {hero.coins}\n")

            for i in range(len(self.items)):
                it = self.items[i]
                print(f"{i}. {it.name} (цена {it.price})")

            print("\nВведите номер чтобы купить")
            print("q - выйти\n")

            s = input("> ").strip().lower()
            if s == "q":
                print("\nВы вышли из магазина.\n")
                return

            if not s.isdigit():
                print("\nНеверный ввод.\n")
                continue

            idx = int(s)
            if idx < 0 or idx >= len(self.items):
                print("\nНет такого предмета.\n")
                continue

            item = self.items[idx]
            if hero.coins < item.price:
                print("\nНедостаточно монет.\n")
                continue

            hero.coins -= item.price
            hero.inventory.append(item)
            print(f"\nКуплено: {item.name}. Осталось монет: {hero.coins}\n")


# -------------------- ENEMY --------------------

class Enemy:
    def __init__(self):
        names = ["Орк", "Гоблин", "Скелет", "Демон", "Тролль", "Вампир"]
        self.name = random.choice(names)
        self.hp = random.randint(60, 120)
        self.damage = random.randint(6, 18)
        self.reward = random.randint(10, 30)


# -------------------- HEROES --------------------

class Hero(ABC):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.damage = random.randint(10, 16)
        self.magic_power = 0
        self.coins = random.randint(30, 70)
        self.mana = 10
        self.inventory = []
        self.spells = []
        self.dodge_turns = 0  # без isinstance

    @abstractmethod
    def special_skill(self, enemy):
        pass

    def show_stats(self):
        print("\n====================")
        print(f"Герой: {self.name}")
        print(f"HP: {self.hp}")
        print(f"MANA: {self.mana}")
        print(f"DMG: {self.damage}")
        print(f"COINS: {self.coins}")
        print("====================\n")

    def restore_after_fight(self):
        self.hp = 100
        self.dodge_turns = 0
        if self.name == "Маг":
            self.mana = 20
        else:
            self.mana = 10

    def cast_spell_menu(self, enemy):
        if len(self.spells) == 0:
            print("\nЗаклинаний нет.\n")
            return False

        print("\n====== ЗАКЛИНАНИЯ ======")
        for i in range(len(self.spells)):
            sp = self.spells[i]
            print(f"{i}. {sp.name} (мана {sp.mana_cost})")
        print("q - назад\n")

        s = input("> ").strip().lower()
        if s == "q":
            return False
        if not s.isdigit():
            print("\nНеверный ввод.\n")
            return False

        idx = int(s)
        if idx < 0 or idx >= len(self.spells):
            print("\nНет такого заклинания.\n")
            return False

        sp = self.spells[idx]
        if self.mana < sp.mana_cost:
            print("\nНедостаточно маны.\n")
            return False

        self.mana -= sp.mana_cost
        sp.apply(self, enemy)
        return True

    def use_item_menu(self):
        if len(self.inventory) == 0:
            print("\nРюкзак пуст.\n")
            return False

        print("\n========= РЮКЗАК =========")
        for i in range(len(self.inventory)):
            it = self.inventory[i]
            print(f"{i}. {it.name}")
        print("q - назад\n")

        s = input("> ").strip().lower()
        if s == "q":
            return False
        if not s.isdigit():
            print("\nНеверный ввод.\n")
            return False

        idx = int(s)
        if idx < 0 or idx >= len(self.inventory):
            print("\nНет такого предмета.\n")
            return False

        item = self.inventory.pop(idx)
        item.use(self)
        return True


class Rogue(Hero):
    def __init__(self):
        super().__init__("Ловкач")
        self.spells = [Heal()]

    def special_skill(self, enemy):
        if self.mana < 10:
            print("\nНе хватает маны!\n")
            return
        self.mana -= 10
        self.dodge_turns = 3
        print("\nЛовкач активировал уклонение на 3 атаки!\n")


class Warrior(Hero):
    def __init__(self):
        super().__init__("Силовик")
        self.damage += 2

    def special_skill(self, enemy):
        if self.mana < 10:
            print("\nНе хватает маны!\n")
            return
        self.mana -= 10
        dmg = self.damage + 15
        enemy.hp -= dmg
        print(f"\nСиловик наносит мощный удар: {dmg} урона!\n")


class Mage(Hero):
    def __init__(self):
        super().__init__("Маг")
        self.mana = 20
        self.magic_power = 10
        self.spells = [Fireball(), Heal()]

    def special_skill(self, enemy):
        if self.mana < 10:
            print("\nНе хватает маны!\n")
            return
        self.mana -= 10
        dmg = 45 + self.magic_power
        enemy.hp -= dmg
        print(f"\nМаг применяет спец-умение: {dmg} урона!\n")


class Universal(Hero):
    def __init__(self):
        super().__init__("Универсальный")
        self.spells = [Heal()]

    def special_skill(self, enemy):
        if self.mana < 10:
            print("\nНе хватает маны!\n")
            return
        self.mana -= 10
        self.hp += 15
        if self.hp > 100:
            self.hp = 100
        enemy.hp -= self.damage
        print("\nУниверсальный восстановил HP и ударил врага!\n")


# -------------------- COMBAT --------------------

def do_attack(hero, enemy):
    crit = random.randint(1, 100) <= 25
    dmg = hero.damage * 2 if crit else hero.damage
    if crit:
        print("\nКРИТ!\n")
    enemy.hp -= dmg
    print(f"\n{hero.name} наносит {dmg} урона!\n")


def enemy_attack(hero, enemy):
    if hero.dodge_turns > 0:
        hero.dodge_turns -= 1
        print("\nГерой уклонился!\n")
        return
    hero.hp -= enemy.damage
    print(f"\n{enemy.name} атакует (-{enemy.damage} HP)\n")


def battle(hero, enemy):
    print("\n====================")
    print(f"Враг: {enemy.name}")
    print(f"HP: {enemy.hp} | DMG: {enemy.damage}")
    print(f"Награда: {enemy.reward} монет")
    print("====================\n")

    while hero.hp > 0 and enemy.hp > 0:
        hero.show_stats()
        print(f"Враг: {enemy.name} | HP: {enemy.hp}\n")

        print("1. Атака")
        print("2. Спец.умение")
        print("3. Магия")
        print("4. Рюкзак")
        print("5. Показать рюкзак\n")

        move = input("> ").strip()

        if move == "1":
            do_attack(hero, enemy)

        elif move == "2":
            hero.special_skill(enemy)

        elif move == "3":
            ok = hero.cast_spell_menu(enemy)
            if not ok:
                print("\nЗаклинание не применено -> обычная атака\n")
                do_attack(hero, enemy)

        elif move == "4":
            ok = hero.use_item_menu()
            if not ok:
                print("\nПредмет не использован -> обычная атака\n")
                do_attack(hero, enemy)

        elif move == "5":
            if len(hero.inventory) == 0:
                print("\nРюкзак пуст.\n")
            else:
                print("\nВ рюкзаке:")
                for i in range(len(hero.inventory)):
                    print("-", hero.inventory[i].name)
                print()
            continue

        else:
            print("\nНеверный ввод -> обычная атака\n")
            do_attack(hero, enemy)

        if enemy.hp > 0:
            enemy_attack(hero, enemy)

    if hero.hp > 0:
        print("\n====================")
        print("ПОБЕДА!")
        print(f"+{enemy.reward} монет")
        print("====================\n")
        hero.coins += enemy.reward
        hero.restore_after_fight()
        return True

    print("\nВы проиграли...\n")
    return False

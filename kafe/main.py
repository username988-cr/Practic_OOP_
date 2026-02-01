from collections import deque
import random
import time


# Классы
class Order:
    def __init__(self, client_name: str, dish: str):
        self.client_name = client_name
        self.dish = dish

    def __str__(self):
        return f"{self.client_name} — {self.dish}"


class Client:
    def __init__(self, name: str):
        self.name = name


class CafeQueue:
    def __init__(self):
        self.queue = deque()

    def add_orders(self, orders: list[Order]):
        self.queue.extend(orders)

    def has_orders(self) -> bool:
        return bool(self.queue)

    def size(self) -> int:
        return len(self.queue)

    def cook_one(self):
        if not self.queue:
            print("Все заказы выполнены")
            return

        order = self.queue.popleft()
        cook_time = random.randint(1, 3)
        print(f"Готовим: {order} ({cook_time} сек.)")
        time.sleep(cook_time)
        print(f"Готовый заказ: {order}")
        print("-" * 40)


#Проверка ввода
def safe_yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("да", "д", "yes", "y"):
            return True
        if ans in ("нет", "н", "no", "n"):
            print("=" * 40)
            return False
        print("Ошибка: введите 'да' или 'нет'.")


def safe_int_input(prompt: str, min_v: int, max_v: int) -> int:
    while True:
        s = input(prompt).strip()
        if not s.isdigit():
            print("Ошибка: нужно ввести число.")
            continue
        v = int(s)
        if v < min_v or v > max_v:
            print(f"Ошибка: число должно быть от {min_v} до {max_v}.")
            continue
        return v


def choose_dish(menu: list[str]) -> str:
    print("\nМеню:")
    for i, dish in enumerate(menu, 1):
        print(f"{i}. {dish}")
    idx = safe_int_input("Выберите номер блюда: ", 1, len(menu))
    return menu[idx - 1]


# Основная логика
def simulate():
    menu = ["Кофе", "Чай", "Сэндвич", "Пицца", "Десерт", "Сок", "Бургер", "Салат"]
    cafe = CafeQueue()

    #  Автоматические клиенты
    auto_clients = random.randint(3, 6)
    for i in range(auto_clients):
        client = Client(f"Клиент_{i + 1}")
        orders_count = random.randint(1, 4)
        orders = [
            Order(client.name, random.choice(menu))
            for _ in range(orders_count)
        ]
        cafe.add_orders(orders)

    print(f"Автоматически добавлено клиентов: {auto_clients}")
    print(f"Заказов в очереди: {cafe.size()}")
    print("=" * 40)

    # Ручное добавление  заказа
    if safe_yes_no("Хотите сделать заказ? (да/нет): "):
        name = input("Введите ваше имя: ").strip()
        if not name:
            name = "Гость"

        client = Client(name)
        temp_orders = []

        while True:
            dish = choose_dish(menu)
            temp_orders.append(Order(client.name, dish))

            if not safe_yes_no("Это весь заказ? (да — отправить, нет — добавить ещё): "):
                continue
            break

        cafe.add_orders(temp_orders)
        print(f"Заказ клиента '{client.name}' добавлен ({len(temp_orders)} блюд)")
        print("=" * 40)

    #  Готовка
    while cafe.has_orders():
        cafe.cook_one()

    print("Все заказы выполнены")


simulate()

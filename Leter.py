class Leter:
    def __init__(self,name,name2,leter,method):
        self.method = method
        self._leter = leter.capitalize()
        self._name = name.capitalize()
        self._name2 = name2.capitalize()

    def send(self):
       print(f"\nОтправитель:{self._name},    Получатель:{self._name2};\n\n Ваше Сообщение '{self._leter}'.\n\nОтправлено  с помощью {self.method} - Успешно")


class Email(Leter):
    def send(self):
       print(f"\nОтправитель:{self._name},    Получатель:{self._name2};\n\n Ваше Сообщение '{self._leter}'.\n\nОтправлено  с помощью {self.method} - Успешно")


class Post(Leter):
     def send(self):
        print(f"\nОтправитель:{self._name},    Получатель:{self._name2};\n\n Ваше Сообщение '{self._leter}'.\n\nОтправлено  с помощью {self.method} - Успешно")

class Telegram(Leter):
     def send(self):
        print(f"\nОтправитель:{self._name},   Получатель:{self._name2};\n\n Ваше Сообщение: '{self._leter}'.\n\nОтправлено  с помощью {self.method} - Успешно")



def start(letter: Leter):
    letter.send()

def choice():

    print("Приветствуем в почтовом сервисе!\n")

    def choice2():
        while True:
            print("\nВыберите способ отправки сообщения:")
            print("1. Email\n2. Почта\n3. Telegram")
            choice = input("\nВаш выбор: ")
            if choice == "1":
                start(Email(input("Введите имя отправителя:"),input("Введите имя получателя:"),input("Введите текст письма:"),"Email"))
                break

            if choice == "2":
                start(Post(input("Введите имя отправителя:"),input("Введите имя получателя:"),input("Введите текст письма:"),"Почты"))
                break

            if choice == "3":
                start(Telegram(input("Введите имя отправителя:"),input("Введите имя получателя:"),input("Введите текст письма:"),"Telegram"))
                break  

    choice2()
    while True:
        print("\nХотите отправить ещё одно сообщение?")
        print("1. Да\n2. Нет")
        choic = input("\nВаш выбор: ")

        if choic == "1":
            choice2()
        if choic == "2":
            print("До свидания!")
            break





choice()
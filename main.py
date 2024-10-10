def greet(language):
    greetings = {
        '1': "Здравствуйте!",
        '2': "Hello!",
        '3': "Привіт!",
        '4': "Cześć!",
        '5': "Hallo!"
    }
    return greetings.get(language, "Неверный выбор!")

def main():
    while True:
        print("Выберите язык / Choose a language / Виберіть мову / Wybierz język / Wählen Sie eine Sprache:")
        print("1. Русский")
        print("2. English")
        print("3. Українська")
        print("4. Polski")
        print("5. Deutsch")
        print("6. Выход / Exit")

        choice = input("Введите номер языка / Enter language number / Введіть номер мови / Wprowadź numer języka / Geben Sie die Sprachnummer ein: ")

        if choice in ['1', '2', '3', '4', '5']:
            greeting = greet(choice)
            print(greeting)
        elif choice == '6':
            print("Выход... / Exiting... / Wyjście... / Aussteigen...")
            break
        else:
            print("Неверный выбор! / Invalid choice! / Неправильний вибір! / Niepoprawny wybór!")

        while True:
            action = input("Введите команду (или 'выход' для возврата) / Enter command (or 'exit' to return): ")
            if action.lower() == 'выход' or action.lower() == 'exit':
                break
            elif action.lower() == 'hello':
                print("Команда 'hello' выполнена! / 'hello' command executed! / Команда 'привіт' виконана! / Komenda 'cześć' wykonana! / 'hallo' Befehl ausgeführt!")
            elif action.lower() == 'info':
                print("Это пример команды! / This is a sample command! / Це приклад команди! / To jest przykład polecenia! / Dies ist ein Beispielbefehl!")
            else:
                print("Выполняется команда:", action)

if __name__ == "__main__":
    main()

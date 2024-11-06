import warnings
warnings.filterwarnings("ignore")

import re

def validate_card_number(card_number):
    # Паттерн для проверки формата номера карты
    pattern = r'^(?:(\d{4}[- ]?){3}\d{4})$'
    return re.fullmatch(pattern, card_number) is not None

def find_card_numbers_in_text(text):
    # Паттерн для поиска номеров карт в тексте
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)

def find_card_numbers_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content.strip():  # Проверяем, что файл не пуст
                return find_card_numbers_in_text(content)
            else:
                print(f"Файл {file_path} пуст.")
                return []
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []

if __name__ == "__main__":
    while True:
        print("\nВыберите способ ввода данных:")
        print("1. Пользовательский ввод")
        print("2. Ввод адреса файла")
        print("3. Выход")

        try:
            k = int(input())
        except ValueError:
            print("Пожалуйста, введите число от 1 до 3.")
            continue

        if k == 1:
            card_input = input("Введите номер карты для проверки: ").strip()
            if validate_card_number(card_input):
                print("Номер карты корректный.")
            else:
                print("Номер карты некорректный.")

        elif k == 2:
            file_path = input("Введите путь к файлу для поиска номеров карт: ").strip()
            card_numbers_from_file = find_card_numbers_in_file(file_path)
            if card_numbers_from_file:
                print("Номера карт, найденные в файле:", card_numbers_from_file)
            else:
                print("Номера карт не найдены.")

        elif k == 3:
            break
        else:
            print("Пожалуйста, введите корректное число от 1 до 3.")

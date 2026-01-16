"""
Name.py - учебный модуль для работы с именами
"""

def format_full_name(first_name, last_name):
    """Форматирует полное имя"""
    if not first_name or not last_name:
        return "Ошибка: не указано имя или фамилия"
    return f"{first_name.strip().capitalize()} {last_name.strip().capitalize()}"

def count_vowels_in_text(text):
    """
    Подсчитывает количество гласных букв в тексте
    Гласные: a, e, i, o, u (английские) и а, е, ё, и, о, у, ы, э, ю, я (русские)
    Буква 'y' НЕ считается гласной в этой реализации
    """
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def is_palindrome_string(text):
    """Проверяет, является ли строка палиндромом"""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def process_list_of_names(names_list):
    """Обрабатывает список имен"""
    return [name.strip().capitalize() for name in names_list if name and name.strip()]

def get_name_initials(full_name):
    """Получает инициалы из полного имени"""
    parts = full_name.split()
    if len(parts) < 2:
        return "Ошибка: имя должно содержать хотя бы имя и фамилию"
    return ".".join([p[0].upper() for p in parts if p]) + "."

if __name__ == "__main__":
    print("Тестируем функции:")
    print(f"format_full_name('john', 'doe'): {format_full_name('john', 'doe')}")
    print(f"count_vowels_in_text('Python'): {count_vowels_in_text('Python')}")
    print(f"count_vowels_in_text('Hello'): {count_vowels_in_text('Hello')}")
    print(f"count_vowels_in_text('Привет'): {count_vowels_in_text('Привет')}")

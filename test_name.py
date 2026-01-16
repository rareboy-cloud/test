"""
test_name.py - тесты для модуля Name.py
Использование: python3 -m pytest test_name.py -v
"""

import pytest
from Name import (
    format_full_name,
    count_vowels_in_text,
    is_palindrome_string,
    process_list_of_names,
    get_name_initials
)


# ============================================================================
# ГРУППА 1: Тесты для функции format_full_name()
# ============================================================================

def test_format_full_name_normal_case():
    """Тест: обычное форматирование имени"""
    result = format_full_name("john", "doe")
    expected = "John Doe"
    assert result == expected, f"Ожидалось '{expected}', получено '{result}'"


def test_format_full_name_uppercase():
    """Тест: имя в верхнем регистре"""
    result = format_full_name("JANE", "SMITH")
    assert result == "Jane Smith"


def test_format_full_name_with_spaces():
    """Тест: имена с пробелами по краям"""
    result = format_full_name("  john  ", "  doe  ")
    assert result == "John Doe"


def test_format_full_name_empty_first():
    """Тест: пустое имя"""
    result = format_full_name("", "doe")
    assert result == "Ошибка: не указано имя или фамилия"


def test_format_full_name_empty_last():
    """Тест: пустая фамилия"""
    result = format_full_name("john", "")
    assert result == "Ошибка: не указано имя или фамилия"


def test_format_full_name_russian_names():
    """Тест: русские имена"""
    result = format_full_name("иван", "иванов")
    assert result == "Иван Иванов"


# ============================================================================
# ГРУППА 2: Тесты для функции count_vowels_in_text()
# ============================================================================

def test_count_vowels_english():
    """Тест: английские слова"""
    assert count_vowels_in_text("Hello") == 2
    assert count_vowels_in_text("Python") == 1
    assert count_vowels_in_text("AEIOU") == 5


def test_count_vowels_russian():
    """Тест: русские слова"""
    assert count_vowels_in_text("Привет") == 2
    assert count_vowels_in_text("Абракадабра") == 5

def test_count_vowels_empty_string():
    """Тест: пустая строка"""
    assert count_vowels_in_text("") == 0


def test_count_vowels_no_vowels():
    """Тест: строка без гласных"""
    assert count_vowels_in_text("bcdfg") == 0
    assert count_vowels_in_text("прст") == 0


def test_count_vowels_mixed_languages():
    """Тест: смешанные языки"""
    assert count_vowels_in_text("Hello Привет") == 4


# ============================================================================
# ГРУППА 3: Тесты для функции is_palindrome_string()
# ============================================================================

def test_is_palindrome_true():
    """Тест: настоящие палиндромы"""
    assert is_palindrome_string("топот") == True
    assert is_palindrome_string("racecar") == True
    assert is_palindrome_string("А роза упала на лапу Азора") == True


def test_is_palindrome_false():
    """Тест: не палиндромы"""
    assert is_palindrome_string("машина") == False
    assert is_palindrome_string("hello") == False


def test_is_palindrome_case_insensitive():
    """Тест: регистр не имеет значения"""
    assert is_palindrome_string("ТоПоТ") == True
    assert is_palindrome_string("RaceCar") == True


def test_is_palindrome_single_character():
    """Тест: один символ"""
    assert is_palindrome_string("а") == True
    assert is_palindrome_string("") == True


# ============================================================================
# ГРУППА 4: Тесты для функции process_list_of_names()
# ============================================================================

def test_process_list_of_names_normal():
    """Тест: нормальный список имен"""
    input_list = ["john", "JANE", "alex"]
    expected = ["John", "Jane", "Alex"]
    result = process_list_of_names(input_list)
    assert result == expected


def test_process_list_of_names_with_spaces():
    """Тест: имена с пробелами"""
    input_list = ["  john  ", "  JANE  ", "  alex  "]
    expected = ["John", "Jane", "Alex"]
    result = process_list_of_names(input_list)
    assert result == expected


def test_process_list_of_names_with_empty_strings():
    """Тест: список с пустыми строками"""
    input_list = ["john", "", "  ", "JANE"]
    expected = ["John", "Jane"]
    result = process_list_of_names(input_list)
    assert result == expected


def test_process_list_of_names_empty_list():
    """Тест: пустой список"""
    assert process_list_of_names([]) == []


# ============================================================================
# ГРУППА 5: Тесты для функции get_name_initials()
# ============================================================================

def test_get_name_initials_two_part_name():
    """Тест: имя из двух частей"""
    assert get_name_initials("Иван Иванов") == "И.И."
    assert get_name_initials("John Doe") == "J.D."


def test_get_name_initials_three_part_name():
    """Тест: имя из трех частей"""
    assert get_name_initials("Анна Мария Петрова") == "А.М.П."
    assert get_name_initials("John Michael Doe") == "J.M.D."


def test_get_name_initials_single_part_name():
    """Тест: имя из одной части (ошибка)"""
    result = get_name_initials("Одинокоеимя")
    assert result == "Ошибка: имя должно содержать хотя бы имя и фамилию"


def test_get_name_initials_with_extra_spaces():
    """Тест: имя с лишними пробелами"""
    assert get_name_initials("  Иван  Иванов  ") == "И.И."


# ============================================================================
# ПАРАМЕТРИЗОВАННЫЕ ТЕСТЫ (один тест для многих случаев)
# ============================================================================

@pytest.mark.parametrize("first,last,expected", [
    ("john", "doe", "John Doe"),
    ("JANE", "SMITH", "Jane Smith"),
    ("иван", "иванов", "Иван Иванов"),
    ("", "doe", "Ошибка: не указано имя или фамилия"),
    ("john", "", "Ошибка: не указано имя или фамилия"),
])
def test_format_full_name_parametrized(first, last, expected):
    """Параметризованный тест для format_full_name"""
    result = format_full_name(first, last)
    assert result == expected


@pytest.mark.parametrize("text,expected_count", [
    ("Hello", 2),
    ("Python", 1),
    ("Привет", 2),
    ("", 0),
    ("AEIOU", 5),
    ("аеиоу", 5),
])
def test_count_vowels_parametrized(text, expected_count):
    """Параметризованный тест для count_vowels_in_text"""
    result = count_vowels_in_text(text)
    assert result == expected_count, f"Для текста '{text}' ожидалось {expected_count}, получено {result}"


# ============================================================================
# ФИКСТУРЫ (подготовка данных для тестов)
# ============================================================================

@pytest.fixture
def sample_names_list():
    """Фикстура: возвращает тестовый список имен"""
    return ["  john  ", "JANE", "  alex  ", "", "  bob  "]


def test_process_names_with_fixture(sample_names_list):
    """Тест с использованием фикстуры"""
    result = process_list_of_names(sample_names_list)
    
    # Проверяем количество элементов
    assert len(result) == 4
    
    # Проверяем конкретные значения
    assert "John" in result
    assert "Jane" in result
    assert "Alex" in result
    assert "Bob" in result
    
    # Проверяем что пустые строки отфильтрованы
    assert "" not in result
    assert "  " not in result


# ============================================================================
# ТЕСТЫ НА ОШИБКИ И ГРАНИЧНЫЕ СЛУЧАИ
# ============================================================================

def test_edge_case_none_values():
    """Тест: передача None значений"""
    result = format_full_name(None, "doe")
    assert result == "Ошибка: не указано имя или фамилия"


# ============================================================================
# ЗАПУСК ТЕСТОВ ПРИ ПРЯМОМ ВЫПОЛНЕНИИ ФАЙЛА
# ============================================================================

if __name__ == "__main__":
    print("Запуск тестов напрямую...")
    print("=" * 60)
    
    # Импортируем pytest для запуска
    import sys
    
    # Запускаем pytest
    result = pytest.main([__file__, "-v"])
    
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТ ТЕСТОВ:")
    
    if result == 0:
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("❌ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ")
    
    print("=" * 60)

# Лабораторная работа по предмету: Управление проектами интеллектуальных информационных систем

## Описание

Эта лабораторная работа содержит решения для двух задач:

1. Функцию, которая определяет в какой из двух вещественных переменных больше цифр после запятой.
2. Программа для управления списком студентов, включая их экзаменационные расписания.

## Структура проекта

- `src/`
  - `task1.py`: Решение первой задачи.
  - `task2.py`: Решение второй задачи.
- `README.md`: Этот файл с кратким описанием и интерфейсом программы.
- `DOC.md`: Описание варианта задачи.
## Интерфейс программы

### Задание 1

Функция `compare_decimal_places` сравнивает два вещественных числа и возвращает сообщение, указывающее, какое число имеет больше цифр после запятой.

Пример использования:

```python
from src.task1 import compare_decimal_places

num1 = 3.14159
num2 = 2.71828
result = compare_decimal_places(num1, num2)
print(result)

### Задание 2

Программа позволяет создать список студентов с их предметами и датами экзаменов. Она выводит расписание экзаменов в табличном формате.

```python
from src.task2 import Student, Subject, print_exam_schedule
import datetime

students = [
        Student("Ivanov", "Kirill", datetime.date(2000, 5, 15), [
            Subject("Math", datetime.date(2024, 6, 1), "Lavrenov"),
            Subject("History", datetime.date(2024, 6, 15), "Radeonova"),
        ]),
        Student("Petrova", "Elizaveta", datetime.date(2001, 7, 25), [
            Subject("Math", datetime.date(2024, 6, 1), "Lavrenov"),
            Subject("Chemistry", datetime.date(2024, 6, 10), "Hohlov"),
        ]),
    ]

    print_exam_schedule(students)

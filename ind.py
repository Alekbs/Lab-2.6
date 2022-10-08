#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import sys
from datetime import date

if __name__ == '__main__':
    # Список работников.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            name = input("Фамилия и инициалы? ")
            groop = input("Группа? ")
            marks = []
            for i in range(5):
                marks.append(input("Введите оценки по 5 предметам? "))

            # Создать словарь.
            student = {
                'name': name,
                'groop': groop,
                'marks': marks,
            }

            # Добавить словарь в список.
            students.append(student)
            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('marks', ''))

        elif command == 'list':
                    # Заголовок таблицы.
                    line = '+-{}-+-{}-+-{}-+'.format(
                        '-' * 30,
                        '-' * 20,
                        '-' * 8
                    )
                    print(line)
                    print(
                        '| {:^30} | {:^20} | {:^8} |'.format(
                            "Ф.И.О.",
                            "Группа",
                            "Оценки"
                        )
                    )
                    print(line)

                    # Вывести данные о всех студентах.
                    for idx, student in enumerate(students, 1):
                        res = all(int(x) > 3 for x in student['marks'])
                        if res:
                            print(
                                '| {:<30} | {:<20} | {:>8} |'.format(
                                    student.get('name', ''),
                                    student.get('groop', ''),
                                    ''.join(student['marks'])
                                )
                            )
                        else:
                            print("Таких студентов нет")
                    print(line)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывод студентов с оценками 4 и 5;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
            year = date.today().year
            print(year)
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

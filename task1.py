#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = []

    klass = {
        'name': '1a',
        'year': 5,
    }
    school.append(klass)

    klass = {
        'name': '3a',
        'student': 7,
    }
    school.append(klass)

    school[1] = {
        'name': '3a',
        'student': 4,
    }
    klass = {
        'name': '4f',
        'student': 32,
    }
    school.append(klass)

    del(school[0])
    print(
        '| {:>10}  | {:>20} |'.format(
            "Номер класса",
            "Количество учеников"
        )
    )

    for idx, klass in enumerate(school, 1):
        print(
            '| {:>12}  | {:>20} |'.format(
                klass.get('name', ''),
                klass.get('student', 0)
            )
        )
    s = 0
    for idx, klass in enumerate(school, 1):
        s += klass['student']
    print("Количество учеников в школе: ", s)
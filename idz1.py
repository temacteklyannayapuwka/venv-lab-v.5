#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import argparse

# Получаем имя файла данных из переменной окружения, если она установлена
data_file = os.environ.get('STUDENTS_DATA', 'students_data.json')

# Функция для ввода данных о студентах
def input_students():
    students = []  # Создаем пустой список студентов
    n = int(input("Введите количество студентов: "))

    for i in range(n):
        student = {}  # Создаем пустой словарь для каждого студента
        student["фамилия и инициалы"] = input("Введите фамилию и инициалы студента: ")
        student["номер группы"] = input("Введите номер группы: ")
        student["успеваемость"] = []

        for j in range(5):
            grade = int(input(f"Введите оценку {j + 1}: "))
            student["успеваемость"].append(grade)

        students.append(student)  # Добавляем словарь студента в список студентов

    students.sort(key=lambda x: x["фамилия и инициалы"])  # Сортируем студентов по фамилии
    return students

# Функция для вывода студентов с оценкой 2
def print_students_with_grade_2(students):
    found = False
    for student in students:
        if 2 in student["успеваемость"]:
            print(f"Фамилия и инициалы: {student['фамилия и инициалы']}, Номер группы: {student['номер группы']}")
            found = True
    if not found:
        print("Нет студентов с оценкой 2")

# Функция для сохранения данных в файл JSON
def save_data_to_json(students):
    with open(data_file, 'w', encoding='utf-8') as file:
        json.dump(students, file, ensure_ascii=False)

# Функция для чтения данных из файла JSON
def load_data_from_json():
    if os.path.exists(data_file):
        with open(data_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return []

# Функция для выполнения основной части программы
def main():
    parser = argparse.ArgumentParser(description='Manage student data')
    parser.add_argument('--input', action='store_true', help='Input new student data')
    parser.add_argument('--print_grade_2', action='store_true', help='Print students with grade 2')
    args = parser.parse_args()

    if args.input:
        students = input_students()
    else:
        if os.path.exists(data_file):
            students = load_data_from_json()
        else:
            students = input_students()  # Ввод данных о студентах

    if args.print_grade_2:
        print("Студенты с оценкой 2:")
        print_students_with_grade_2(students)  # Вывод студентов с оценкой 2

    save_data_to_json(students)  # Сохраняем данные в файл JSON

# Основная часть программы
if __name__ == "__main__":
    main()  # Вызываем основную функцию

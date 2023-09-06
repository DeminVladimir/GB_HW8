# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

import os


# lst1 = [['Иван', 'Иванов'], ['Петр', 'Петров']]

def get_user_data() -> list:
    name = input('Введите имя: ')
    sur_name = input('Введите фамилию: ')
    phone_num = input('Введите номер телефона: ')
    desc = input('Введите описание: ')
    return [name, sur_name, phone_num, desc]


def create_record(gb_phone_book: list, user_data: list) -> list:
    gb_phone_book.append(user_data)
    return gb_phone_book


def print_phone_book(gb_phone_book: list) -> None:
    for record in gb_phone_book:
        print(record)


def get_file_name() -> str:
    return input('Введите имя файла: ')


def create_from_data(gb_phone_book: list, file_name: str, delimiter: str) -> list:
    path_sourse = os.path.join('.', file_name)
    with open(path_sourse, 'r', encoding='utf-8') as sourse:
        for line in sourse:
            gb_phone_book = create_record(gb_phone_book, line.strip().split(delimiter))
    return gb_phone_book


def data_for_read() -> str:
    return input('Введите фамилию человека: ').capitalize()


def read_from_data(gb_phone_book: list, reader_data: str) -> None:
    for elem in gb_phone_book:
        for request in range(len(elem)):
            if reader_data == elem[request]:
                print(elem)


def update_phone_book(gb_phone_book: list, reader_data: list, user_data: list) -> list:
    for update_line in gb_phone_book:
        for update_idx in range(len(update_line)):
            if reader_data == update_line[update_idx]:
                update_line[:] = user_data
    return gb_phone_book


def del_user_data(gb_phone_book: list, reader_data: list,) -> list:
    for del_line in gb_phone_book:
        for del_idx in range(len(del_line)):
            if reader_data == del_line[del_idx]:
                del_line.clear()
                return gb_phone_book
    return gb_phone_book


def expor_user_data(gb_phone_book: list, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as export_data:
        for export_line in gb_phone_book:
            for export_idx in range(len(export_line)):
                export_data.writelines(export_line[export_idx])
                if export_idx == (len(export_line)-1):
                    export_data.writelines('\n')
                else:
                    export_data.writelines(', ')


def menu():
    phone_book = list()
    while True:
        print('Введите 1 для выхода из справочника')
        print('Введите 2 для создания новой записи')
        print("Введите 3 для вывода данных на экран")
        print("Введите 4 для импорта данных из файла")
        print('Введите 5 для нахождения данных')
        print('Ввудите 6 для изменения данных')
        print('Введите 7 для удаления данных')
        print('Введтье 8 для экспорта данных в файл')
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            return
        if choise == 2:
            phone_book = create_record(phone_book, get_user_data())
        if choise == 3:
            print_phone_book(phone_book)
        if choise == 4:
            phone_book = create_from_data(phone_book, get_file_name(), ',')
        if choise == 5:
            read_from_data(phone_book, data_for_read())
        if choise == 6:
            phone_book = update_phone_book(phone_book, data_for_read(), get_user_data())
        if choise == 7:
            phone_book = del_user_data(phone_book, data_for_read())
        if choise == 8:
            expor_user_data(phone_book, get_file_name())


menu()

with open('book.txt', 'w',encoding='utf-8') as file:
    file.write('name\n')
    file.write('surname\n')
    file.write('number_phone\n')

def add_contact(file_path):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{name}, {surname}, {phone}")
    
def save_to_file(filename):
    with open(filename, 'w',encoding='utf-8') as file:
        print('Контакт сохранен')

def show_contacts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
    
def main():
    file_path = []
    filename = 'book.txt'

    while True:
        print("1. Добавить контакт")
        print("2. Сохранить файл")
        print("3. Вывести все контакты")


        choice = input('Выберите действие: ')
        if choice == '1':
            name = input('Фамилия: ')
            surname = input('Имя: ')
            number_phone= input('Номер телефона: ')
            add_contact(file_path)
        elif choice == '2':
            save_to_file(filename, file_path)
        elif choice == '3':
            show_contacts(file_path)
        elif choice == '8':
            break
        else:
            print('Некорректный выбор. Попробуйте снова')    
if __name__ == "__main__":
    main()


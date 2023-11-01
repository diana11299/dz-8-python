def add_contact(phonebook, name, surname, middle_name, phone_number):
    contact = {
        'name': name,
        'surname': surname,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    phonebook.append(contact)
    print('Контакт добавлен')

def save_to_file(filename, phonebook):
    with open(filename, 'w',encoding='utf-8') as file:
        print('Контакт сохранен')
        

def views_contacts(phonebook):
    for index, contact in enumerate(phonebook, start=1):
        print(f"{index}. {contact['name']}, {contact['surname']}, {contact['middle_name']}, {contact['phone_number']}\n")


def edit_contact(phonebook, search_key, new_data):
    for contact in phonebook:
        if (search_key.lower() in contact['name'].lower() or search_key.lower() in contact['surname'].lower()):
            contact.update(new_data)
            print('Контакт изменен')
            return
    print('Контакт не найден')
    
def delete_contact(phonebook, search_key):
    for contact in phonebook[:]:
        if (search_key.lower() in contact['name'].lower() or search_key.lower() in contact['surname'].lower()):
            phonebook.remove(contact)
            print('Контакт удален')
            return
    print('Контакт не найден')

def main():
    phonebook = []
    filename = 'contacts.txt'

    while True:
        print("1. Добавить контакт")
        print("2. Сохранить файл")
        print("3. Вывести все контакты")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")

        choice = input('Выберите действие: ')
        if choice == '1':
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            middle_name = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
        elif choice == '2':
            save_to_file(filename, phonebook)
        elif choice == '3':
            views_contacts(phonebook)
        elif choice == '4':
            search_key = input("Введите имя или фамилию для изменения: ")
            new_name = input('Новая фамилия: ')
            new_surname = input('Новое имя: ')
            new_middle_name = input('Новое отчество: ')
            new_phone_number = input('Новый номер телефона: ')
            new_data = {
                'name': new_name,
                'surname': new_surname,
                'middle_name': new_middle_name,
                'phone_number': new_phone_number
            }
            edit_contact(phonebook, search_key, new_data)
        elif choice == '5':
            search_key = input("Введите имя или фамилию для удаления: ")
            delete_contact(phonebook, search_key)
        elif choice == '6':
            break
        else:
            print('Некорректный выбор. Попробуйте снова')

if __name__ == "__main__":
    main()
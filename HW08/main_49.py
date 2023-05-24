# Задача 49
# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def file_read(f_name) -> list:  # read file data into data
    data = open(f_name).read().split('\n')
    return [i.split(':') for i in data]

def file_write(f_name, data: list) -> None:  # write data into specified file
    data = [':'.join(map(str, data[i])) for i in range(len(data))]
    open(f_name, 'w').writelines('\n'.join(map(str, data)))

def show_records(data: list, fields: list, elem_show=[-1]) -> None: # print the list by specified indixes
    if elem_show[0] == -2: #nothing to show - service value
        print("No records found for this search!\n")
    else:
        if elem_show[0] == -1:  # by default -> print all data
            elem_show = range(len(data))
            print("\nALL RECORDS:")
        else:
            print("\nRECORDS FOUND:")

        print('\t '.join(fields))
        print("⸻" * 60)
        print('\n'
            .join(map(str, [data[i] for i in elem_show]))
            .replace("[", "")
            .replace("]", "")
            .replace('\'', "")
            .replace(",", "\t\t"))

def add_record(data: list, fields: list) -> list: # add contact to data set
    print("\nADDING A NEW RECORD:")
    new_line = [input(f"enter the {fields[i]}:\t") for i in range(len(fields))]
    data.append(new_line)
    return data

def find_record(data: list) -> list: #find all the records matvhing the criteria
    search_val = input(f"\nEnter a search value\n(name, surname, tel number, comment or their combination sep with a space): ").split()
    res = [x for x in range(len(data)) if all(map(lambda v: v in data[x], search_val))]
    
    if len(res) == 0:
        res = [-2]
    
    return res

def modify_record(data: list, fields: list) -> list: #modify the record found by criteria
    print("\nRECORD MODIFICATION MODE")
    
    rec_modify = [-1]
    while rec_modify[0] < 0 or len(rec_modify) > 1:
        rec_modify = find_record(data)
        show_records(data, fields, rec_modify)
        if len(rec_modify) > 1:
            print("\nMore than 1 record matches your search - use several fields to specify!")
    
    fld_modify = int(input(f"\nWhich field would you like to modify (1-5)?\n(1 - surname, 2 - name, 3 - tel number, 4 - comment, 5 - NO change): ")) - 1

    if 0 <= fld_modify < 5:
        data[rec_modify[0]][fld_modify] = input(f"Enter new value for field \'{fields[fld_modify]}\' to replace current value \'{data[rec_modify[0]][fld_modify]}\': ")
    
    return data

def delete_record(data: list, fields: list) -> list: #delete the record found by criteria
    print("\nRECORD DELETION MODE")
    
    rec_modify = [-1]
    while rec_modify[0] < 0 or len(rec_modify) > 1:
        rec_modify = find_record(data)
        show_records(data, fields, rec_modify)
        if len(rec_modify) > 1:
            print("\nMore than 1 record matches your search - use several fields to specify!")
    
    del_confirm = input("\nConfirm you would like to delete record specified above (Y/N): ")
    
    if del_confirm == 'Y' or del_confirm == 'y':
        data.pop(rec_modify[0])
    
    return data

    
file_name = 'phones.txt'
data_fields = ['last name', 'first name', 'tel number', 'comment']
data = file_read(file_name)

while 1:

    print('''
    COMMANDS FOR TELEPHONE BOOK:
    All record review - 1
    Search for the record - 2
    Adding new record - 3
    Deletion of the record - 4
    Modification of the record - 5
    Exit - 0 ''')

    command = int(input('\nChoose your command: '))
    if command == 1: #show all records
        show_records(data, data_fields)
    elif command == 2: # show the records found
        show_records(data, data_fields, find_record(data))
    elif command == 3: #add record
        add_record(data, data_fields)
    elif command == 4: #delete record
        delete_record(data, data_fields)
    elif command == 5: #delete record
        modify_record(data, data_fields)
    elif command == 0: #save & exit
        file_write(file_name, data)
        break
    else:
       print('\nThe command does NOT exists! Try again.')


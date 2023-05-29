phone_book: list[dict[str, str]] = []
path = 'phones.txt'


def open_pb():
    global phone_book

    phone_book = [] #otherwise re-open of database will add new (same) lines to already opened data

    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()  # as our lines in file are sep by \n

    for contact in data:
        contact = contact.strip().split(':')
        new = {'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]}
        phone_book.append(new)


def save_pb():
        global phone_book
        data = []
        for contact in phone_book:
             data.append(':'.join([value for value in contact.values()]))
        data = '\n'.join(data)

        with open(path, 'w', encoding = 'UTF-8') as file:
             file.write(data)


def get_pb():
    global phone_book
    return phone_book


def add_contact(new: dict[str, str]) -> str:
    global phone_book

    new_id = int(phone_book[-1].get('id')) + 1 #index to add
    new['id'] = str(new_id)

    phone_book.append(new)
    
    return new.get('name')


def search_contact(word: str) -> list[dict[str, str]]:
    global phone_book
    res = []

    for contact in phone_book:
        for fld in contact.values():
            if word.lower() in fld.lower():
                res.append(contact)
                break

    return res


def modify_contact(new: dict, index: int):
     global phone_book
     for contact in phone_book:
          if index == contact.get('id'):
            contact['name'] = new.get('name', contact.get('name'))
            contact['phone'] = new.get('phone', contact.get('phone'))
            contact['comment'] = new.get('comment', contact.get('comment'))
            return contact.get('name')
          

def delete_contact(index: int) -> str:
     global phone_book
     
     for i in range(len(phone_book)):
          if index == phone_book[i].get('id'):
            name = phone_book[i].get('name')
            del phone_book[i]
            return name
     
                  
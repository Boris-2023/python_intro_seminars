class PhoneBook:

    def __init__(self, path: str = 'phones.txt'):
        self._phone_book: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0

    def open(self):
        self._phone_book = []# otherwise re-open of database will add new (same) lines to already opened data
        with open(self._path, 'r', encoding='UTF-8') as file:
            data = file.readlines()  # as our lines in file are sep by \n
        for contact in data:
            contact = contact.strip().split(':')
            new = {'id': contact[0], 'name': contact[1],
                   'phone': contact[2], 'comment': contact[3]}
            self._phone_book.append(new)

    def save(self):
        data = []
        for contact in self._phone_book:
            data.append(':'.join([value for value in contact.values()]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def load(self):
        return self._phone_book

    def add(self, new: dict) -> str:
        self._last_id = int(self._phone_book[len(self._phone_book)-1]['id']) + 1
        new['id'] = str(self._last_id)
        self._phone_book.append(new)
        return new.get('name')

    def search(self, word: str) -> list[dict[str, str]]:
        res: list[dict[str, str]] = []
        for contact in self._phone_book:
            for fld in contact.values():
                if word.lower() in fld.lower():
                    res.append(contact)
                    break

        return res

    def modify(self, new: dict, index: int):
        for contact in self._phone_book:
            if index == contact.get('id'):
                contact['name'] = new.get('name', contact.get('name'))
                contact['phone'] = new.get('phone', contact.get('phone'))
                contact['comment'] = new.get('comment', contact.get('comment'))
                return contact.get('name')

    def delete(self, index: int) -> str:
        for i in range(len(self._phone_book)):
            if index == self._phone_book[i].get('id'):
                name = self._phone_book[i].get('name')
                del self._phone_book[i]
                return name

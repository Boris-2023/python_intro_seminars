import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_msg(msg: str):
    print('\n' + '='*len(msg))
    print(msg)
    print('='*len(msg) + '\n')


def print_contacts(book: list[dict[str, str]], error: str):
    msg_len = 70
    if book:
        print('\n' + '='*msg_len)
        for contact in book:
            print(f'{contact.get("id"):>3}.{contact.get("name"):<20} | {contact.get("phone"):^20} | {contact.get("comment"):<20}')
        print(msg_len*'=' + '\n')
    else:
        print_msg(error)


def input_contact(msg: str) -> dict[str, str]:
    new = {}
    print_msg(msg)
    for key, txt in text.new_contact.items():
        if(key != 'id'):
            cur_val = input(txt)
            if cur_val:
                new[key] = cur_val
        else:
            new[key] = '0'

    print('\n' + str(new))
    return new


def input_search(msg: str) -> str:
    return input(msg)


def confirm_delete(name: str):
    confirm = input(text.delete_confirm(name)).lower()
    if confirm == 'y':
        return True
    else:
        return False

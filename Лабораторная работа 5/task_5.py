import string
from random import sample


def get_random_password(n: int = 8) -> str:
    string_password = string.ascii_uppercase + string.ascii_lowercase + string.digits  # строка-алфавит
    password = "".join(sample(string_password, n))  # создание пароля
    return password


print(get_random_password())

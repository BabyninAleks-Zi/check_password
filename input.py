PASSWORD = input('Введите пароль:')
SCORE = 'Рейтинг пароля:'


def is_very_long(PASSWORD):
    return len(PASSWORD) > 8


def has_digit(PASSWORD):
    return any(symbol.isdigit() for symbol in PASSWORD)


def has_upper_letters(PASSWORD):
    return any(symbol.isupper() for symbol in PASSWORD)


def has_lower_letters(PASSWORD):
    return any(symbol.islower() for symbol in PASSWORD)


def has_symbols(PASSWORD):
    return any(not symbol.isdigit() and
        not symbol.isalpha() for symbol in PASSWORD)


list_rating = [
    is_very_long,
    has_digit,
    has_upper_letters,
    has_lower_letters,
    has_symbols
]
rating = 0
for rating_result in list_rating:
    if rating_result(PASSWORD):
        rating += 2

print(SCORE, rating)

import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Fat Cat!'

    if p_message == 'roll':
        return (random.randint(1, 999999999999))

    if p_message == '!game':
        return '`Fat Cats Fat Cats Fat Cats Fat Cats Fat Cats Fat Cats Fat Cats Fat Cats Fat Cats Fat Cats Fat Cats .`'

    if p_message == 'FatCat':
        return 'Fat Cats!'

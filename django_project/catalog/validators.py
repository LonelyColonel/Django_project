from django.forms import ValidationError


def validate_amazing(value):
    must_be_in_our_item = ['Превосходно', 'Роскошно', 'Amazing', 'Wonderful']

    # for i in must_be_in_our_item:
    #     if i.lower() not in value.lower():
    #         raise ValidationError(f'Обязательно нужно использовать слова {", ".join(must_be_in_our_item)}!')
    if not any(filter(lambda x: x.lower() in value.lower(), must_be_in_our_item)):
        raise ValidationError(f'Обязательно нужно использовать слова {", ".join(must_be_in_our_item)}!')

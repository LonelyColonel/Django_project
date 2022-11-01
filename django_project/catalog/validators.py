from django.forms import ValidationError


def validate_amazing(*args):
    from functools import wraps

    @wraps(args)
    def validator(value):
        must_be_in_our_item = args

        if not any(filter(lambda x: x.lower() in value.lower(), must_be_in_our_item)):
            raise ValidationError(f'Обязательно нужно использовать слова {", ".join(must_be_in_our_item)}!')
        return value

    return validator

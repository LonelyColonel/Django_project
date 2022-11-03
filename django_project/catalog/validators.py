from django.core.exceptions import ValidationError
from functools import wraps
import re


def validate_amazing(*args):

    @wraps(validate_amazing)
    def validator(value):
        pattern = re.compile(fr'.*(\b({"|".join(args)})\b).*', re.I)
        for i in value.split('\n'):
            if re.fullmatch(pattern, i):
                return value
        raise ValidationError(f'Обязательно нужно использовать слова {", ".join(args)}.')

    return validator

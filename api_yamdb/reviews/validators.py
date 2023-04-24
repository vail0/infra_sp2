from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validator(value):
    if value < 1 or value > timezone.now().year:
        raise ValidationError(
            ('%(value)s неверный год'),
            params={'value': value},
        )

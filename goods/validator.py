from django.core.exceptions import ValidationError

def validate_select_option(value):
    if value == '':
        raise ValidationError('Ви повинні обрати поле')
from django.core.exceptions import ValidationError

def validate_symbols(value):
    if ("@" in value) or ("#" in value) or ('&' in value):
        raise ValidationError('You can`t include "@" or "#" or "&" here.', code='symbol-err')
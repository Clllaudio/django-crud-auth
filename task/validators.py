import re
from django.core.exceptions import ValidationError

def validar_contrasena_segura(value):
    # Verificar longitud mínima
    if len(value) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
    
    # Verificar si contiene al menos una letra mayúscula
    if not re.findall(r'[A-Z]', value):
        raise ValidationError('La contraseña debe contener al menos una letra mayúscula.')
    
    # Verificar si contiene al menos un número
    if not re.findall(r'\d', value):
        raise ValidationError('La contraseña debe contener al menos un número.')
    
    # Verificar si contiene al menos un carácter especial
    if not re.findall(r'[!@#$%^&*(),.?":{}|<>_]', value):
        raise ValidationError('La contraseña debe contener al menos un carácter especial (!@#$%^&*(),.?":{}|<>).')

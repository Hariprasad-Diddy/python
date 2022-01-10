import string
from random import choices


def password_generate():
    """
    This function create random Password and the length of the password was 12 with containing Characters,Digits and Special Characters
    """
    char_num_special = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choices(char_num_special,k=12))
    return password


created_password = password_generate()
print(created_password)
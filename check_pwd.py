def check_pwd(s):
    special_characters = set("~`!@#$%^&*()_+-=")
    if len(s) < 8 or len(s) > 20:
        return False
    if not any(char.isupper() for char in s):
        return False

    if not any(char.islower() for char in s):
        return False

    if not any(char.isdigit() for char in s):
        return False
    if not any(char in special_characters for char in s):
        return False

    return True


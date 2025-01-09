def check(psw):

    lenth = len(psw)
    if (lenth<6 or lenth >12):
        return False
    

    # has_lower = any(char.islower() for char in psw)
    # has_upper = any(char.isupper() for char in psw)
    # has_digit = any(char.isdigit() for char in psw)
    # has_special = any(char in "@!#$%&" for char in psw)

    has_lower = [char for char in psw if char.islower()]
    has_upper = [char for char in psw if char.isupper()]
    has_digit = [char for char in psw if char.isdigit()]
    has_special = [char for char in psw if char in "@!#$%&"]

    a = len(has_lower)
    b = len(has_upper)
    c = len(has_digit)
    d = len(has_special)

    print(a,b,c,d)

    if a and b and c and d:
        return True
    else:
        return False
    
psw = input("Password:")
print(f'Is valid {check(psw)}')

while True:
    try:
        password = input("Enter a password ")
        if len(password) < 8:
            raise ValueError(" at least minimam 8 charater ")
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        for character in password:
            if character.isupper():
                has_upper = True
            if character.islower():
                has_lower = True
            if character.isdigit():
                has_digit = True
            if not character.isalnum():
                has_special = True
        if has_upper == False:
            raise ValueError("at least one upper case")
        if has_lower == False:
            raise ValueError("at least one lower case")
        if has_digit == False:
            raise ValueError("at least one digit case")
        if has_special == False:
            raise ValueError("at least one special character")
        print("valid password")
        print(password)  
        break
    except Exception as e:
        print(e)




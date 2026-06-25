password = "Security@123"

is_valid_length = False

if 8 <= len(password) <= 16:
    is_valid_length = True
    print("length of password is ok")

print(is_valid_length)


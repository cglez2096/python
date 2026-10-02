
import bcrypt

password = b"thisismypassword"

hash = bcrypt.hashpw(password,bcrypt.gensalt())
print(hash)

enter_password = input('Enter your password')
enter_password = bytes(enter_password, encoding='utf-8')

if bcrypt.checkpw(enter_password,hash):
    print("Login Successfully")
else:
    print("Invalid Password")



from hashlib import sha256
from os import path


salt = path.basename(__file__)

pass1 = input("Введите пароль:")
hash_obj1 = sha256(salt.encode("UTF-8") + pass1.encode("UTF-8"))
hex_dig_res1 = hash_obj1.hexdigest()

try:
    with open("hash.txt", "w") as hash_file:
        print(hex_dig_res1, file=hash_file, end="")
    print("В базе данных хранится строка: ", hex_dig_res1)
except:
    print("проблема с файлом")
    exit(1)

pass2 = input("Введите пароль еще раз для проверки:")
hash_obj2 = sha256(salt.encode("UTF-8") + pass2.encode("UTF-8"))
hex_dig_res2 = hash_obj2.hexdigest()

try:
    with open("hash.txt", "r") as hash_file:
        hex_dig_res_old = hash_file.readline()
except:
    print("проблема с файлом")
    exit(1)

if hex_dig_res2 == hex_dig_res_old:
    print("Вы ввели правильный пароль")
else:
    print("Вы ввели не правильный пароль")
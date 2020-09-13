import hashlib
import random
import string
from datetime import datetime
import time

# пароль и количесво символов в пароле 
password = 'yA64tpab'
quantity = 0

hash_object = hashlib.md5(password.encode()) # шифрование пароя 

print(hash_object.hexdigest()) # вывидение хеша пароля 

start_time = datetime.now() # запуск таймера для посчета времени исполнение подбора 

for x in password: # подсщет количесво символов в пароле
	quantity += 1


while True: # подбор пароля
	hellocarl = (''.join(random.choice(string.ascii_letters + string.digits) for i in range(quantity)))
	if hashlib.md5(hellocarl.encode()).hexdigest() == hash_object.hexdigest(): # проверка хеша на совпадение
		print(datetime.now() - start_time) # вывод этога таймера












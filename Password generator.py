import random

a = "qwertyuiopasdfghjklzxcvbnm"
b = "QWERTYUIOPLKJHGFDSAZXCVBNM"
c = "0123456789"
d = "()-=_+*&^%$#@!:}{?><"

all = a + b + c + d

lentgh = int(input("Lentgh of password: "))

if lentgh >= 8:
    print("Reliable amount symbols")
    password = "".join(random.sample(all, lentgh))
    print(password)
else:
    print("Amount symbol must be more then 8 or equal this number, your", lentgh)

    input()


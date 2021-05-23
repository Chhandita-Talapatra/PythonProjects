import random
import string
size=int(input("Enter the size of CAPTCHA : "))
captcha=""
for i in range(size) :
    captcha=captcha+"".join([random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)])
print("CAPTCHA is : ",captcha)
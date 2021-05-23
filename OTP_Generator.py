import random
n=int(input("Enter the length of the OTP: "))
otp=0
for i in range(n):
    otp=otp*10+random.randint(0,9)
print("Your one tine password is : ",otp)
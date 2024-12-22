import time 
from lib.mathlib import *
from lib.crlib import *
from lib.inputlib import *
# def gen_gen(p):
#     i =0 
#     while i != p-1:
#         g = random.randint(1 , p-2 )
#         for i in range(1 , p-2  ):
#             if g** i ==1:
#                 break 
#     return g     









p = get_prime(100000 , 999999)        
# p = int(input("enter the p value : "))
print("p value : " , p)


g = getGenrator( p )
print("g value : " , g)
m = intput("enter the value of m : ")
k = intput("enter the k value : ")
secret_key = intput("enter the s value : ")


A = pow(g, secret_key , p)

public_key = (p,g,A)

ft = time.time()

cipher = elgamal_encrypt(public_key , m,k)
st= time.time()
print(st - ft )
print("cipher text : " , cipher)
message = elgamal_decrypt(public_key , cipher , secret_key )
print("public key : " , public_key )
print("secret Key  : ",secret_key)
print("message : " , message)


sign = elgamal_sign(public_key, k ,secret_key , m )

print("digital is signed  : " , elgamal_verify(public_key,sign , m) )
import time

from lib.crlib import *
from lib.inputlib import *





    
# def cmp_methodes(m , e,n):
#     ft = time.time()
#     print("result by the first methode :" , (m**e)%n)
#     st = time.time()
#     print("time to finish excuting : " , st-ft)
#     ft = time.time()
#     print("result by the second methode :" , expo_iter(m , e )%n)
#     st = time.time()
#     print("time to finish excuting : ", st - ft)
#     ft = time.time()
#     print("result by the third methode :" , pow(m , e, n))
#     st = time.time()
#     print("time to finish excuting : " , st-ft)
#     return pow(m , e, n)

m = intput("inter m : ")
p = intput("inter p : ")
q = intput("inter q : ")
n = intput("inter n : ")
e = intput("inter e : ")
phi =  (p-1)*(q-1)
if(gcd(n,phi)!= 1 ): 
    raise Exception("n is coprime to p !!!")
    



ft = time.time()  
c = rsa_encrypt(m,e,n) 
st = time.time()
print("the cipher is : " ,c  )
print(st - ft )
d = get_private_key(e, phi)
print("the private key is ; " , d)

print("the plain is : " , rsa_decrypt(c , d, n))


sign = rsa_sign((d ,n ) ,m )
print("the sign is created by this owner : " , rsa_verify((e, n ),m , sign))
# result = mod_exp(base , exp , mod)
# print("result : " , result)



# plain_text = input("enter the text you want to encrypt : ")


# inter m : 1822
# inter p : 577
# inter q : 719
# inter n : 414863
# inter e : 65537


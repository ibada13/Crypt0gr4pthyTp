import hashlib 
from lib.mathlib import *
from typing import Tuple
from lib.mathlib import *
########################## rsa ##################################



def rsa_encrypt(m , e, n):
    return pow(m , e,n)

def rsa_decrypt(c , d , n):
    return pow(c ,d, n)

def get_private_key(e,phi):
    return modinv(e ,phi)

def rsa_sign(secret_key , m):
    d,n = secret_key
    h = hashlib.sha256(str(m).encode('utf-8')).hexdigest()
    # print("hash from sign_gen : " , h)
    hint =  int( h ,16)
    return  rsa_decrypt( hint, d, n)

def rsa_verify(public_key ,m, sign):
    e,n = public_key
    h = hashlib.sha256(str(m).encode('utf-8')).hexdigest()
    # print("hash from check_sign : " , h)

    hint = int(h,16) 
    return hint%n == rsa_encrypt(sign , e,n )














#################### EL-GAMAL #########################

def elgamal_encrypt(public_key:Tuple[int , int  , int] , m  , k):
    p,g,A = public_key
    c1 =  pow(g, k, p)
    c2 =   m * pow(A, k, p) % p
    return c1,c2


def elgamal_decrypt(public_key,cipher , secret_key):
    c1 , c2 = cipher 
    p,g,A = public_key
    m1 = pow(c1 ,secret_key,p)
    s = modinv(m1 , p)
    
    return s*c2  %p

def elgamal_sign(public_key , k ,  secret_key , m ): 
    p , g , A = public_key 
    r = pow(g, k , p )
    kinv = modinv( k , p -1 )
    h=  int(hashlib.sha256(str(m).encode('utf-8')).hexdigest(),16)
    s = (kinv * (h - secret_key * r)) % (p - 1)
    return (r,s )



def elgamal_verify(public_key  , sign , m   ):
    p , g , A = public_key 
    r,s = sign 
    h=  int(hashlib.sha256(str(m).encode('utf-8')).hexdigest(),16)
    # h = m 
    return (pow(r,s,p)*pow( A , r,p)   )%p == pow(g, h , p)
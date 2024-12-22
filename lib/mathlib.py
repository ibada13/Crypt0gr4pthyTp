import random 
def pow(base:int, exponent:int, mod:int|None =None)->int:
    if mod is None:
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2
        return result
    else:
        result = 1
        base %= mod
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exponent //= 2
        return result
    


def egcd(a:int, b:int)->int:
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)






def check_prime(p : int)->int:
    for i in range(2 , p //2):
        if (p % i == 0 ):
            return False
    return True



def get_prime(a:int , b:int )->int:
    p =random.randint(a,b)
    while check_prime(p) == False:
        p =random.randint(a,b)

    return p


def gcd(a:int, b:int)->int:
    while b:
        a, b = b, a % b
    return a


def coprime_with(a:int , b:int )->bool:
    return gcd(a, b) == 1 




def getGenrator(p :int)->int:
    g = random.randint( 1 ,p)
    while coprime_with( g, p) ==False :
        g = random.randint( 1 ,p)
    return g




def expo_iter(base:int,exp:int)->int:
    res = 1 
    while(exp != 0 ):
        res *=base
        exp-=1
    return res



def mod_exp(base:int , exp:int , mod:int)->int:
    return expo_recer(base,exp )% mod




# def mod_inverse(a, m):
#     m0, x0, x1 = m, 0, 1
#     while a > 1:
#         q = a // m
#         a, m = m, a % m
#         x0, x1 = x1 - q * x0, x0
#     if x1 < 0:
#         x1 += m0
#     return x1 if m == 1 else None

    
def modinv(a:int, m:int)->int:
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m



def lcm(a:int, b:int)->int:
    return abs(a * b) // gcd(a, b)



def expo_recer(base:int , exp:int )->int:
    if(exp ==0):
        return 1

    else:
        return base*expo_recer(base ,exp-1 )
    

def pow1(base:int , exp:int , mod :int )->int:
    
    x = base 
    y = exp 
    s = 1
    while y!=0:
        s= s*x % mod
        y = y-1

    return s
        

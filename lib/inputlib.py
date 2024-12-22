from typing import Any
from decimal import Decimal
def floanput(prompt:Any , onerror :Any = "Input must be a valid float.")->float :
    try:
        return float(input(prompt))
    except ValueError:
        print( onerror)
        return floanput(prompt , onerror=onerror)

def intput(prompt:Any , onerror :Any= "Input must be a valid int.")->int:
    return int(floanput(prompt , onerror=onerror) )
    


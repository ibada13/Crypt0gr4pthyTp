from typing import Any
def numinput(prompt:Any)->int :
    try:
        return int(input(prompt))
    except ValueError:
        print("Input must be a valid number." )
        return numinput(prompt)
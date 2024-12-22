from typing import Any
def numinput(prompt:Any)->float|int :
    try:
        return float(input(prompt))
    except ValueError:
        print("Input must be a valid number." )
        return numinput(prompt)
def numinput(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Input must be a valid number.")
        return numinput(prompt)
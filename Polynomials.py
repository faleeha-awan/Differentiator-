def diff():
    polynomial = input("Input a polynomial: ")
    variable = "x"


    terms = polynomial.split("+")
    for term in terms:
        if variable in term:
            if "^" in term:
                parts = term.split(variable)
                coefficient = int(parts[0]) if parts[0] else 1
                power = int(parts[1][1:])
            else:
                coefficient = int(term[:-1]) if term[:-1] else 1
                power = 1
            new_coefficient = coefficient * power
            new_power = power - 1
            if new_power == 0:
                print(new_coefficient)
            elif new_power == 1:
                print(new_coefficient, variable)
            else:
                print(new_coefficient, variable, "^", new_power)
            
            
diff()
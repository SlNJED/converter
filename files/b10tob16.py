def b10_b16(decimal_number):
    number = int(decimal_number)
    result = ""
    
    for i in decimal_number:
        remainder = number%16
        number = number//16
        
        if remainder > 9:
            result += hexa_value[str(remainder)]
        else:
            result += str(remainder)
        
        if number <= 0:
            break

    return result[::-1]
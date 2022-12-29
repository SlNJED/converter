from Result import Result

def b2tob10(binary_number: str):
    number = binary_number.replace(' ', '')[::-1]
    return sum([int(value)*(2**i) for i, value in enumerate(number)])
    
            
print(b2tob10("10 0111 0000 1111")) # 0010 0111 0000 1111 = 9999



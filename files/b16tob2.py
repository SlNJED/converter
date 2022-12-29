# HEXA TO BINARY          
def b16_b2(number):
    hexa_nb = number
    result = ""

    for i in hexa_nb:
        total = ""
        if i.isdigit():
            i = int(i)
        else:
            i = int([key for key, value in hexa_value.items() if value == i][0])
        
        for digit in range(4):
            total += str(i%2)
            i = i//2
        result += total[::-1]
    
    return result
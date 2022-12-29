# HEXA TO DECIMAL
def b16_b10(number):
    
    result = 0
    number = number[::-1]
    for i in range(0, len(number)):
        if number[i].isdigit():
            result += int(number[i])*(16**i)
        else:
            result += int([key for key, value in hexa_value.items() if value == number[i]][0])*(16**i)

    return result
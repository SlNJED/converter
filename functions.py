hexa_value = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F"
}

def check_base_input(string):
    while True:
        var = int(input(string))
        if not var in [2, 10, 16]:
            print("You must choose between base 2, 10 or 16 try again ...")
            continue
        else:
            break
    return var

print("[NUMBER CONVERTER BASE2, BASE10, BASE16]\n")

# BASE 2 to BASE 10
def b2_b10(binary_number: str):
    number = binary_number.replace(' ', '')[::-1]
    return sum([int(value)*(2**i) for i, value in enumerate(number)])

# BASE 2 to BASE 16
def b2_b16(binary_number: str):
    number = binary_number.replace(' ', '')[::-1]

    nb_list = [number[i:i + 4 ] for i in range(0, len(number), 4)]
    
    result = ""
    for i in nb_list:
        total = sum([int(value)*(2**i) for i, value in enumerate(i)])
        if total > 9:
            result += hexa_value[str(total)]
        else:
            result += str(total)

    return result[::-1]



# BASE 10 NUMBER CONVERTER INTO BASE 2 NUMBER
def b10_b2(decimal_number: str):
    nb = int(decimal_number)
    
    result = ""
    for i in range(8 * ( (nb//255) + 1 )):
        result += str(nb%2)
        nb = nb//2
    result = result[::-1]
    
    index = 0
    for i in result:
        if i == "0":
            index += 1
        else:
            break
        
    return result[index:len(result)]

# BASE 10 TO BASE 16 
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
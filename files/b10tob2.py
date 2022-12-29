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
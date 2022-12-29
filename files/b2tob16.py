hexa_value = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F"
}

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
def add_space(number):
    result = ""
    for i, value in enumerate(number):
        result += value
        if i+1 and (i+1)%4 == 0:
            result += " "
        
    return result

var = "00110010"
print(var)
var = add_space(var)
print(var)
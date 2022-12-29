from functions import *

BASE2 = 2       # BINARY
BASE10 = 10     # DECIMAL
BASE16 = 16     # HEXADECIMAL

while True:
    
    print("-------------------------")
    number = input("Please enter a number (type exit to exit) --> ")

    if number == "exit":
        break
    
    base_number = check_base_input("\nEnter the base of your number (2, 10, 16):\n\n--> ")
    
    if base_number == 2:
        decimal = b2_b10(number)    # BASE 2 TO BASE 10
        hexa = b2_b16(number)       # BASE 2 TO BASE 16
        
        print(f"\nFROM [B2]: {number}\n\nTO:\t[B10] {decimal}\n\t[B16] {hexa}\n")

    elif base_number == 10:
        binary = b10_b2(number)  # BASE 10 TO BASE 2
        hexa = b10_b16(number)   # BASE 10 TO BASE 16
        
        print(f"\nFROM [B10]: {number}\n\nTO:\t[B2] {binary}\n\t[B16] {hexa}\n")
        
    elif base_number == 16:
        binary = b16_b2(number)  # BASE 16 TO BASE 2
        decimal = b16_b10(number) # BASE 16 TO BASE 10

        print(f"\nFROM [B16]: {number}\n\nTO:\t[B2] {binary}\n\t[B10] {decimal}\n")
        
        
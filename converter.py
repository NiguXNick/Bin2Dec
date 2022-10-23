def BinToDec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

def main():
    binary = input("Enter a binary number: ")
    decimal = BinToDec(binary)
    print("The decimal equivalent is", decimal)

main()

import random
def main():
    cont = True
    op = ["ENCODE", "DECODE", "EXIT"]
    while cont == True:
        print("This is the Caeser Cipher program, a program which will encode or decode any text based on an integer key provided.")
        eDE = input("Please enter encode or decode to encode or decode your text, otherwise enter exit to exit the program: ")
        eDE = eDE.upper()
        if eDE != op[0] and eDE != op[1] and eDE != op[2]:
            while eDE != op[0] and eDE != op[1] and eDE != op[2]:
                eDE = input("That was an incorrect choice please try again: ")
                eDE = eDE.upper()
        if eDE == op[0]:
            str = input("Please input the text you would like to encode : ")
            key = random.randrange(26)
            tsr = encode(str, key)
            print(f"your text after encryption is the following: {tsr} \nthe key for this text is: {key}" )
        elif eDE == op[1]:
            str = input("Please input the text you would like to decode: ")
            key = int(input("Next please inpt the key of the encryption: "))
            if not(isinstance(key, int)) and not(key > 0) and not(key <= 25):
                while not(isinstance(key, int)) and not(key > 0) and not(key <= 25):
                    key = input("\nThat was an incorrect key please try again.")
            tsr = decode(str, key)
            print(f"your text after decryption is the following: {tsr} \nthe key for this text is: {key}")
        else:
            exit()

def encode(str, key):
    tsr = ""
    str = str.upper()
    for char in str:
        temp = ord(char)
        if temp + key > 90:
            temp = temp + key - 26
        else:
            temp += key
        tsr += chr(temp)
    return tsr



def decode(str, key):
    tsr = ""
    str = str.upper()
    for char in str:
        temp = ord(char)
        if temp - key < 65:
            temp = temp - key + 26
        else:
            temp -= key
        tsr += chr(temp)
    return tsr




main()
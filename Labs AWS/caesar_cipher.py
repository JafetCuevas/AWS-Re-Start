def getDoubleAlphabet(alphabet):
    doubleAlphabet =  alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
def runCaesarCipherProgram():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    doubleAlphabte = getDoubleAlphabet(alphabet)
    message = getMessage()
    myCipherKey = getCipherKey()
    #negativeCipherKey = cipherKey*(-1)
    
    encryptedMessage = encryptMessage(message, myCipherKey, alphabet)
    print(f'El alfabeto que estamos usando para encriptar es: {alphabet} "/n"\
    El mensaje original es: {message} "/n" \
    El mensaje cifrado es: {encryptedMessage}')
    
    decryptedMessage = decryptMessage(encryptedMessage, myCipherKey, alphabet)
    print(f'El mensaje desencriptado es: {decryptedMessage}')
    
runCaesarCipherProgram()
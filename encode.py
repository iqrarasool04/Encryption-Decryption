#creating bifid square using key
def creatingBifidSquare():
    key = 'BGWKZQPNDSIOAXEFLCUMTHYVR'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    key = key.upper()
    key_2d = [list(key[i:i+5]) for i in range(0, len(key), 5)]
    square = key_2d
    for row in key_2d:
        print('\t'.join(row))
    print(square)

    return square

#for cipher text in numbers
def bifidEncodingNum(message, square):
    message = message.upper().replace('J', 'I')  
    nums_i = []
    nums_j = []
    for char in message:
        for i in range(5):
            for j in range(5): 
                if square[i][j] == char:
                    nums_j.append(str(j + 1))
                    nums_i.append(str(i + 1))
    return ''.join(nums_i + nums_j)


#for cipher text in alphabets
def bifidEncodingAlpha(encoded, square, key):
    decoded = ''
    i_next = False
    for char in encoded:
        if i_next:
            i = int(char) - 1
            decoded += square[j][i]
            i_next = False
        else:
            j = int(char) - 1
            i_next = True
    return decoded

#calling functions
key = 'BGWKZQPNDSIOAXEFCLUMTHYVR'
Message = 'In cryptography the smallest mistakes can lead to the biggest secrets'
bifidSquare = creatingBifidSquare()
print('Encoding:')
encodedMessage = bifidEncodingNum(Message, bifidSquare)
print("Cipher Text (numbers):", encodedMessage)
decodedMessage = bifidEncodingAlpha(encodedMessage, bifidSquare, key)
print("Cipher Text (alphabets):", decodedMessage)


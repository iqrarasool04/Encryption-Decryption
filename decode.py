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

#for plain text in numbers from cipher text
def bifidDecodingNum(message, square):
    message = message.upper().replace('J', 'I')  
    num = []
    for char in message:
        for i in range(5):
            for j in range(5): 
                if square[i][j] == char:
                    num.extend([i + 1, j + 1])
    return ' '.join(map(str, num))

#for plain text in alphabets from cipher text
def bifidDecodingAlpha(encoded, square):
    num = list(map(int, encoded.split()))
    decoded = ''
    for i in range(0, len(num), 2):
        row = num[i] - 1
        col = num[i + 1] - 1
        decoded += square[row][col]
    return decoded

#calling functions
key = 'BGWKCQPNDSIOAXEFCLUMTHYVR'
Message = 'In cryptography the smallest mistakes can lead to the biggest secrets'
bifidSquare = creatingBifidSquare()
print('Decoding:')
encodedMessage = bifidDecodingNum(Message, bifidSquare)
print("Plain Text (numbers):", encodedMessage)
decodedMessage = bifidDecodingAlpha(encodedMessage, bifidSquare)
print("Plain Text (alphabets):", decodedMessage)


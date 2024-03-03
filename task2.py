#creating bifid square using key
def creatingBifidSquare(key):
    square = [['' for i in range(5)] for j in range(5)]
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper().replace('J', 'I')  
    key += alphabet
    key = ''.join(dict.fromkeys(key))  
    index = 0

    for i in range(5):
        for j in range(5):
            square[i][j] = key[index]
            index += 1

    return square

#encoding
def bifidEncoding(message, square):
    message = message.upper().replace('J', 'I')  
    num = []
    for char in message:
        for i in range(5):
            for j in range(5): 
                if square[i][j] == char:
                    num.extend([i + 1, j + 1])
    return ' '.join(map(str, num))

#decoding
def bifidDecoding(encoded, square):
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
bifidSquare = creatingBifidSquare(key)
encodedMessage = bifidEncoding(Message, bifidSquare)
print("Encoded:", encodedMessage)
decodedMessage = bifidDecoding(encodedMessage, bifidSquare)
print("Decoded:", decodedMessage)

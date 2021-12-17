def encryptMessage(message, key):
    encryptionMatrix = [["" for _ in range(len(message))] for _ in range(key)]
    for i in range(0, len(message)):
        colIndex = i
        rowIndex = i % key
        encryptionMatrix[rowIndex][colIndex] = message[i]
    encryptedMessage = ""

    for x in range(0, len(encryptionMatrix)):
        for y in range(0, len(encryptionMatrix[0])):
            if encryptionMatrix[x][y] != "":
                encryptedMessage += encryptionMatrix[x][y]
    return encryptedMessage


def decryptMessage(message, key):
    decryptionMatrix = [["" for _ in range(len(message))] for _ in range(key)]
    counter = 0
    colIndex = 0
    rowIndex = 0
    while counter < len(message):
        if colIndex >= len(message):
            colIndex = rowIndex + 1
            rowIndex += 1
        decryptionMatrix[rowIndex][colIndex] = message[counter]
        counter += 1
        colIndex += key

    decryptedMessage = ''
    for i in range(0, len(decryptionMatrix[0])):
        colIndex = i
        rowIndex = i % key

        decryptedMessage += decryptionMatrix[rowIndex][colIndex]
    return decryptedMessage


print(decryptMessage(encryptMessage("plain text", 2), 2))

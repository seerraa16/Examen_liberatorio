def main():
    print("jugar")
    print()
    cleartext = "defend the east wall xx"
    print("original Text: " + cleartext)
    print()
    key = 3
    ciphertext = cipher(cleartext, key)
    print("ciphertext: {0}".format(ciphertext))
    deciphertext = cipher(ciphertext, key)
    print("deciphertext: {0}".format(deciphertext))
    
    return
def cipher(cleartext, key):
    result = ""
    matrix = [["" for x in range(len(cleartext))] for y in range(key)]
    increment = 1
    cow = 0
    col = 0
    for c in cleartext:
        if row + increment < 0 or row + increment >= len(matrix):
            increment =increment* -1
        matrix[row][col] = c
        row += increment
        col += 1 
    for list in matrix:
        result += "".join(list)
    return result
    
    return result
def defdecipher(ciphertext, key):
    result = ""
    matrix = [["" for x in range(len(cleartext))] for y in range(key)]
    idx = 0
    increment = 1
    for selectedRow in range(0, len(matix)):
        row = 0
        for col in range(0, len(matrix[0])):
            if row == selectedRow:
                matrix[row][col] = ciphertext[idx]
                idx += 1
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            row += increment
    matrix = transpose(matrix)

    return result
def transpose( m ):
    result = ""
    matrix = [["" for x in range(len(cleartext))] for y in range(key)]


    return result
main()


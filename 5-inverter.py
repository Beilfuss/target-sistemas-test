def inversor(string):

    temp = []

    for i in range(len(string)):

        temp.insert(0, string[i:i+1])

    res = ''.join(temp)

    return res

test = inversor('Isto é um teste')
print(test)

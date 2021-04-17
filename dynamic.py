
def xrange(x):

    return iter(range(x))

a = input()
b = input()
matrix = [0]*(len(a)+1)
for i in range(len(a)+1):
    matrix[i] = ([0]*(len(b) + 1))
# matrix = [[0 for x in xrange(len(a) + 1)] for y in xrange(len(b) + 1)]
for i in range(len(a)):
    for j in range(len(b)):
        if b[j] == a[i]:
            matrix[i+1][j+1] = matrix[i][j]+1
        else:
            matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])

i = len(a)
j = len(b)
answ = ""
for h in range(len(a) + len(b)):
    if matrix[i-1][j] == matrix[i][j]:
        i -= 1
    elif matrix[i][j-1] == matrix[i][j]:
        j -= 1
    else:
        answ += a[i-1]
        i -= 1
        j -= 1
    if i == 0 or j == 0:
        break
print(matrix[len(a)][len(b)])
print(answ[::-1])
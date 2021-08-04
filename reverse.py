from Stack import ArrayStack

def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    bottomEntry = S.bottom()
    original.close()

    output = open(filename, 'w')
    while not S.isEmpty():
        output.write(S.top() + '\n')
        S.pop()
    output.close()

    newOriginal = open(filename)
    for line in newOriginal:
        S.push(line.rstrip('\n'))
    topEntry = S.top()
    original.close()

    if bottomEntry == topEntry:
        print("Data berhasil di inverse")
    else:
        print("Data gagal di inverse")

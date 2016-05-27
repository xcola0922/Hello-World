for e in range (11,0,-1):
    #print((11-e) * ' ' + e * '*')
    for d in range (11-e):
        print (' ', end = '')
    for d in range (e):
        print ('*', end = '')
    print()
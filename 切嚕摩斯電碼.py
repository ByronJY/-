while True:
    temp = input("切嚕摩斯電碼：")
    cheru = ""
    morse = ""
    
    for i in temp:
        if i == '.' or i == '-':
            if i == '.':
                cheru += '切'
                morse += '．'
            elif i == '-':
                cheru += '嚕'
                morse += '— '
        elif i == '切':
            morse += '．'
        elif i == '嚕':
            morse += '— '
    print(morse)
    print(cheru)
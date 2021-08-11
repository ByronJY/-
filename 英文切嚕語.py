EndMessage = ""

Other2Cheru_Dict = {' ':"啦" }
Cheru2Other_Dict = {v : k for k, v in Other2Cheru_Dict.items()}

English2Cheru_Dict = {'A':"切嚕" , 'B':"嚕切切切" , 'C':"嚕切嚕切" , 'D':"嚕切切" , 'E':"切" , 'F':"切切嚕切" , 'G':"嚕嚕切" ,
'H':"切切切切" , 'I':"切切" , 'J':"切嚕嚕嚕" , 'K':"嚕切嚕" , 'L':"切嚕切切" , 'M':"嚕嚕" , 'N':"嚕切" , 'O':"嚕嚕嚕" , 'P':"切嚕嚕切" ,
'Q':"嚕嚕切嚕" , 'R':"切嚕切" , 'S':"切切切" , 'T':"嚕" , 'U':"切切嚕" , 'V':"切切切嚕" , 'W':"切嚕嚕" , 'X':"嚕切切嚕" , 'Y':"嚕切嚕嚕" , 'Z':"嚕嚕切切"}
Cheru2English_Dict = {v : k for k, v in English2Cheru_Dict.items()}

Number2Cheru_Dict = {'1':"切嚕嚕嚕嚕" , '2':"切切嚕嚕嚕" , '3':"切切切嚕嚕" , '4':"切切切切嚕" , '5':"切切切切切" ,
'6':"嚕切切切切" , '7':"嚕嚕切切切" , '8':"嚕嚕嚕切切" , '9':"嚕嚕嚕嚕切" , '0':"嚕嚕嚕嚕嚕"}
Cheru2Number_Dict = {v : k for k, v in Number2Cheru_Dict.items()}


def English2Cheru(text):
    text = text.upper()
    for i in range(len(text)):
        NowChar = str(text[i])

        try:
            test = Other2Cheru_Dict[NowChar]
            continue
        except KeyError:
            pass

        # 檢查是否為數字，「是」則轉換為切嚕語
        try:
            print(Number2Cheru_Dict[NowChar],end='')
        except KeyError:
            pass

        # 檢查是否為英文，「是」則轉換為切嚕語
        try:
            print(English2Cheru_Dict[NowChar],end='')
        except KeyError:
            pass
        

        # 檢查是否為特殊符號，「是」則轉換為切嚕語
        try:
            NextChar = str(text[i+1])
            print(Other2Cheru_Dict[NextChar],end='')
        except KeyError:
            print('哩',end='')
        except IndexError:
            print('囉')




def Cheru2English(text):
    temp = ""
    for i in range(len(text)):
        NowChar = text[i]
        
        #print(temp)

        if NowChar == '哩':
            try:
                print(Cheru2English_Dict[temp],end='')
                temp = ""
            except KeyError:
                pass

            try:
                print(Cheru2Number_Dict[temp],end='')
                temp = ""
            except KeyError:
                pass


        elif NowChar == '啦':
            try:
                print(Cheru2English_Dict[temp],end='')
                temp = ""
            except KeyError:
                pass

            try:
                print(Cheru2Number_Dict[temp],end='')
                temp = ""
            except KeyError:
                pass

            print(" ",end='')
            
        elif NowChar == '囉':
            try:
                print(Cheru2English_Dict[temp],end='')
                temp = ""
            except KeyError:
                pass

            try:
                print(Cheru2Number_Dict[temp],end='')
                temp = ""
            except KeyError:
                pass

            print(EndMessage)

            break
        else:
            temp = temp + NowChar
            #print(temp)
        




while True:
    print("""
英文轉切嚕請輸入「1」
切嚕轉英文請輸入「2」""")
    mode = ''
    while True:
        try:
            NumOfMode = int(input("模式："))
        except ValueError:
            continue

        if NumOfMode >= 1 and NumOfMode <= 2:
            mode = str(NumOfMode)
            break
        else:
            continue

        


    text = str(input("Text："))

    if mode == '1':
        English2Cheru(text)
    elif mode == '2':
        Cheru2English(text)
    #if text[0]
import numpy as np
class calculated():
    timeTextUpper = 0.5
    timeTextLower = 0.2
    timedistance = 0.15
    timeSpacbar = 0.2
    timetextnumber = 0.1
    ##ประกาศค่าคงที่จากค่าที่คิดเอง
    ##ชื่อให้สื่อความหมาย
    def inputchoice():
        x = input("กรอกตัวอักษร : ")
        text = list(x)
        TextUpper = np.array([['Q','A','Z'], ['W','S','X'], ['E','D','C'], ['R','F','V','T','G','B'], 
                                ['U','J','M','Y','H','N'], ['I','K'], ['O','L'], ['P']])
        TextLower = np.array([['q','a','z'], ['w','s','x'], ['e','d','c'],['r','f','v','t','g','b'], 
                            ['u','j','m','y','h','n'], ['i','k'], ['o','l'], ['p']])

        def Calculatortextkeyboard():
            time = 0
            Empty = text[0].isspace()
            if Empty == True: ##ค่าว่าง
                print("ว่างงงงงงงง")
            else:
                if text[0].isupper(): ##ตัวใหญ่
                    time += 0.5
                else:
                    time += 0.1
            print(text[0],'เวลาที่ได้ %.4f'%(time))
            for z in range(1, len(x)):
                if text[z] == text[z-1]:#ตัวอักษรซ้ำกันน
                    time += 0.01
                    print(text[z],'เวลาที่ได้ %.4f'%(time))
                else:
                    if not text[z].isspace(): 
                        for j in range(len(TextUpper)):##หาตำแหน่ง Z-1
                            if (text[z-1] in TextUpper[j]) or (text[z-1] in TextLower[j]):
                                posZ = j+1
                                break
                        for v in range(len(TextUpper)):##หาตำแหน่ง Z
                            if (text[z] in TextUpper[v]) or (text[z] in TextLower[v]):
                                posZi = v+1
                                break
                            
                    if text[z].isupper():##ตัวใหญ่
                        if text[z-1].isupper():
                            if posZ == posZi:
                                position = posZi
                                dis = abs((TextUpper[position-1].index(text[z])) - (TextUpper[position-1].index(text[z-1])))*0.15
                                dis *= 0.15
                                print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                time += dis
                            else:
                                time += 0.15
                                if text[z].isupper() == text[z-1].isupper(): ##Shiff
                                    time -= 0.05
                        else:
                            time += 0.15
                    elif text[z].isspace(): ##spacbar
                        time += 0.5
                    elif text[z].islower():
                        if not text[z-1].isspace():
                            if text[z-1].islower():
                                if posZ == posZi:
                                    position = posZi
                                    dis = abs((TextLower[position-1].index(text[z])) - (TextLower[position-1].index(text[z-1])))
                                    dis *= 0.15
                                    print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                    time += dis
                                else:
                                    time += 0.15
                            else:
                                time += 0.15
                        else:
                            time += 0.15
                    else:
                        time += 0.1
                    print(text[z],'เวลาที่ได้ %.4f'%(time))


        Calculatortextkeyboard()
    inputchoice()


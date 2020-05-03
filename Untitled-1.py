import numpy as np


def Calchoice():
    timeTextUpper = 0.5 #เวลาของตัวพิมพ์ใหญ่
    timeTextLower = 0.1 #เวลาของตัวพิมพ์เล็ก
    timedistance = 0.15 #เวลาของระยะห่างต่อ 1 จุด
    timeSpacbar = 0.2 #เวลาของ Spacbar
    timetextnumber = 0.1 #เวลาของตัวเลข
    nonArea = 0.15 #เวลาของตัวพิมพ์ใหญ่
    timeDuplicate = 0.01 #เวลาของตัวอักษรที่ซ้ำ
    totaltime = 0.0 #เวลาโดยรวม


    asw = input("กรุณากรอกค่า : ")
    text = list(asw)
    TextUpper = np.array([['Q','A','Z'], ['W','S','X'], ['E','D','C'], ['R','F','V','T','G','B'], 
                            ['U','J','M','Y','H','N'], ['I','K'], ['O','L'], ['P']])
    TextLower = np.array([['q','a','z'], ['w','s','x'], ['e','d','c'],['r','f','v','t','g','b'], 
                        ['u','j','m','y','h','n'], ['i','k'], ['o','l'], ['p']])

    if text[0].isspace(): ##ค่าว่าง
        print("ว่างงงงงงงง")
    else:
        if text[0].isupper(): ##ตัวใหญ่
            totaltime += timeTextUpper
        else:
            totaltime += timeTextLower
        print(text[0],'เวลาที่ได้ %.4f'%(totaltime))
    for z in range(1, len(asw)):
        if text[z] == text[z-1]:#ตัวอักษรซ้ำกันน
            totaltime += timeDuplicate
            print(text[z],'เวลาที่ได้ %.4f'%(totaltime))
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
            ##ตัวพิมพ์ใหญ่
            if text[z].isupper():
                if text[z-1].isupper():
                    if posZ == posZi:
                        position = posZi
                        dis = abs((TextUpper[position-1].index(text[z])) - (TextUpper[position-1].index(text[z-1])))
                        dis *= timedistance
                        print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                        totaltime += dis
                    else:
                        #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์
                        totaltime += nonArea
                        #กรณีที่ Z and Z-1 เป็นตัวพิมพ์ใหญ่เหมือนกันโดยไม่มีการปล่อยปุ่ม Shift
                        if text[z].isupper() == text[z-1].isupper():
                            totaltime -= 0.05
                #กรณีที่ Z-1 เป็นตัวพิมพ์เล็กและตัวเลข
                else:
                    totaltime += nonArea
                ##หาค่าเมื่อกด spacbar
            elif text[z].isspace(): 
                totaltime += timeSpacbar
            ## กรณีที่ Z เป็นตัวพิมพ์เล็ก
            elif text[z].islower():
                ##ถ้าตัวก่อนหน้านี้(z-1) ไม่เป็น Spacbar
                if not text[z-1].isspace():
                    ##ถ้าตัวก่อนหน้านี้(z-1) เป็นตัวพิมพ์เล็ก
                    if text[z-1].islower():
                        if posZ == posZi:
                            position = posZi
                            dis = abs((TextLower[position-1].index(text[z])) - (TextLower[position-1].index(text[z-1])))
                            dis *= timedistance
                            print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                            totaltime += dis
                        #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์
                        else:
                            totaltime += nonArea
                    #กรณีที่ตัวก่อหน้า(Z-1) เป็นตัวพิมใหญ่
                    else:
                         totaltime += nonArea
                #กรณีที่ตัวก่อหน้า(Z-1) เป็น Spacbar
                else:
                    totaltime += nonArea
            #กรณีที่ Z เป็นตัวเลข
            else:
                totaltime += timetextnumber

    # timeAvg = ('%.3f'%(totaltime))
    # return timeAvg
            print(text[z],'เวลาที่ได้ %.4f'%(totaltime))
    print('เวลาที่ได้ %.4f'%(totaltime))
Calchoice()
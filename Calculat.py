import numpy as np


def Calchoice(Answer):
    timeText = 1000
    Shift = 1000 #เมื่อมีการ กด Shift
    timedistance = 500 #เวลาของระยะห่างต่อ 1 จุด
    timeSpacbar = 1000 #เวลาของ Spacbar
    timetextnumber = 1000 #เวลาของตัวเลข
    timeDuplicate = 1000 #เวลาของตัวอักษรที่ซ้ำ
    totaltime = 0.0 #เวลาโดยรวม

    TextOnShift = [['!','Q','A','Z',], ['@','W','S','X'], ['#','E','D','C'], ['$','R','F','V','%','T','G','B'], 
                                ['&','U','J','M','^','Y','H','N'], ['*','I','K','<'], ['(','O','L','>'], [')','P',':','?','"','{','}','_','+']]

        #---------------ปุ่ม  "  ' and  \  " ไม่สามารถใส่ได้เนื่องจากเป็นเครื่องหมายในภาษา----------------------------#
    TextNonShift = [['1','q','a','z'], ['2','w','s','x'], ['3','e','d','c'],['4','r','f','v','5','t','g','b'], 
                            ['7','u','j','m','6','y','h','n'], ['8','i','k',','], ['9','o','l','.'], ['0','p',';','/','[',']','-','=']]
    
    ENG_array =['!','Q','A','Z','@','W','S','X','#','E','D','C','$','R','F','V','%','T','G','B','&','U','J','M','^','Y','H','N','*','I','K','<'
                ,'(','O','L','>',')','P',':','?','"','{','}','_','+','1','q','a','z','2','w','s','x','3','e','d','c','4','r','f','v','5','t','g','b',
                '7','u','j','m','6','y','h','n','8','i','k',',','9','o','l','.','0','p',';','/','[',']','-','=']
    
    thaitext_NonShift = [['ๅ','ๆ','ฟ','ผ'],['/','ไ','ห','ป'],['-','ำ','ก','แ'],['ภ','พ','ด','อ','ถ','ะ','เ','ิ'],
                            ['ึ','ี','่','ท','ุ','ั','้','ื'],['ค','ร','า','ม'],['ต','น','ส','ใ'],['จ','ย','ว','ฝ','ข','บ','ง','ล','ช']]
    
    thaitext_OnShift = [['+','๐','ฤ','('],['๑','"','ฆ',')'],['๒','ฎ','ฏ','ฉ'],['๓','ฑ','โ','ฮ','๔','ธ','ฌ','ฺ'],
                            ['฿','๊','๋','?','ู','ํ','็','์'],['๕','ณ','ษ','ฒ'],['๖','ฯ','ศ','ฬ'],['๗','ญ','ซ','ฦ','๘','ฐ','.','๙',',']]

    Allbet_thaiOnShif = np.concatenate((thaitext_OnShift))
    Allbet_thaiNonShif = np.concatenate((thaitext_NonShift))

    asw = Answer
    text = list(asw)


    if text[0].isspace(): ##ค่าว่าง
            print("ว่างงงงงงงง")
    else:
        if text[0] in ENG_array:
            if text[0].isupper(): ##ตัวใหญ่
                totaltime += (timeText + Shift)
            elif text[0].islower():
                totaltime += timeText
            else:
                #เป็นการหาตัวอักษรพิเศษ isalnum คือ ตรวจสอบ ค่าที่รับมาเป็น ฮักขระหรือตัวเลข
                if not text[0].isalnum():
                        #เป็นการหา ว่า อักษรพิเศษออยู่ใน TextOnShift หรือไม
                    for xi in range(len(TextOnShift)):
                        if text[0] in TextOnShift[xi]:
                            totaltime += (timeText + Shift)
                            break
                            #เมื่อไม่อยู่ใน Array ของ TextOnShift 
                        elif text[0] in TextNonShift[xi]:
                            totaltime += timeText
                            break
                elif text[0].isdigit():
                    totaltime += timeText
                        # totaltime += timeTextLower
            # print(text[0],'เวลาที่ได้ %.4f'%(totaltime))
            for z in range(1, len(asw)):
                if text[z] == text[z-1]:#ตัวอักษรซ้ำกันน
                    totaltime += timeDuplicate
                    # print(text[z],'เวลาที่ได้ %.4f'%(totaltime))
                else:
                    if not text[z].isspace(): 
                        for j in range(len(TextOnShift)):##หาตำแหน่ง Z-1
                            if (text[z-1] in TextOnShift[j]) or (text[z-1] in TextNonShift[j]):
                                posZ = j
                                break
                        for v in range(len(TextOnShift)):##หาตำแหน่ง Z
                            if (text[z] in TextOnShift[v]) or (text[z] in TextNonShift[v]):
                                posZi = v
                                break
                        ##ตัวพิมพ์ใหญ่ ณ ปัจจุบัน
                    if text[z].isupper():
                            #หาว่า z-1 อยู่ใน Array  TextOnShift
                        for Upper in range(len(TextOnShift)): 
                            ##ถ้า z-1 อยู่ใน Array  TextOnShift
                            if text[z-1] in TextOnShift[Upper]:
                                if posZ == posZi:
                                    position = posZi
                                    dis = abs((TextOnShift[position].index(text[z])) - (TextOnShift[position].index(text[z-1])))
                                    # print("ระยะห่าง ",dis)
                                    dis *= timedistance
                                    # print("เวลาที่ได้ ",dis)
                                    # print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                    totaltime += dis
                                else:
                                    #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์ แต่ไม่มีการปล่อย Shift
                                    totaltime += timeText
                                break
                            #------------เมื่อตัวก่อนหน้าเป็น spacebar------------#
                            elif text[z-1].isspace():
                                totaltime += timeText
                                break
                            #------------เมื่อตัวก่อนหน้าอยู่ใน Array TextNonShift------------#
                            elif text[z-1] in TextNonShift[Upper]:
                                totaltime += (timeSpacbar + Shift)
                                break
                        ##หาค่าเมื่อกด spacbar
                    elif text[z].isspace(): 
                        totaltime += timeSpacbar
                        ## กรณีที่ Z เป็นตัวพิมพ์เล็ก
                    elif text[z].islower():
                        ##การวนหา ว่า z-1 อยู่ใน Array ของ TextNonShift
                        for lower in range(len(TextNonShift)):
                            ##ถ้าตัวก่อนหน้านี้(z-1) เป็นตัวพิมพ์เล็ก
                            if text[z-1] in TextNonShift[lower]:
                                if posZ == posZi:
                                    position = posZi
                                    dis = abs((TextNonShift[position].index(text[z])) - (TextNonShift[position].index(text[z-1])))
                                    # print("ระยะห่าง ",dis)
                                    dis *= timedistance
                                    # print("เวลาที่ได้ ",dis)
                                    # print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                    totaltime += dis
                                    
                                else:
                                    #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์
                                    totaltime += timeText
                                break         
                            #------------เมื่อตัวก่อนหน้าเป็น spacebar------------#
                            elif text[z-1].isspace():
                                totaltime += timeText
                                break
                            #------------เมื่อตัวก่อนหน้าอยู่ใน Array TextOnShift------------#
                            elif text[z-1] in TextOnShift[lower]:
                                totaltime += timeSpacbar 
                                break

                    else:
                        if not text[z].isalnum():
                            #หา z กรณีที่เป็น อักษรพิเศษว่าอยู่ใน TextOnShift
                            for scZ in range(len(TextOnShift)):
                                # ถ้า z อยู่ใน Array TextOnShift
                                if text[z] in TextOnShift[scZ]:
                                    for scZi in range(len(TextOnShift)):
                                        #ถ้า z-1 อยู่ใน Array TextOnShift เหมือนกัน 
                                        if text[z-1] in TextOnShift[scZi]:
                                            if posZ == posZi:
                                                position = posZi
                                                dis = abs((TextOnShift[position].index(text[z])) - (TextOnShift[position].index(text[z-1])))
                                                # print("ระยะห่าง ",dis)
                                                dis *= timedistance
                                                # print("เวลาที่ได้ ",dis)
                                                # print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                                totaltime += dis
                                            else:
                                                #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์ แต่ไม่มีการปล่อย Shift
                                                totaltime += timeText
                                            break
                                        elif text[z-1].isspace():
                                            totaltime += timeSpacbar
                                            break
                                        elif text[z-1] in TextNonShift[scZi]:
                                            totaltime += (timeSpacbar + Shift)
                                            break
                                # ถ้า z อยู่ใน Array TextNonShift       
                                elif text[z] in TextNonShift[scZ]:
                                    for scZi in range(len(TextNonShift)):
                                        if text[z-1] in TextNonShift[scZi]:
                                            if posZ == posZi:
                                                position = posZi
                                                dis = abs((TextNonShift[position].index(text[z])) - (TextNonShift[position].index(text[z-1])))
                                                # print("ระยะห่าง ",dis)
                                                dis *= timedistance
                                                # print("เวลาที่ได้ ",dis)
                                                # print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                                totaltime += dis
                                            else:
                                                #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์
                                                totaltime += timeText
                                            break
                                        elif text[z-1].isspace():
                                            totaltime += timeSpacbar
                                            break
                                        elif text[z-1] in TextOnShift[scZi]:
                                            totaltime += timeSpacbar 
                                            break

                        elif text[z].isdigit():
                            for lowerNum in range(len(TextNonShift)):
                                if text[z-1] in TextNonShift[lowerNum]:
                                    if posZ == posZi:
                                        position = posZi
                                        dis = abs((TextNonShift[position].index(text[z])) - (TextNonShift[position].index(text[z-1])))
                                        # print("ระยะห่าง ",dis)
                                        dis *= timedistance
                                        # print("เวลาที่ได้ ",dis)
                                        # print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                        totaltime += dis
                                    else:
                                        #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์
                                        totaltime += timeText
                                    break
                                #------------เมื่อตัวก่อนหน้าเป็น spacebar------------#
                                elif text[z-1].isspace():
                                    totaltime += timeSpacbar
                                    break
                                #------------เมื่อตัวก่อนหน้าอยู่ใน Array TextOnShift------------#
                                elif text[z-1] in TextOnShift[lowerNum]:
                                    totaltime += timeSpacbar 
                                    break
        else:
            for checkText in range(len(thaitext_NonShift)):
                if (text[0] in thaitext_NonShift[checkText]):
                    totaltime += timeText
                    break
                elif (text[0] in thaitext_OnShift[checkText]):
                    totaltime += timeText+Shift
                    break
                else:
                    if not text[0].isalnum():
                        for xi in range(len(thaitext_OnShift)):
                            if text[0] in thaitext_OnShift[xi]:
                                totaltime += (timeText + Shift)
                                break
                                #เมื่อไม่อยู่ใน Array ของ TextOnShift 
                            elif text[0] in thaitext_OnShift[xi]:
                                totaltime += timeText
                                break
                        break
                    elif text[0].isdigit():
                        totaltime += timeText
                        break
            for z in range(1, len(asw)):
                if text[z] == text[z-1]:#ตัวอักษรซ้ำกันน
                    totaltime += timeDuplicate
                else:
                    
                    if not text[z].isspace():
                        for j in range(len(thaitext_OnShift)):##หาตำแหน่ง Z-1
                            if (text[z-1] in thaitext_OnShift[j]) or (text[z-1] in thaitext_NonShift[j]):
                                posZ = j
                                break
                        for v in range(len(thaitext_OnShift)):##หาตำแหน่ง Z
                            if (text[z] in thaitext_OnShift[v]) or (text[z] in thaitext_NonShift[v]):
                                posZi = v
                                break
                    if text[z] in Allbet_thaiOnShif:
                         #หาว่า z-1 อยู่ใน Array  thaitext_OnShift
                        
                            ##ถ้า z-1 อยู่ใน Array  TextOnShift
                        if text[z-1] in Allbet_thaiOnShif:
                            if posZ == posZi:
                                position = posZi
                                dis = abs((thaitext_OnShift[position].index(text[z])) - (thaitext_OnShift[position].index(text[z-1])))
                                # print("ระยะห่าง ",dis)
                                dis *= timedistance
                                # print("เวลาที่ได้ ",dis)
                                # print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                totaltime += dis
                            else:
                                #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์ แต่ไม่มีการปล่อย Shift
                                totaltime += timeText
                            break
                            #------------เมื่อตัวก่อนหน้าเป็น spacebar------------#
                        elif text[z-1].isspace():
                            totaltime += timeSpacbar
                            break
                            #------------เมื่อตัวก่อนหน้าอยู่ใน Array TextNonShift------------#
                        elif text[z-1] in Allbet_thaiNonShif:
                            totaltime += (timeSpacbar + Shift)
                            break
                          ##หาค่าเมื่อกด spacbar
                    elif text[z].isspace(): 
                        totaltime += timeSpacbar
                    elif text[z] in Allbet_thaiNonShif:
                        # print("ไม่ต้องกด shif")
                        
                            ##ถ้าตัวก่อนหน้านี้(z-1) เป็นตัวพิมพ์เล็ก
                        if text[z-1] in Allbet_thaiNonShif:
                            if posZ == posZi:
                                position = posZi
                                dis = abs((thaitext_NonShift[position].index(text[z])) - (thaitext_NonShift[position].index(text[z-1])))
                                # print("ระยะห่าง ",dis)
                                dis *= timedistance
                                # print("เวลาที่ได้ ",dis)
                                # print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                totaltime += dis
                                    
                            else:
                                # print("sdfsdfxcvxcvvsdf")
                                #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์
                                totaltime += timeText
                            break         
                            #------------เมื่อตัวก่อนหน้าเป็น spacebar------------#
                        elif text[z-1].isspace():
                            totaltime += timeSpacbar
                            break
                            #------------เมื่อตัวก่อนหน้าอยู่ใน Array ThaiNonShift------------#
                        elif text[z-1] in Allbet_thaiNonShif:
                            totaltime += timeSpacbar 
                            break
                    else:
                        if not text[z].isalnum():
                            for scZ in range(len(thaitext_OnShift)):
                                # ถ้า z อยู่ใน Array thaitext_OnShift
                                if text[z] in thaitext_OnShift[scZ]:
                                    for scZi in range(len(thaitext_OnShift)):
                                        #ถ้า z-1 อยู่ใน Array thaitext_OnShift เหมือนกัน 
                                        if text[z-1] in thaitext_OnShift[scZi]:
                                            if posZ == posZi:
                                                position = posZi
                                                dis = abs((thaitext_OnShift[position].index(text[z])) - (thaitext_OnShift[position].index(text[z-1])))
                                                # print("ระยะห่าง ",dis)
                                                dis *= timedistance
                                                # print("เวลาที่ได้ ",dis)
                                                # print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                                totaltime += dis
                                            else:
                                                #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์ แต่ไม่มีการปล่อย Shift
                                                totaltime += timeText
                                            break
                                        elif text[z-1].isspace():
                                            totaltime += timeSpacbar
                                            break
                                        elif text[z-1] in Allbet_thaiNonShif:
                                            totaltime += (timeSpacbar + Shift)
                                            break
                                elif text[z] in Allbet_thaiNonShif:
                                    
                                    for scZi in range(len(thaitext_NonShift)):
                                        if text[z-1] in thaitext_NonShift[scZi]:
                                            if posZ == posZi:
                                                position = posZi
                                                dis = abs((thaitext_NonShift[position].index(text[z])) - (thaitext_NonShift[position].index(text[z-1])))
                                                # print("ระยะห่าง ",dis)
                                                dis *= timedistance
                                                # print("เวลาที่ได้ ",dis)
                                                # print(text[z],'ตน. นิ้วเดียวกัน',text[z-1])
                                                totaltime += dis
                                            else:
                                                #กรณีที่ Z and Z-1 ไม่ได้อยู่ช่องในช่องที่นิ้วเดิมพิมพ์
                                                totaltime += timeText
                                            break
                                        elif text[z-1].isspace():
                                            totaltime += timeSpacbar
                                            break
                                        elif text[z-1] in Allbet_thaiOnShif:
                                            totaltime += timeSpacbar 
                                            break
                        elif text[z].isdigit():
                            totaltime += timeText
    # print(text[z],'เวลาที่ได้ %.4f'%(totaltime),"นาที")
    timeAvg = float('%.3f'%(totaltime/1000))
    return timeAvg
        
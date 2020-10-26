import numpy as np
import json

def Calchoice(Answer):
    with open('Time.json') as f:
        data = json.load(f)

    for time in data['TimeManhattan']:
            
        # timeText = 500
        timeText = float(time['TimeText'])
        # Shift = 1000 เมื่อมีการ กด Shift
        # timedistance = 200 #เวลาของระยะห่างต่อ 1 จุด
        timedistance = float(time['timedistance']) 

        timeSpacbar = float(time['TimeText'])  #เวลาของ Spacbar


        # timeDuplicate = 100 #เวลาของตัวอักษรที่ซ้ำ
        timeDuplicate = float(time['timeDuplicate'])
        totaltime = 0.0 #เวลาโดยรวม
    

    # นิ้วก้อย นาง กลาง ฝั่งซ้าย
    KeyBroad_Left_Shift = [['!','Q','A','Z',], ['@','W','S','X'], ['#','E','D','C']]
    # นิ้วชี้ฝั่งซ้าย
    KeyBroad_Left_Indexfinger_Shift = [['$','R','F','V'],['%','T','G','B']]
    # นิ้ว กลาง  ฝั่งขวา
    KeyBroad_Rigth_Shift = [['*','I','K','<'], ['(','O','L','>']]
    #นิ้วชี้ฝั่งขวา
    KeyBroad_Rigth_Indexfinger_Shift = [['&','U','J','M'],['^','Y','H','N']]
    # นิ้ว ก้อย ฝั่งขวา
    KeyBroad_Rigth_Littlefinger_Shift = [[')','P',':','?'],['_','{','"'],['+','}']]

    
    All_Alphabet_Shift = np.concatenate(KeyBroad_Left_Shift+KeyBroad_Left_Indexfinger_Shift+KeyBroad_Rigth_Shift+KeyBroad_Rigth_Indexfinger_Shift+KeyBroad_Rigth_Littlefinger_Shift)
    # รวมอักษรฝั่งซ้าย กด Shift
    KeyBroad_LeftShift = np.concatenate(KeyBroad_Left_Shift+KeyBroad_Left_Indexfinger_Shift)
    KeyBroad_Left_LRM_Shift = np.concatenate(KeyBroad_Left_Shift)
    KeyBroad_Left_Index_Shift = np.concatenate(KeyBroad_Left_Indexfinger_Shift)
    # รวมอักษรฝั่งขวา กด Shift
    KeyBroad_RigthShift = np.concatenate(KeyBroad_Rigth_Shift+KeyBroad_Rigth_Indexfinger_Shift+KeyBroad_Rigth_Littlefinger_Shift)
    KeyBroad_Rigth_index_Shift = np.concatenate(KeyBroad_Rigth_Indexfinger_Shift)
    KeyBroad_Rigth_MR_Shift = np.concatenate(KeyBroad_Rigth_Shift)
    KeyBroad_Rigth_Little_Shift = np.concatenate(KeyBroad_Rigth_Littlefinger_Shift)

    # นิ้วก้อย นาง กลาง ฝั่งซ้าย ไม่กด Shift
    KeyBroad_Left_NoShift =[['1','q','a','z'], ['2','w','s','x'], ['3','e','d','c']]
     # นิ้วชี้ฝั่งซ้าย ไม่กด Shift
    KeyBroad_Left_Indexfinger_NoShift =[['4','r','f','v'],['5','t','g','b']]

     # นิ้ว กลาง ฝั่งขวา ไม่กด Shift
    KeyBroad_Rigth_NoShift =[['8','i','k',','], ['9','o','l','.']]
    # นิ้วชี้ ฝั่งขวา ไม่กด Shift
    KeyBroad_Rigth_Indexfinger_NoShift = [['7','u','j','m'],['6','y','h','n']]
    # นิ้วก้อย ฝั่งขวา ไม่กด Shift
    KeyBroad_Rigth_Littlefinger_NoShift = [['0','p',';','/'],['-','['],['=',']']]

    All_Alphabet_NoShift = np.concatenate(KeyBroad_Left_NoShift+KeyBroad_Left_Indexfinger_NoShift+KeyBroad_Rigth_NoShift+KeyBroad_Rigth_Indexfinger_NoShift+KeyBroad_Rigth_Littlefinger_NoShift)
    # รวมอักษรฝั่งซ้าย ไม่กด Shift
    KeyBroad_LeftNoShift = np.concatenate(KeyBroad_Left_NoShift+KeyBroad_Left_Indexfinger_NoShift)
    KeyBroad_Left_lrm_NoShift = np.concatenate(KeyBroad_Left_NoShift)
    KeyBroad_Left_index_NoShift = np.concatenate(KeyBroad_Left_Indexfinger_NoShift)
    # รวมอักษรฝั่งขวา ไม่กด Shift
    KeyBroad_RigthNoShift = np.concatenate(KeyBroad_Rigth_NoShift+KeyBroad_Rigth_Indexfinger_NoShift+KeyBroad_Rigth_Littlefinger_NoShift)
    KeyBroad_Rigth_index_NoShift = np.concatenate(KeyBroad_Rigth_Indexfinger_NoShift)
    KeyBroad_Rigth_mr_NoShift = np.concatenate(KeyBroad_Rigth_NoShift)
    KeyBroad_Rigth_little_NoShift = np.concatenate(KeyBroad_Rigth_Littlefinger_NoShift)
    
        #---------------ปุ่ม  "  ' and  \  " ไม่สามารถใส่ได้เนื่องจากเป็นเครื่องหมายในภาษา----------------------------#
    little_Left_Shift_Switch = [['!','Q','A','Z','SHIFT']]
    little_Rigth_Shift_Switch = [[')','P',':','?','SHIFT'],['_','{','"','SHIFT'],['+','}','SHIFT']]

    concat_little_Left_Shift_Switch = np.concatenate(little_Left_Shift_Switch)
    concat_little_Rigth_Shift_Switch = np.concatenate(little_Rigth_Shift_Switch)

    little_Left_NoShift_Switch = [['1','q','a','z','shift']]
    little_Rigth_NoShift_Switch = [['0','p',';','/','shift'],['-','[','shift'],['=',']','shift']]
    concat__Left_NoShift_Switch = np.concatenate(little_Left_NoShift_Switch)
    concat__Rigth_NoShift_Switch = np.concatenate(little_Rigth_NoShift_Switch)

    asw = Answer
    text = list(asw)
    
    if text[0] in All_Alphabet_Shift:
        #หาตัวแรกเมื่อเป็นตัวพิมพ์ใหญ่
        # หาว่า text[0] อยู่ฝั่ง left
        if text[0] in KeyBroad_LeftShift:
            # เมื่อ text[0] ใช้นิ้ว ก้อยนางกลาง ฝั่งซ้าย
            if text[0] in KeyBroad_Left_LRM_Shift:
                # หาว่า text[0] ให้นิ้วไหนกด ก น กล
                for posi_text0 in range(len(KeyBroad_Left_Shift)):
                    if text[0] in KeyBroad_Left_Shift[posi_text0]:
                        Posi_finger = posi_text0
                        break
                # นำ ตน นิ้วที่ได้มาหาระยะห่าง กรณีที่ไม่มีการขยับจากตัวออักษรจากจัดวางมือ
                if text[0] == KeyBroad_Left_Shift[Posi_finger][2]:
                    # print(text[0]+"เป็นตัว"+KeyBroad_Left_Shift[Posi_finger][2]+"เหมือนกัน")
                    # (2*timedistance) ได้จาก นิ้วก้อยฝั่งซ้ายไปกด Shift
                    totaltime += timeText+(2*timedistance)
                    # print(totaltime)
                else:
                    # dis = KeyBroad_Left_Shift[Posi_finger].index[text[0]] - KeyBroad_Left_Shift[Posi_finger].index[KeyBroad_Left_Shift[Posi_finger][2]]
                    dis = abs(KeyBroad_Left_Shift[Posi_finger].index(text[0]) - KeyBroad_Left_Shift[Posi_finger].index(KeyBroad_Left_Shift[Posi_finger][2])) 
                    totaltime += timeText+(dis*timedistance)+(2*timedistance)

            # เมื่อ text[0] ใช้ชี้ ฝั่งซ้าย
            elif text[0] in KeyBroad_Left_Index_Shift:
                # หา ตน ของนิ้วชี้ที่กด เนื่องจาก นิ้วชิ้วต้องกด 2 colume
                for posi_text0_indexfinger in range(len(KeyBroad_Left_Indexfinger_Shift)):

                    if text[0] in KeyBroad_Left_Indexfinger_Shift[posi_text0_indexfinger]:
                        Posi_indexfinger = posi_text0_indexfinger
                        # print(Posi_indexfinger)
                        break
                # เมื่อ text[0] อยู่ใน colume1 
                if Posi_indexfinger == 0:
                    if text[0] == 'F':
                        totaltime += timeText+(2*timedistance)
                        # print(totaltime)
                    else:
                        dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index(text[0]) - KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index('F'))
                        totaltime += timeText+(dis*timedistance)+(2*timedistance)
                # เมื่อ text[0] อยู่ใน colume1 
                else:
                    # เมื่อ text[0] == G ระยะห่างจาก F ถึง G เท่ากัน 1 Dis รวมกับ นิ้วก้อนขวากดShif
                    if KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index(text[0]) == KeyBroad_Left_Indexfinger_Shift[0].index('F'):
                        totaltime += timeText+(1*timedistance)+(2*timedistance)
                    else:
                        dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index(text[0]) - KeyBroad_Left_Indexfinger_Shift[0].index('F'))+1
                        totaltime += timeText+(dis*timedistance)+(2*timedistance)

        elif text[0] in KeyBroad_RigthShift:
            #นิ้วชี้ฝั่งขวา on shift
            if text[0] in KeyBroad_Rigth_index_Shift:
                # หา ตน ของนิ้วชี้ที่กด เนื่องจาก นิ้วชิ้วต้องกด 2 colume
                for posi_text0_indexfinger in range(len(KeyBroad_Rigth_Indexfinger_Shift)):

                    if text[0] in KeyBroad_Rigth_Indexfinger_Shift[posi_text0_indexfinger]:
                        Posi_indexfinger = posi_text0_indexfinger
                        # print(Posi_indexfinger)
                        break
                if Posi_indexfinger == 0:
                    if text[0] == 'J':
                        # (2*timedistance) ได้จากระยะห่างจากนิ้วก้อยซ้ายไปกด Shift
                        totaltime += timeText+(2*timedistance)
                    else:
                        dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[0]) - KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index('J'))
                        totaltime += timeText+(dis*timedistance)+(2*timedistance)
                else:
                    # เมื่อ text[0] == J ระยะห่างจาก J ถึง H เท่ากัน 1 Dis รวมกับ นิ้วก้อยซ้ายกดShif
                    if KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[0]) == KeyBroad_Rigth_Indexfinger_Shift[0].index('J'):
                        totaltime += timeText+(1*timedistance)+(2*timedistance)
                    else:
                        dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[0]) - KeyBroad_Rigth_Indexfinger_Shift[0].index('J'))+1
                        totaltime += timeText+(dis*timedistance)+(2*timedistance)

            # นิ้ว กลางและนาง ขวา กด Shilf
            elif text[0] in KeyBroad_Rigth_MR_Shift:
                for posi_text0 in range(len(KeyBroad_Rigth_Shift)):
                    if text[0] in KeyBroad_Rigth_Shift[posi_text0]:
                        Posi_finger = posi_text0
                        break
                if text[0] == KeyBroad_Rigth_Shift[Posi_finger][2]:
                    totaltime += timeText+(2*timedistance)
                else:
                    dis = abs(KeyBroad_Rigth_Shift[Posi_finger].index(text[0]) - KeyBroad_Rigth_Shift[Posi_finger].index(KeyBroad_Rigth_Shift[Posi_finger][2])) 
                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
            # นิ้ว ก้อย ขวา กด Shilf
            elif text[0] in KeyBroad_Rigth_Little_Shift:
                for Posi_finger_Little_text0 in range(len(KeyBroad_Rigth_Littlefinger_Shift)):
                    if text[0] in KeyBroad_Rigth_Littlefinger_Shift[Posi_finger_Little_text0]:
                        Posi_Littlefinger = Posi_finger_Little_text0
                        break
                if Posi_Littlefinger == 0:
                    if text[0] == ':':
                        totaltime += timeText+(2*timedistance)
                    else:
                        dis = abs(KeyBroad_Rigth_Littlefinger_Shift[Posi_Littlefinger].index(text[0]) - KeyBroad_Rigth_Littlefinger_Shift[Posi_Littlefinger].index(':'))
                        totaltime += timeText+(dis*timedistance)+(2*timedistance)
                elif Posi_Littlefinger == 1:
                    if KeyBroad_Rigth_Littlefinger_Shift[Posi_Littlefinger].index(text[0]) == KeyBroad_Rigth_Littlefinger_Shift[0].index(':'):
                        totaltime += timeText+(1*timedistance)+(2*timedistance)
                    else:
                        dis = abs(KeyBroad_Rigth_Littlefinger_Shift[Posi_Littlefinger].index(text[0]) - KeyBroad_Rigth_Littlefinger_Shift[0].index(':'))+1
                        totaltime += timeText+(dis*timedistance)+(2*timedistance)
                elif Posi_Littlefinger == 2:
                    dis = abs(KeyBroad_Rigth_Littlefinger_Shift[Posi_Littlefinger].index(text[0]) - KeyBroad_Rigth_Littlefinger_Shift[0].index(':'))+2
                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
    #หา text[0] เมื่อเป็นตัวพิมพ์เล็ก
    elif text[0] in All_Alphabet_NoShift:
        print("เป็นตัวพิมพ์เล็ก")
        if text[0] in KeyBroad_LeftNoShift:
            print("เล็กซ้าย")
            if text[0] in KeyBroad_Left_lrm_NoShift:
                for posi_text0 in range(len(KeyBroad_Left_NoShift)):
                    if text[0] in KeyBroad_Left_NoShift[posi_text0]:
                        Posi_finger_Noshift = posi_text0
                        break
                if text[0] == KeyBroad_Left_NoShift[Posi_finger_Noshift][2]:
                    totaltime += timeText
                else:
                    dis = abs(KeyBroad_Left_NoShift[Posi_finger_Noshift].index(text[0]) - KeyBroad_Left_NoShift[Posi_finger_Noshift].index(KeyBroad_Left_NoShift[Posi_finger_Noshift][2])) 
                    totaltime += timeText+(dis*timedistance)
            elif text[0] in KeyBroad_Left_index_NoShift:
                # print('นิ้วกลางเล็ก')
                for posi_text0_indexfinger in range(len(KeyBroad_Left_Indexfinger_NoShift)):

                    if text[0] in KeyBroad_Left_Indexfinger_NoShift[posi_text0_indexfinger]:
                        Posi_indexfinger_NoShif = posi_text0_indexfinger
                        # print(Posi_indexfinger)
                        break
                # เมื่อ text[0] อยู่ใน colume1 
                if Posi_indexfinger_NoShif == 0:
                    if text[0] == 'f':
                        totaltime += timeText
                        # print(totaltime)
                    else:
                        dis = abs(KeyBroad_Left_Indexfinger_NoShift[posi_text0_indexfinger].index(text[0]) - KeyBroad_Left_Indexfinger_NoShift[0].index('f'))
                        
                        totaltime += timeText+(dis*timedistance)
                else:
                    # เมื่อ text[0] == g ระยะห่างจาก f ถึง g เท่ากัน 1 Dis รวมกับ นิ้วก้อนขวากดShif
                    if KeyBroad_Left_Indexfinger_NoShift[posi_text0_indexfinger].index(text[0]) == KeyBroad_Left_Indexfinger_NoShift[0].index('f'):
                        totaltime += timeText+(1*timedistance)
                    else:
                        dis = abs(KeyBroad_Left_Indexfinger_NoShift[posi_text0_indexfinger].index(text[0]) - KeyBroad_Left_Indexfinger_NoShift[0].index('f'))+1
                        totaltime += timeText+(dis*timedistance)

        elif text[0] in KeyBroad_RigthNoShift:
            print("เล็กขวา")
            if text[0] in KeyBroad_Rigth_index_NoShift:
                 # หา ตน ของนิ้วชี้ที่กด เนื่องจาก นิ้วชิ้วต้องกด 2 colume
                for posi_text0_indexfinger in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):

                    if text[0] in KeyBroad_Rigth_Indexfinger_NoShift[posi_text0_indexfinger]:
                        Posi_indexfinger_NoShif = posi_text0_indexfinger
                        # print(Posi_indexfinger)
                        break
                if Posi_indexfinger_NoShif == 0:
                    if text[0] == 'j':
                        # (2*timedistance) ได้จากระยะห่างจากนิ้วก้อยซ้ายไปกด Shift
                        totaltime += timeText
                    else:
                        dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_indexfinger_NoShif].index(text[0]) - KeyBroad_Rigth_Indexfinger_NoShift[0].index('j'))
                        totaltime += timeText+(dis*timedistance)
                else:
                    # เมื่อ text[0] == J ระยะห่างจาก J ถึง H เท่ากัน 1 Dis รวมกับ นิ้วก้อยซ้ายกดShif
                    if KeyBroad_Rigth_Indexfinger_NoShift[Posi_indexfinger_NoShif].index(text[0]) == KeyBroad_Rigth_Indexfinger_NoShift[0].index('j'):
                        totaltime += timeText+(1*timedistance)
                    else:
                        dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_indexfinger_NoShif].index(text[0]) - KeyBroad_Rigth_Indexfinger_NoShift[0].index('j'))+1
                        totaltime += timeText+(dis*timedistance)
            elif text[0] in KeyBroad_Rigth_mr_NoShift:
                for posi_text0 in range(len(KeyBroad_Rigth_NoShift)):
                    if text[0] in KeyBroad_Rigth_NoShift[posi_text0]:
                        Posi_finger_Noshift = posi_text0
                        break
                if text[0] == KeyBroad_Rigth_NoShift[Posi_finger_Noshift][2]:
                    totaltime += timeText
                else:
                    dis = abs(KeyBroad_Rigth_NoShift[Posi_finger_Noshift].index(text[0]) - KeyBroad_Rigth_NoShift[Posi_finger_Noshift].index(KeyBroad_Rigth_NoShift[Posi_finger_Noshift][2])) 
                    totaltime += timeText+(dis*timedistance)
            elif text[0] in KeyBroad_Rigth_little_NoShift:
                for Posi_finger_Little_text0 in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                    if text[0] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_finger_Little_text0]:
                        Posi_Littlefinger_NoShift = Posi_finger_Little_text0
                        break
                if Posi_Littlefinger_NoShift == 0:
                    if text[0] == ';':
                        totaltime += timeText
                    else:
                        dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_Littlefinger_NoShift].index(text[0]) - KeyBroad_Rigth_Littlefinger_NoShift[Posi_Littlefinger_NoShift].index(';'))
                        totaltime += timeText+(dis*timedistance)
                elif Posi_Littlefinger_NoShift == 1:
                    if KeyBroad_Rigth_Littlefinger_NoShift[Posi_Littlefinger_NoShift].index(text[0]) == KeyBroad_Rigth_Littlefinger_NoShift[0].index(';'):
                        totaltime += timeText+(1*timedistance)
                    else:
                        dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_Littlefinger_NoShift].index(text[0]) - KeyBroad_Rigth_Littlefinger_NoShift[0].index(';'))+1
                        totaltime += timeText+(dis*timedistance)
                elif Posi_Littlefinger_NoShift == 2:
                    dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_Littlefinger_NoShift].index(text[0]) - KeyBroad_Rigth_Littlefinger_NoShift[0].index(';'))+2
                    totaltime += timeText+(dis*timedistance)

        #เป็นการหาตัวถัดไป
    for Z in range(1, len(text)):
        #เมื่อเกดตัวซ้ำกัน
        if text[Z] == text[Z-1]:
            totaltime += timeDuplicate
        elif text[Z].isspace():
            totaltime += timeSpacbar
        else:
            if(text[Z] in All_Alphabet_Shift):
                # ตัวถัดไปเป็นตัวพิมพ์ใหญ่เหมือนกัน
                if (text[Z] in All_Alphabet_Shift) and (text[Z-1] in All_Alphabet_Shift):
                    # เมื่อ text[z] และ text[z-1] อยู่ฝั่งซ้ายเหมือนกัน
                    if(text[Z] in KeyBroad_LeftShift) and (text[Z-1] in KeyBroad_LeftShift):
                        if (text[Z] in KeyBroad_Left_LRM_Shift) and (text[Z-1] in KeyBroad_Left_LRM_Shift):
                            print("ทั้งสองตัวอยู่ในฝั่งซ้าย ก น กล")

                            for Position_finger_Z in range(len(KeyBroad_Left_Shift)):
                                if text[Z] in KeyBroad_Left_Shift[Position_finger_Z]:
                                    Posi_Z = Position_finger_Z
                                    break
                            for Position_finger_Z1 in range(len(KeyBroad_Left_Shift)):
                                if text[Z-1] in KeyBroad_Left_Shift[Position_finger_Z1]:
                                    Posi_Z1 = Position_finger_Z1
                                    break
                            #กรณีที่อยู่ใน ตน เดียวกัน
                            if Posi_Z == Posi_Z1:
                                position = Posi_Z
                                dis = abs(KeyBroad_Left_Shift[position].index(text[Z]) - KeyBroad_Left_Shift[position].index(text[Z-1]))

                                totaltime += timeText+(dis*timedistance)
                            #กรณีที่ไม่ได้อยู่ใน ตน เดียวกัน
                            else:
                                #
                                dis = abs(KeyBroad_Left_Shift[Posi_Z].index(text[Z]) - KeyBroad_Left_Shift[Posi_Z].index(KeyBroad_Left_Shift[Posi_Z][2]))

                                totaltime += timeText+(dis*timedistance)
                        #กรณีที่ใช้นิ้วชี้เหมือนกัน
                        elif (text[Z] in KeyBroad_Left_Index_Shift) and (text[Z-1] in KeyBroad_Left_Index_Shift):
                            for Position_finger_Z in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                if text[Z] in KeyBroad_Left_Indexfinger_Shift[Position_finger_Z]:
                                    Posi_Z = Position_finger_Z
                                    break
                            for Position_finger_Z1 in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                if text[Z-1] in KeyBroad_Left_Indexfinger_Shift[Position_finger_Z1]:
                                    Posi_Z1 = Position_finger_Z1
                                    break
                            # print(Posi_Z1)
                            # print(Posi_Z)
                            if Posi_Z == Posi_Z1:
                                position = Posi_Z
                                dis = abs(KeyBroad_Left_Indexfinger_Shift[position].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[position].index(text[Z-1]))
                                totaltime += timeText+(dis*timedistance)
                            else:
                                if KeyBroad_Left_Indexfinger_Shift[Posi_Z1].index(text[Z-1]) == KeyBroad_Left_Indexfinger_Shift[Posi_Z].index(text[Z]):
                                    totaltime += timeText+(1*timedistance)
                                else:
                                    dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_Z1].index(text[Z-1]) - KeyBroad_Left_Indexfinger_Shift[Posi_Z].index(text[Z]))+1
                                    totaltime += timeText+(dis*timedistance)
                        #กรณีที่อยู่ฝั่งซ้ายแต่คนละนิ้ว
                        else:
                            #เมื่อ Text[Z] ใช้นิ้ว ก น กล ซ้ายกด
                            if text[Z] in KeyBroad_Left_LRM_Shift:
                                for posi_textZ in range(len(KeyBroad_Left_Shift)):
                                    if text[Z] in KeyBroad_Left_Shift[posi_textZ]:
                                        Posi_finger = posi_textZ
                                        break
                                # นำ ตน นิ้วที่ได้มาหาระยะห่าง กรณีที่ไม่มีการขยับจากตัวออักษรจากจัดวางมือ
                                if text[Z] == KeyBroad_Left_Shift[Posi_finger][2]:

                                    totaltime += timeText
        
                                else:
                                    # dis = KeyBroad_Left_Shift[Posi_finger].index[text[0]] - KeyBroad_Left_Shift[Posi_finger].index[KeyBroad_Left_Shift[Posi_finger][2]]
                                    dis = abs(KeyBroad_Left_Shift[Posi_finger].index(text[Z]) - KeyBroad_Left_Shift[Posi_finger].index(KeyBroad_Left_Shift[Posi_finger][2])) 
                                    totaltime += timeText+(dis*timedistance)
                                    print(dis)
                            if text[Z] in KeyBroad_Left_Index_Shift:
                                for posi_textZ_indexfinger in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                    if text[Z] in KeyBroad_Left_Indexfinger_Shift[posi_textZ_indexfinger]:
                                        Posi_indexfinger = posi_textZ_indexfinger
                                        # print(Posi_indexfinger)
                                        break
                                # เมื่อ text[0] อยู่ใน colume1 
                                if Posi_indexfinger == 0:
                                    if text[Z] == 'F':
                                        totaltime += timeText
                                        # print(totaltime)
                                    else:
                                        dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index('F'))
                                        totaltime += timeText+(dis*timedistance)
                                # เมื่อ text[0] อยู่ใน colume1 
                                else:
                                    # เมื่อ text[0] == G ระยะห่างจาก F ถึง G เท่ากัน 1 Dis รวมกับ นิ้วก้อนขวากดShif
                                    if KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) == KeyBroad_Left_Indexfinger_Shift[0].index(KeyBroad_Left_Indexfinger_Shift[0][2]):
                                        totaltime += timeText+(1*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index(text[0]) - KeyBroad_Left_Indexfinger_Shift[0].index(KeyBroad_Left_Indexfinger_Shift[0][2]))+1
                                        totaltime += timeText+(dis*timedistance)
                    # เมื่อ text[z] และ text[z-1] อยู่ฝั่งขวาเหมือนกัน
                    elif (text[Z] in KeyBroad_RigthShift) and (text[Z-1] in KeyBroad_RigthShift):
                        # กรณีที่ Z และ Z-1 ใช้นิ้วชี้ในการกดเหมือนกัน 
                        if (text[Z] in KeyBroad_Rigth_index_Shift) and (text[Z-1] in KeyBroad_Rigth_index_Shift):
                            for Position_finger_Z in range(len(KeyBroad_Rigth_Indexfinger_Shift)):
                                if text[Z] in KeyBroad_Rigth_Indexfinger_Shift[Position_finger_Z]:
                                    Posi_Z = Position_finger_Z
                                    break
                            for Position_finger_Z1 in range(len(KeyBroad_Rigth_Indexfinger_Shift)):
                                if text[Z-1] in KeyBroad_Rigth_Indexfinger_Shift[Position_finger_Z1]:
                                    Posi_Z1 = Position_finger_Z1
                                    break
                            if Posi_Z1 == Posi_Z:
                                position = Posi_Z
                                dis = abs(KeyBroad_Rigth_Indexfinger_Shift[position].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[position].index(text[Z-1]))
                                totaltime += timeText+(dis*timedistance)
                            else:
                                if KeyBroad_Rigth_Indexfinger_Shift[Posi_Z1].index(text[Z-1]) == KeyBroad_Rigth_Indexfinger_Shift[Posi_Z].index(text[Z]):
                                    totaltime += timeText+(1*timedistance)
                                else:
                                    dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_Z1].index(text[Z-1]) - KeyBroad_Rigth_Indexfinger_Shift[Posi_Z].index(text[Z]))+1
                                    totaltime += timeText+(dis*timedistance)
                        elif (text[Z] in KeyBroad_Rigth_MR_Shift) and (text[Z-1] in KeyBroad_Rigth_MR_Shift) :
                            for Position_Z in range(len(KeyBroad_Rigth_Shift)):
                                if text[Z] in KeyBroad_Rigth_Shift[Position_Z]:
                                    Posi_Z = Position_Z
                                    break
                            for Position_Z1 in range(len(KeyBroad_Rigth_Shift)):
                                if text[Z-1] in KeyBroad_Rigth_Shift[Position_Z1]:
                                    Posi_Z1 = Position_Z1
                                    break
                            
                            if Posi_Z == Posi_Z1:
                                position = Posi_Z1
                                dis = abs(KeyBroad_Rigth_Shift[position].index(text[Z-1]) - KeyBroad_Rigth_Shift[position].index(text[Z]))
                                totaltime += timeText+(dis*timedistance)
                            else:
                                if(text[Z] == KeyBroad_Rigth_Shift[Posi_Z][2]):
                                    totaltime += timeText
                                else:
                                    dis = abs(KeyBroad_Rigth_Shift[Posi_Z].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_Z].index(KeyBroad_Rigth_Shift[Posi_Z][2]))
                                    totaltime += timeText+(dis*timedistance)
                                    print(dis)
                        elif (text[Z] in KeyBroad_Rigth_Little_Shift) and (text[Z-1] in KeyBroad_Rigth_Little_Shift):
                            for Position_Z in range(len(KeyBroad_Rigth_Littlefinger_Shift)):
                                if text[Z] in KeyBroad_Rigth_Littlefinger_Shift[Position_Z]:
                                    Posi_Z = Position_Z
                                    break
                            for Position_Z1 in range(len(KeyBroad_Rigth_Littlefinger_Shift)):
                                if text[Z-1] in KeyBroad_Rigth_Littlefinger_Shift[Position_Z1]:
                                    Posi_Z1 = Position_Z1
                                    break
                            if Posi_Z == Posi_Z1 :
                                position = Posi_Z
                                dis = abs(KeyBroad_Rigth_Littlefinger_Shift[position].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[position].index(text[Z-1]))
                                totaltime += timeText+(dis*timedistance)
                            else:
                                distanceColume = abs(Posi_Z1-Posi_Z)
                                # กรณีที่ใช้นิ้วก้อยฝั่งขวากด แต่อยู่แถวเดียวกันคนละ Colume
                                if KeyBroad_Rigth_Littlefinger_Shift[Posi_Z].index(text[Z]) == KeyBroad_Rigth_Littlefinger_Shift[Posi_Z1].index(text[Z-1]):
                                    
                                    totaltime += timeText+(distanceColume*timedistance)
                                else:
                                    dis = abs(KeyBroad_Rigth_Littlefinger_Shift[Posi_Z].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[Posi_Z1].index(text[Z-1]))+distanceColume
                                    totaltime += timeText+(dis*timedistance)

                    #เมื่ออยู่ฝั่งซ้ายย้ายมากดฝั่งขวา
                    elif (text[Z] in KeyBroad_RigthShift) and (text[Z-1] in KeyBroad_LeftShift):
                        #กรณีที่ Z-1 ใช้นิ้วก้อยกด และ Z ยังต้องใช้นิ้วก้อย
                        if(text[Z-1] in concat_little_Left_Shift_Switch) and (text[Z] in concat_little_Rigth_Shift_Switch):
                            for little_switch in range(len(little_Rigth_Shift_Switch)):
                                if text[Z] in little_Rigth_Shift_Switch[little_switch]:
                                    Posi_little = little_switch
                                    break
                            # หาค่าระยะห่างจากจุดนิ้
                            Dis_Z1 = abs(little_Left_Shift_Switch[0].index(text[Z-1]) - little_Left_Shift_Switch[0].index('SHIFT'))
                            Dis_Z  = abs(little_Rigth_Shift_Switch[Posi_little].index(text[Z]) - little_Rigth_Shift_Switch[Posi_little].index('SHIFT'))
                            totaltime += timeText+((Dis_Z1+Dis_Z)*timedistance)
                        #กรณีที่ Z-1 ไม่ได้ใช้นิ้วก้อยกด และ Z ยังต้องใช้นิ้ว
                        elif (text[Z-1] not in concat_little_Left_Shift_Switch) and (text[Z] in concat_little_Rigth_Shift_Switch):
                            # print('Z-1 ไม่ได้ก้อยกด')
                            for little_switch in range(len(little_Rigth_Shift_Switch)):
                                if text[Z] in little_Rigth_Shift_Switch[little_switch]:
                                    Posi_little = little_switch
                                    break
                            Dis_Z1 = abs(little_Left_Shift_Switch[0].index('A') - little_Left_Shift_Switch[0].index('SHIFT'))
                            Dis_Z  = abs(little_Rigth_Shift_Switch[Posi_little].index(text[Z]) - little_Rigth_Shift_Switch[Posi_little].index('SHIFT'))
                            totaltime += timeText+((Dis_Z1+Dis_Z)*timedistance)
                        #กรณีที่ Z-1 ใช้นิ้วก้อยกด และ Z ไม่ต้องใช้นิ้วก้อย
                        elif (text[Z-1] in concat_little_Left_Shift_Switch) and (text[Z] not in concat_little_Rigth_Shift_Switch):
                            Dis_Z1 = abs(little_Left_Shift_Switch[0].index(text[Z-1]) - little_Left_Shift_Switch[0].index('SHIFT'))
                            # print(Dis_Z1)
                            if text[Z] in KeyBroad_Rigth_index_Shift:
                        
                                for posi_textZ_indexfinger_switch in range(len(KeyBroad_Rigth_Indexfinger_Shift)):

                                    if text[Z] in KeyBroad_Rigth_Indexfinger_Shift[posi_textZ_indexfinger_switch]:
                                        Posi_indexfinger_switch = posi_textZ_indexfinger_switch
                                        break
                                    
                                if Posi_indexfinger_switch == 0:
                                    if text[Z] == 'J':
                                        totaltime += timeText+(Dis_Z1*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger_switch].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index('J'))
                                        totaltime += timeText+(dis*timedistance)+(Dis_Z1*timedistance)
                                else:

                                    if KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger_switch].index(text[Z]) == KeyBroad_Rigth_Indexfinger_Shift[0].index('J'):
                                        totaltime += timeText+(1*timedistance)+(Dis_Z1*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger_switch].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index('J'))+1
                                        totaltime += timeText+(dis*timedistance)+(Dis_Z1*timedistance)

                            # นิ้ว กลางและนาง ขวา กด Shilf
                            elif text[Z] in KeyBroad_Rigth_MR_Shift:
                                for posi_textZ in range(len(KeyBroad_Rigth_Shift)):
                                    if text[Z] in KeyBroad_Rigth_Shift[posi_textZ]:
                                        Posi_fingerZ = posi_textZ
                                        break
                                if text[Z] == KeyBroad_Rigth_Shift[Posi_fingerZ][2]:
                                    totaltime += timeText+(Dis_Z1*timedistance)
                                else:
                                    dis = abs(KeyBroad_Rigth_Shift[Posi_fingerZ].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_fingerZ].index(KeyBroad_Rigth_Shift[Posi_fingerZ][2])) 
                                    totaltime += timeText+(dis*timedistance)+(Dis_Z1*timedistance)

                        # ไม่ต้องใช้นิ้วก้อยทั้งสองข้าง
                        elif (text[Z-1] not in concat_little_Left_Shift_Switch) and (text[Z] not in concat_little_Rigth_Shift_Switch):
                            if text[Z] in KeyBroad_Rigth_index_Shift:
                                # หา ตน ของนิ้วชี้ที่กด เนื่องจาก นิ้วชิ้วต้องกด 2 colume
                                for posi_text0_indexfinger in range(len(KeyBroad_Rigth_Indexfinger_Shift)):
                                    if text[Z] in KeyBroad_Rigth_Indexfinger_Shift[posi_text0_indexfinger]:
                                        Posi_indexfinger = posi_text0_indexfinger
                                        # print(Posi_indexfinger)
                                        break
                                if Posi_indexfinger == 0:
                                    if text[Z] == 'J':
                                        # (2*timedistance) ได้จากระยะห่างจากนิ้วก้อยซ้ายไปกด Shift
                                        totaltime += timeText+(2*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index('J'))
                                        totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                else:
                                    # เมื่อ text[0] == J ระยะห่างจาก J ถึง H เท่ากัน 1 Dis รวมกับ นิ้วก้อยซ้ายกดShif
                                    if KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) == KeyBroad_Rigth_Indexfinger_Shift[0].index('J'):
                                        totaltime += timeText+(1*timedistance)+(2*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index('J'))+1
                                        totaltime += timeText+(dis*timedistance)+(2*timedistance)

                            # นิ้ว กลางและนาง ขวา กด Shilf
                            elif text[Z] in KeyBroad_Rigth_MR_Shift:
                                for posi_textZ in range(len(KeyBroad_Rigth_Shift)):
                                    if text[Z] in KeyBroad_Rigth_Shift[posi_textZ]:
                                        Posi_finger = posi_textZ
                                        break
                                if text[Z] == KeyBroad_Rigth_Shift[Posi_finger][2]:
                                    totaltime += timeText+(2*timedistance)
                                else:
                                    dis = abs(KeyBroad_Rigth_Shift[Posi_finger].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_finger].index(KeyBroad_Rigth_Shift[Posi_finger][2])) 
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)

                    #เมื่ออยู่ฝั่งขวาย้ายมากดฝั่งซ้าย
                    elif (text[Z] in KeyBroad_LeftShift) and (text[Z-1] in KeyBroad_RigthShift):
                        print("ฝั่งขวาย้ายมากดฝั่งซ้าย")
                        #กรณีที่ Z-1 ใช้นิ้วก้อยกด และ Z ยังต้องใช้นิ้วก้อย
                        if(text[Z-1] in concat_little_Rigth_Shift_Switch ) and (text[Z] in concat_little_Left_Shift_Switch):
                            for little_switch in range(len(little_Rigth_Shift_Switch)):
                                if text[Z-1] in little_Rigth_Shift_Switch[little_switch]:
                                    Posi_little = little_switch
                                    break
                            Dis_Z1 = abs(little_Rigth_Shift_Switch[Posi_little].index(text[Z-1]) - little_Rigth_Shift_Switch[Posi_little].index('SHIFT'))
                            Dis_Z = abs(little_Left_Shift_Switch[0].index(text[Z]) - little_Left_Shift_Switch[0].index('SHIFT'))
                            totaltime += timeText+((Dis_Z1+Dis_Z)*timedistance)
                        # กรณีที่Z-1 ไม่ใช้นิ้วก้อย Z ใช้นิ้วก้อย
                        elif (text[Z-1] not in concat_little_Rigth_Shift_Switch) and (text[Z] in concat_little_Left_Shift_Switch):
                            Dis_Z1 = abs(little_Rigth_Shift_Switch[0].index(':') - little_Rigth_Shift_Switch[0].index('SHIFT'))
                            Dis_Z = abs(little_Left_Shift_Switch[0].index(text[Z]) - little_Left_Shift_Switch[0].index('SHIFT'))
                            totaltime += timeText+((Dis_Z1+Dis_Z)*timedistance)
                        # กรณีที่Z-1 นิ้วก้อย Z ไม่ใช้นิ้วก้อย
                        elif (text[Z-1] in concat_little_Rigth_Shift_Switch) and (text[Z] not in concat_little_Left_Shift_Switch):
                            for little_switch in range(len(little_Rigth_Shift_Switch)):
                                if text[Z-1] in little_Rigth_Shift_Switch[little_switch]:
                                    Posi_little = little_switch
                                    break
                            Dis_Z1 = abs(little_Rigth_Shift_Switch[Posi_little].index(text[Z-1]) - little_Rigth_Shift_Switch[Posi_little].index('SHIFT'))
                            if text[Z] in KeyBroad_Left_LRM_Shift:
                                # หาว่า text[0] ให้นิ้วไหนกด ก น กล
                                for posi_textZ in range(len(KeyBroad_Left_Shift)):
                                    if text[Z] in KeyBroad_Left_Shift[posi_textZ]:
                                        Posi_fingerZ = posi_textZ
                                        break
                                # นำ ตน นิ้วที่ได้มาหาระยะห่าง กรณีที่ไม่มีการขยับจากตัวออักษรจากจัดวางมือ
                                if text[Z] == KeyBroad_Left_Shift[Posi_fingerZ][2]:
                                    # print(text[0]+"เป็นตัว"+KeyBroad_Left_Shift[Posi_finger][2]+"เหมือนกัน")
                                    # (2*timedistance) ได้จาก นิ้วก้อยฝั่งซ้ายไปกด Shift
                                    totaltime += timeText+(2*timedistance)
                                    # print(totaltime)
                                else:
                                    dis = abs(KeyBroad_Left_Shift[Posi_fingerZ].index(text[Z]) - KeyBroad_Left_Shift[Posi_fingerZ].index(KeyBroad_Left_Shift[Posi_fingerZ][2])) 
                                    totaltime += timeText+(dis*timedistance)+(Dis_Z1*timedistance)

                            elif text[Z] in KeyBroad_Left_Index_Shift:
                                # หา ตน ของนิ้วชี้ที่กด เนื่องจาก นิ้วชิ้วต้องกด 2 colume
                                for posi_textZ_indexfinger in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                    if text[Z] in KeyBroad_Left_Indexfinger_Shift[posi_textZ_indexfinger]:
                                        Posi_indexfingerZ = posi_textZ_indexfinger
                                        # print(Posi_indexfinger)
                                        break
                                # เมื่อ text[0] อยู่ใน colume1 
                                if Posi_indexfingerZ == 0:
                                    if text[Z] == 'F':
                                        totaltime += timeText+(Dis_Z1*timedistance)
                                        # print(totaltime)
                                    else:
                                        dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfingerZ].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[Posi_indexfingerZ].index('F'))
                                        totaltime += timeText+(dis*timedistance)+(Dis_Z1*timedistance)
                                # เมื่อ text[0] อยู่ใน colume1 
                                else:
                                    # เมื่อ text[0] == G ระยะห่างจาก F ถึง G เท่ากัน 1 Dis รวมกับ นิ้วก้อนขวากดShif
                                    if KeyBroad_Left_Indexfinger_Shift[Posi_indexfingerZ].index(text[Z]) == KeyBroad_Left_Indexfinger_Shift[0].index('F'):
                                        totaltime += timeText+(1*timedistance)+(Dis_Z1*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfingerZ].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[0].index('F'))+1
                                        totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                        
                        # กรณีที่Z-1 นิ้วก้อย Z ไม่ใช้นิ้วก้อย
                        elif (text[Z-1] not in concat_little_Rigth_Shift_Switch) and (text[Z] not in concat_little_Left_Shift_Switch):
                            print("ไม่ก้อยตึงสอง")
                            if text[Z] in KeyBroad_Left_LRM_Shift:
                                # หาว่า text[0] ให้นิ้วไหนกด ก น กล
                                for posi_textZ in range(len(KeyBroad_Left_Shift)):
                                    if text[Z] in KeyBroad_Left_Shift[posi_textZ]:
                                        Posi_fingerZ = posi_textZ
                                        break
                                # นำ ตน นิ้วที่ได้มาหาระยะห่าง กรณีที่ไม่มีการขยับจากตัวออักษรจากจัดวางมือ
                                if text[Z] == KeyBroad_Left_Shift[Posi_fingerZ][2]:
                                    # print(text[0]+"เป็นตัว"+KeyBroad_Left_Shift[Posi_finger][2]+"เหมือนกัน")
                                    # (2*timedistance) ได้จาก นิ้วก้อยฝั่งซ้ายไปกด Shift
                                    totaltime += timeText+(2*timedistance)
                                    # print(totaltime)
                                else:
                                    dis = abs(KeyBroad_Left_Shift[Posi_fingerZ].index(text[Z]) - KeyBroad_Left_Shift[Posi_fingerZ].index(KeyBroad_Left_Shift[Posi_fingerZ][2])) 
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)

                            elif text[Z] in KeyBroad_Left_Index_Shift:
                                # หา ตน ของนิ้วชี้ที่กด เนื่องจาก นิ้วชิ้วต้องกด 2 colume
                                for posi_textZ_indexfinger in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                    if text[Z] in KeyBroad_Left_Indexfinger_Shift[posi_textZ_indexfinger]:
                                        Posi_indexfingerZ = posi_textZ_indexfinger
                                        # print(Posi_indexfinger)
                                        break
                    
                                if Posi_indexfingerZ == 0:
                                    if text[Z] == 'F':
                                        totaltime += timeText+(2*timedistance)
                                        # print(totaltime)
                                    else:
                                        dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfingerZ].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[Posi_indexfingerZ].index('F'))
                
                                else:
                                    # เมื่อ text[Z] == G ระยะห่างจาก F ถึง G เท่ากัน 1 Dis รวมกับ นิ้วก้อนขวากดShif
                                    if KeyBroad_Left_Indexfinger_Shift[Posi_indexfingerZ].index(text[Z]) == KeyBroad_Left_Indexfinger_Shift[0].index('F'):
                                        totaltime += timeText+(1*timedistance)+(2*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfingerZ].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[0].index('F'))+1
                                        totaltime += timeText+(dis*timedistance)+(2*timedistance)

                # ตัวก่อนหน้าเป็นตัวพิมพ์เล็ก
                elif (text[Z-1] in All_Alphabet_NoShift) and (text[Z] in All_Alphabet_Shift):
                        # กรณี Z-1 อยู่ฝั่นซ้าย แล้วตัว Z เป็นตัวพิมพ์ใหญ่ฝั่งซ้ายเหมือนกัน
                        if(text[Z-1] in KeyBroad_LeftNoShift) and (text[Z] in KeyBroad_LeftShift):
                            # กรณี Z-1 อยู่ฝั่งซ้าย แล้วตัว Z เป็นตัวพิมพ์ใหญ่ฝั่งซ้าย ใช้นิ้วเดียวกันกด ก น กล
                            if(text[Z-1] in KeyBroad_Left_lrm_NoShift) and (text[Z] in KeyBroad_Left_LRM_Shift):

                                for Posi_Z1_NoShift in range(len(KeyBroad_Left_NoShift)):
                                    if(text[Z-1] in KeyBroad_Left_NoShift[Posi_Z1_NoShift]):
                                        Posi_Z1_No_Shift = Posi_Z1_NoShift
                                        break
                                for Posi_Z_Shift in range(len(KeyBroad_Left_Shift)):
                                    if(text[Z] in KeyBroad_Left_Shift[Posi_Z_Shift]):
                                        Posi_Z_Shift = Posi_Z_Shift
                                        break
                                if Posi_Z1_NoShift == Posi_Z_Shift:
                                    position = Posi_Z_Shift
                                    if(KeyBroad_Left_NoShift[position].index(text[Z-1]) == KeyBroad_Left_Shift[position].index(text[Z])):
                                        totaltime += timeDuplicate+(2*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Left_NoShift[Posi_Z1_No_Shift].index(text[Z-1]) - KeyBroad_Left_Shift[Posi_Z_Shift].index(text[Z]))
                                        totaltime +=  timeText+(dis*timedistance)+(2*timedistance)
                                        
                                else:
                                    dis = abs(KeyBroad_Left_Shift[Posi_Z_Shift].index(text[Z]) - KeyBroad_Left_Shift[Posi_Z_Shift].index(KeyBroad_Left_Shift[Posi_Z_Shift][2]))
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                            # กรณี Z-1 อยู่ฝั่งซ้าย แล้วตัว Z เป็นตัวพิมพ์ใหญ่ฝั่งซ้าย ใช้นิ้วเดียวกันกด ชี้
                            elif(text[Z-1] in KeyBroad_Left_index_NoShift) and (text[Z] in KeyBroad_Left_Index_Shift):
                                for Posi_Z1_NoShift in range(len(KeyBroad_Left_Indexfinger_NoShift)):
                                    if text[Z-1] in KeyBroad_Left_Indexfinger_NoShift[Posi_Z1_NoShift]:
                                        Posi_Z1_No_Shift = Posi_Z1_NoShift
                                        break
                                for Posi_Z_Shift in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                    if(text[Z] in KeyBroad_Left_Indexfinger_Shift[Posi_Z_Shift]):
                                        Posi_Z_Shift = Posi_Z_Shift
                                        break
 
                                if Posi_Z_Shift == Posi_Z1_No_Shift:
                                    position = Posi_Z1_No_Shift
                                    dis = abs(KeyBroad_Left_Indexfinger_NoShift[position].index(text[Z-1]) - KeyBroad_Left_Indexfinger_Shift[position].index(text[Z]))
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                else:
                                    dis = abs(KeyBroad_Left_Indexfinger_NoShift[Posi_Z1_No_Shift].index(text[Z-1]) - KeyBroad_Left_Indexfinger_Shift[Posi_Z_Shift].index(text[Z]))+1
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                            # ฝั่งซ้ายเหมือนกันแต่ คนละนิ้ว
                            else:
                                if(text[Z] in KeyBroad_Left_LRM_Shift):
                                    for Posi_Z_Shift in range(len(KeyBroad_Left_Shift)):
                                        if(text[Z] in KeyBroad_Left_Shift[Posi_Z_Shift]):
                                            Posi_Z_Shift = Posi_Z_Shift
                                            break
                                    if text[Z] == KeyBroad_Left_Shift[Posi_Z_Shift][2]:
                                        totaltime += timeText+(2*timedistance)
                                        # print(totaltime)
                                    else:
                                        dis = abs(KeyBroad_Left_Shift[Posi_Z_Shift].index(text[Z]) - KeyBroad_Left_Shift[Posi_Z_Shift].index(KeyBroad_Left_Shift[Posi_Z_Shift][2])) 
                                        totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                elif text[Z] in KeyBroad_Left_Index_Shift:
                                    # หา ตน ของนิ้วชี้ที่กด เนื่องจาก นิ้วชิ้วต้องกด 2 colume
                                    for posi_text0_indexfinger in range(len(KeyBroad_Left_Indexfinger_Shift)):

                                        if text[Z] in KeyBroad_Left_Indexfinger_Shift[posi_text0_indexfinger]:
                                            Posi_indexfinger = posi_text0_indexfinger
                                            # print(Posi_indexfinger)
                                            break
             
                                    if Posi_indexfinger == 0:
                                        if text[Z] == 'F':
                                            totaltime += timeText+(2*timedistance)
                                            # print(totaltime)
                                        else:
                                            dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index('F'))
                                            totaltime += timeText+(dis*timedistance)+(2*timedistance)

                                    else:
    
                                        if KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) == KeyBroad_Left_Indexfinger_Shift[0].index('F'):
                                            totaltime += timeText+(1*timedistance)+(2*timedistance)
                                        else:
                                            dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[0].index('F'))+1
                                            totaltime += timeText+(dis*timedistance)+(2*timedistance)
                        # กรณี Z-1 อยู่ฝั่งขวา แล้วตัว Z เป็นตัวพิมพ์ใหญ่ฝั่งขวาเหมือนกัน
                        elif(text[Z-1] in KeyBroad_RigthNoShift) and (text[Z] in KeyBroad_RigthShift):
                            # กรณีที่เป็นนิ้วชี้ข้างขวาทั้งคู่
                            if(text[Z-1] in KeyBroad_Rigth_index_NoShift) and (text[Z] in KeyBroad_Rigth_index_Shift):
                                for Posi_Z1_NoShift in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                    if text[Z-1] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Z1_NoShift]:
                                        Posi_Z1_No_Shift = Posi_Z1_NoShift
                                        break
                                for Posi_Z_Shift in range(len(KeyBroad_Rigth_Indexfinger_Shift)):
                                    if(text[Z] in KeyBroad_Rigth_Indexfinger_Shift[Posi_Z_Shift]):
                                        Posi_Z_Shift = Posi_Z_Shift
                                        break
                                if Posi_Z_Shift == Posi_Z1_No_Shift:
                                    position = Posi_Z1_No_Shift
                                    dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[position].index(text[Z-1]) - KeyBroad_Rigth_Indexfinger_Shift[position].index(text[Z]))
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                else:
                                    dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_Z1_No_Shift].index(text[Z-1]) - KeyBroad_Rigth_Indexfinger_Shift[Posi_Z_Shift].index(text[Z]))+1
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                            # กรณีที่เป็นนิ้วกลางและนางข้างขวาทั้งคู่
                            elif (text[Z-1] in KeyBroad_Rigth_mr_NoShift) and (text[Z] in KeyBroad_Rigth_MR_Shift):

                                for Posi_Z1_NoShift in range(len(KeyBroad_Rigth_NoShift)):
                                    if text[Z-1] in KeyBroad_Rigth_NoShift[Posi_Z1_NoShift]:
                                        Posi_Z1_No_Shift = Posi_Z1_NoShift
                                        break
                                for Posi_Z_Shift in range(len(KeyBroad_Rigth_Shift)):
                                    if(text[Z] in KeyBroad_Rigth_Shift[Posi_Z_Shift]):
                                        Posi_Z_Shift = Posi_Z_Shift
                                        break
                                if Posi_Z1_No_Shift == Posi_Z_Shift:
                                    position = Posi_Z_Shift
                                    dis = abs(KeyBroad_Rigth_NoShift[position].index(text[Z-1]) - KeyBroad_Rigth_Shift[position].index(text[Z]))
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                else:
                                    dis = abs(KeyBroad_Rigth_Shift[Posi_Z_Shift].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_Z_Shift].index(KeyBroad_Rigth_Shift[Posi_Z_Shift][2]))
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                            # กรณีที่เป็นนิ้วก้อยข้างขวาทั้งคู่
                            elif (text[Z-1] in KeyBroad_Rigth_little_NoShift) and (text[Z] in KeyBroad_Rigth_Little_Shift):
                                for Posi_Z1_NoShift in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                                    if text[Z-1] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_Z1_NoShift]:
                                        Posi_Z1_No_Shift = Posi_Z1_NoShift
                                        break
                                for Posi_Z_Shift in range(len(KeyBroad_Rigth_Littlefinger_Shift)):
                                    if(text[Z] in KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_Shift]):
                                        Posi_Z_Shift = Posi_Z_Shift
                                        break
                                if Posi_Z1_NoShift == Posi_Z_Shift:
                                    position = Posi_Z_Shift
                                    dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[position].index(text[Z-1]) - KeyBroad_Rigth_Littlefinger_Shift[position].index(text[Z]))
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                else:
                                    distanceColume = abs(Posi_Z1_NoShift - Posi_Z_Shift)
                                    dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_Z1_No_Shift].index(text[Z-1]) - KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_Shift].index(text[Z]))+distanceColume
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                            # คนละนิ้วข้างขวา
                            else:
                                #นิ้วชี้ฝั่งขวา on shift
                                if text[Z] in KeyBroad_Rigth_index_Shift:
                                    # หา ตน ของนิ้วชี้ที่กด เนื่องจาก นิ้วชิ้วต้องกด 2 colume
                                    for posi_text0_indexfinger in range(len(KeyBroad_Rigth_Indexfinger_Shift)):

                                        if text[Z] in KeyBroad_Rigth_Indexfinger_Shift[posi_text0_indexfinger]:
                                            Posi_indexfinger = posi_text0_indexfinger
                                            # print(Posi_indexfinger)
                                            break
                                    if Posi_indexfinger == 0:
                                        if text[Z] == 'J':
                                            # (2*timedistance) ได้จากระยะห่างจากนิ้วก้อยซ้ายไปกด Shift
                                            totaltime += timeText+(2*timedistance)
                                        else:
                                            dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index('J'))
                                            totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                    else:
                                        # เมื่อ text[Z] == J ระยะห่างจาก J ถึง H เท่ากัน 1 Dis รวมกับ นิ้วก้อยซ้ายกดShif
                                        if KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) == KeyBroad_Rigth_Indexfinger_Shift[0].index('J'):
                                            totaltime += timeText+(1*timedistance)+(2*timedistance)
                                        else:
                                            dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index('J'))+1
                                            totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                # นิ้วกลาง นาง
                                elif text[Z] in KeyBroad_Rigth_MR_Shift:
                                    for posi_text0 in range(len(KeyBroad_Rigth_Shift)):
                                        if text[Z] in KeyBroad_Rigth_Shift[posi_text0]:
                                            Posi_finger = posi_text0
                                            break
                                    if text[Z] == KeyBroad_Rigth_Shift[Posi_finger][2]:
                                        totaltime += timeText+(2*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Rigth_Shift[Posi_finger].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_finger].index(KeyBroad_Rigth_Shift[Posi_finger][2])) 
                                        totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                elif(text[Z] in KeyBroad_Rigth_Little_Shift):
                                    for Posi_Z in range(len(KeyBroad_Rigth_Littlefinger_Shift)):
                                        if text[Z] in KeyBroad_Rigth_Littlefinger_Shift[Posi_Z]:
                                            Posi_Z_current = Posi_Z
                                            break
                                    if(Posi_Z_current == 0):
                                        dis = abs(KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_current].index(KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_current][2]))
                                        totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                    else:
                                        distanceColume = abs(Posi_Z_current-0)
                                        dis = abs(KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[0].index(KeyBroad_Rigth_Littlefinger_Shift[0][2]))+distanceColume
                                        totaltime += timeText+(dis*timedistance)+(2*timedistance)

                        # กรณีที่ Z-1 ตัวเล็กซ้ายเปลี่ยนเป็น Z ย้ายมากดฝั่งขวา
                        elif (text[Z-1] in KeyBroad_LeftNoShift) and (text[Z] in KeyBroad_RigthShift):
                            # กรณีที่ Z-1 ใช้นิ้วก้อยกด และ Z ต้องใช้นิ้วก้อยฝั่งขวา
                            if(text[Z-1] in concat__Left_NoShift_Switch) and (text[Z] in KeyBroad_Rigth_Little_Shift):
                                for Posi_Z_current_swicth in range(len(KeyBroad_Rigth_Littlefinger_Shift)):
                                    if text[Z] in KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_current_swicth]:
                                        Posi_Z_current = Posi_Z_current_swicth
                                        break
                                Dis_Z = abs(KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[0].index(KeyBroad_Rigth_Littlefinger_Shift[0][2]))+Posi_Z_current
                                Dis_Z1 = abs(little_Left_NoShift_Switch[0].index(text[Z-1]) - little_Left_NoShift_Switch[0].index('shift'))
                                dis = Dis_Z + Dis_Z1
                                totaltime += timeText+(dis*timedistance)
                            # กรณีที่ Z-1 ใช้นิ้วก้อยกด และ Z ไม่ใช้นิ้วก้อยฝั่งขวา
                            elif (text[Z-1] in concat__Left_NoShift_Switch) and (text[Z] not in KeyBroad_Rigth_Little_Shift):
                                Dis_Z1 = abs(little_Left_NoShift_Switch[0].index(text[Z-1]) - little_Left_NoShift_Switch[0].index('shift'))
                                #  Z ไม่ใช้นิ้วก้อยฝั่งขวา เป็น กลาง นาง
                                if text[Z] in KeyBroad_Rigth_MR_Shift:
                                    for Posi_Z_current_swicth in range(len(KeyBroad_Rigth_Shift)):
                                        if(text[Z] in KeyBroad_Rigth_Shift[Posi_Z_current_swicth]):
                                            Posi_Z_current = Posi_Z_current_swicth
                                            break
                                    Dis_Z = abs(KeyBroad_Rigth_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_Z_current].index(KeyBroad_Rigth_Shift[Posi_Z_current][2]))
                                    dis = Dis_Z + Dis_Z1

                                    totaltime += timeText+(dis*timedistance)
                                #  Z ไม่ใช้นิ้วก้อยฝั่งขวา เป็น ชี้
                                elif text[Z] in KeyBroad_Rigth_index_Shift:
                                    for Posi_Z_current_swicth in range(len(KeyBroad_Rigth_Indexfinger_Shift)):
                                        if(text[Z] in KeyBroad_Rigth_Indexfinger_Shift[Posi_Z_current_swicth]):
                                            Posi_Z_current = Posi_Z_current_swicth
                                            break
                                    Dis_Z = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index(KeyBroad_Rigth_Indexfinger_Shift[0][2]))+Posi_Z_current 
                                    dis = Dis_Z + Dis_Z1
                                    totaltime += timeText+(dis*timedistance)
                            # กรณีที่ Z-1 ไม่ใช้นิ้วก้อย แต่ Z ใช้นิ้วก้อย
                            elif (text[Z-1] not in concat__Left_NoShift_Switch) and (text[Z] in KeyBroad_Rigth_Little_Shift):
                                for Posi_Z_current_swicth in range(len(KeyBroad_Rigth_Littlefinger_Shift)):
                                    if text[Z] in KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_current_swicth]:
                                        Posi_Z_current = Posi_Z_current_swicth
                                        break

                                dis = abs(KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[0].index( KeyBroad_Rigth_Littlefinger_Shift[0][2]))+Posi_Z_current
                                totaltime += timeText+(dis*timedistance)+(2*timedistance)

                            elif (text[Z-1] not in concat__Left_NoShift_Switch) and (text[Z] not in KeyBroad_Rigth_Little_Shift):
                                print("ไม่ก้อยทั้งสอง")
                                if text[Z] in KeyBroad_Rigth_index_Shift:
                                    # หา ตน ของนิ้วชี้ที่กด เนื่องจาก นิ้วชิ้วต้องกด 2 colume
                                    for posi_text0_indexfinger in range(len(KeyBroad_Rigth_Indexfinger_Shift)):
                                        if text[Z] in KeyBroad_Rigth_Indexfinger_Shift[posi_text0_indexfinger]:
                                            Posi_indexfinger = posi_text0_indexfinger
                                            # print(Posi_indexfinger)
                                            break
                                    if Posi_indexfinger == 0:
                                        if text[Z] == 'J':
                                            # (2*timedistance) ได้จากระยะห่างจากนิ้วก้อยซ้ายไปกด Shift
                                            totaltime += timeText+(2*timedistance)
                                        else:
                                            dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index('J'))
                                            totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                    else:
                                        # เมื่อ text[0] == J ระยะห่างจาก J ถึง H เท่ากัน 1 Dis รวมกับ นิ้วก้อยซ้ายกดShif
                                        if KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) == KeyBroad_Rigth_Indexfinger_Shift[0].index('J'):
                                            totaltime += timeText+(1*timedistance)+(2*timedistance)
                                        else:
                                            dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_indexfinger].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index('J'))+1
                                            totaltime += timeText+(dis*timedistance)+(2*timedistance)

                                # นิ้ว กลางและนาง ขวา กด Shilf
                                elif text[Z] in KeyBroad_Rigth_MR_Shift:
                                    for posi_textZ in range(len(KeyBroad_Rigth_Shift)):
                                        if text[Z] in KeyBroad_Rigth_Shift[posi_textZ]:
                                            Posi_finger = posi_textZ
                                            break
                                    if text[Z] == KeyBroad_Rigth_Shift[Posi_finger][2]:
                                        totaltime += timeText+(2*timedistance)
                                    else:
                                        dis = abs(KeyBroad_Rigth_Shift[Posi_finger].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_finger].index(KeyBroad_Rigth_Shift[Posi_finger][2])) 
                                        totaltime += timeText+(dis*timedistance)+(2*timedistance)

                        # กรณีที่ Z-1 ตัวเล็กขวาเปลี่ยนเป็น Z ย้ายมากดฝั่งซ้าย
                        elif (text[Z-1] in KeyBroad_RigthNoShift) and (text[Z] in KeyBroad_LeftShift):

                            # เมื่อ Z-1 ต้องใช้นิ้วก้อยขวากด และ Z ต้องใช้นิ้วก้อยซ้าย
                            if(text[Z-1] in concat__Rigth_NoShift_Switch) and (text[Z] in concat_little_Left_Shift_Switch):
                                for Posi_Z1_NoShift in range(len(little_Rigth_NoShift_Switch)):
                                    if text[Z-1] in little_Rigth_NoShift_Switch[Posi_Z1_NoShift]:
                                        Posi_Z1_No_Shift = Posi_Z1_NoShift
                                        break
                                Dis_Z1 = abs(little_Rigth_NoShift_Switch[Posi_Z1_No_Shift].index(text[Z-1]) - little_Rigth_NoShift_Switch[Posi_Z1_No_Shift].index('shift'))
                                Dis_Z = abs(KeyBroad_Left_Shift[0].index(text[Z]) - KeyBroad_Left_Shift[0].index(KeyBroad_Left_Shift[0][2]))
                                dis = Dis_Z + Dis_Z1
                                totaltime += timeText+(dis*timedistance)
                            #------------------------- งง ----------------------------------------
                            # เมื่อ Z-1 ไม่ต้องใช้นิ้วก้อยขวากด และ Z ต้องใช้นิ้วก้อยซ้าย
                            elif(text[Z-1] not in concat__Rigth_NoShift_Switch) and (text[Z] in concat_little_Left_Shift_Switch):

                                Dis_Z = abs(KeyBroad_Left_Shift[0].index(text[Z]) - KeyBroad_Left_Shift[0].index(KeyBroad_Left_Shift[0][2]))
                                # totaltime += timeText+(Dis_Z*timedistance)+(2*timedistance)

                                if(text[Z-1] in KeyBroad_Rigth_mr_NoShift):
                                    for Posi_Z1_No_Shift in range(len(KeyBroad_Rigth_NoShift)):
                                        if(text[Z-1] in KeyBroad_Rigth_NoShift[Posi_Z1_No_Shift]):
                                            Posi_Z1_NoShift = Posi_Z1_No_Shift
                                            break
                                    Dis_Z1 = abs(KeyBroad_Rigth_NoShift[Posi_Z1_NoShift].index(text[Z-1]) - KeyBroad_Rigth_NoShift[Posi_Z1_NoShift].index(KeyBroad_Rigth_NoShift[Posi_Z1_NoShift][2]))
                                    dis = Dis_Z + Dis_Z1
                                    print(dis)
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                    
                                elif(text[Z-1] in KeyBroad_Rigth_index_NoShift):
                                    for Posi_Z1_No_Shift in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                        if(text[Z-1] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Z1_No_Shift]):
                                            Posi_Z1_NoShift = Posi_Z1_No_Shift
                                            break
                                    
                                    Dis_Z1 = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_Z1_NoShift].index(text[Z-1]) - KeyBroad_Rigth_Indexfinger_NoShift[0].index(KeyBroad_Rigth_Indexfinger_NoShift[0][2]))+Posi_Z1_NoShift
                                    dis = Dis_Z + Dis_Z1
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)


                            # เมื่อ Z-1 ต้องใช้นิ้วก้อยขวากด และ Z ไม่ต้องใช้นิ้วก้อยซ้าย
                            elif(text[Z-1] in concat__Rigth_NoShift_Switch) and (text[Z] not in concat_little_Left_Shift_Switch):
                                for Posi_Z1_NoShift in range(len(little_Rigth_NoShift_Switch)):
                                    if text[Z-1] in little_Rigth_NoShift_Switch[Posi_Z1_NoShift]:
                                        Posi_Z1_No_Shift = Posi_Z1_NoShift
                                        break
 
                                Dis_Z1 = abs(little_Rigth_NoShift_Switch[Posi_Z1_No_Shift].index(text[Z-1]) - little_Rigth_NoShift_Switch[Posi_Z1_No_Shift].index('shift'))+Posi_Z1_No_Shift

                                if(text[Z] in KeyBroad_Left_LRM_Shift):
                                    for Posi_Z_current_swicth in range(len(KeyBroad_Left_Shift)):
                                        if text[Z] in KeyBroad_Left_Shift[Posi_Z_current_swicth]:
                                            Posi_Z_current = Posi_Z_current_swicth
                                            break
                                    Dis_Z = abs(KeyBroad_Left_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Left_Shift[Posi_Z_current].index(KeyBroad_Left_Shift[Posi_Z_current][2]))
                                    dis = Dis_Z + Dis_Z1

                                    totaltime += timeText+(dis*timedistance)
                                
                                elif(text[Z] in KeyBroad_Left_Index_Shift):
                                    for Posi_Z_current_swicth in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                        if text[Z] in KeyBroad_Left_Indexfinger_Shift[Posi_Z_current_swicth]:
                                            Posi_Z_current = Posi_Z_current_swicth
                                            break
                                    Dis_Z = abs(KeyBroad_Left_Indexfinger_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[0].index(KeyBroad_Left_Indexfinger_Shift[Posi_Z_current][2]))+Posi_Z_current
                                    dis = Dis_Z + Dis_Z1
                                    totaltime += timeText+(dis*timedistance)

                            # เมื่อ Z-1 ไม่ต้องใช้นิ้วก้อยขวากด และ Z ไม่ต้องใช้นิ้วก้อยซ้าย
                            elif(text[Z-1] not in concat__Rigth_NoShift_Switch) and (text[Z] not in concat_little_Left_Shift_Switch):
                                if(text[Z] in KeyBroad_Left_LRM_Shift):
                                    for Posi_Z_current_swicth in range(len(KeyBroad_Left_Shift)):
                                        if text[Z] in KeyBroad_Left_Shift[Posi_Z_current_swicth]:
                                            Posi_Z_current = Posi_Z_current_swicth
                                            break
                                    dis = abs(KeyBroad_Left_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Left_Shift[Posi_Z_current].index(KeyBroad_Left_Shift[Posi_Z_current][2]))
                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)
                                
                                elif(text[Z] in KeyBroad_Left_Index_Shift):
                                    
                                    for Posi_Z_current_swicth in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                        if text[Z] in KeyBroad_Left_Indexfinger_Shift[Posi_Z_current_swicth]:
                                            Posi_Z_current = Posi_Z_current_swicth
                                            break
                                    dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_Z_current].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[0].index(KeyBroad_Left_Indexfinger_Shift[Posi_Z_current][2]))+Posi_Z_current

                                    totaltime += timeText+(dis*timedistance)+(2*timedistance)

                # ตัวก่อนหน้าเป็นตัว spacebar
                elif (text[Z-1].isspace()) and (text[Z] in All_Alphabet_Shift):
                    # ตัวก่อนหน้าเป็นตัว spacebar Z อยู่ฝั่งซ้าย
                    if(text[Z] in KeyBroad_LeftShift):
                        if(text[Z] in KeyBroad_Left_LRM_Shift):
                            for Posi_Z_current in range(len(KeyBroad_Left_Shift)):
                                if(text[Z] in KeyBroad_Left_Shift[Posi_Z_current]):
                                    Posi_Z = Posi_Z_current
                                    break
                            dis = abs(KeyBroad_Left_Shift[Posi_Z].index(text[Z]) - KeyBroad_Left_Shift[Posi_Z].index(KeyBroad_Left_Shift[Posi_Z][2]))
                            
                            totaltime += timeText+(dis*timedistance)+(2*timedistance)
                        elif(text[Z] in KeyBroad_Left_Index_Shift):
                            for Posi_Z_current in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                if(text[Z] in KeyBroad_Left_Indexfinger_Shift[Posi_Z_current]):
                                    Posi_Z = Posi_Z_current
                                    break
                            dis = abs(KeyBroad_Left_Indexfinger_Shift[Posi_Z].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[0].index(KeyBroad_Left_Indexfinger_Shift[0][2]))+Posi_Z
                            totaltime += timeText+(dis*timedistance)+(2*timedistance)

                    elif(text[Z] in KeyBroad_RigthShift):
                        if(text[Z] in KeyBroad_Rigth_index_Shift):
                            for Posi_Z_current in range(len(KeyBroad_Rigth_Indexfinger_Shift)):
                                if(text[Z] in KeyBroad_Rigth_Indexfinger_Shift[Posi_Z_current]):
                                    Posi_Z = Posi_Z_current
                                    break
                            dis = abs(KeyBroad_Rigth_Indexfinger_Shift[Posi_Z].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index(KeyBroad_Rigth_Indexfinger_Shift[0][2]))+Posi_Z
                            totaltime += timeText+(dis*timedistance)+(2*timedistance)
                        elif(text[Z] in KeyBroad_Rigth_MR_Shift):
                            for Posi_Z_current in range(len(KeyBroad_Rigth_Shift)):
                                if(text[Z] in KeyBroad_Rigth_Shift[Posi_Z_current]):
                                    Posi_Z = Posi_Z_current
                                    break
                            dis = abs(KeyBroad_Rigth_Shift[Posi_Z].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_Z].index(KeyBroad_Rigth_Shift[Posi_Z][2]))
                            totaltime += timeText+(dis*timedistance)+(2*timedistance)
                        elif(text[Z] in KeyBroad_Rigth_Little_Shift):
                            for Posi_Z_current in range(len(KeyBroad_Rigth_Littlefinger_Shift)):
                                if(text[Z] in KeyBroad_Rigth_Littlefinger_Shift[Posi_Z_current]):
                                    Posi_Z1 = Posi_Z_current
                                    break
                            dis = abs(KeyBroad_Rigth_Littlefinger_Shift[Posi_Z1].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[0].index(KeyBroad_Rigth_Littlefinger_Shift[0][2]))+Posi_Z1
                            totaltime += timeText+(dis*timedistance)+(2*timedistance)
            # text[Z] เป็นตัวพิมพ์เล็ก
            if(text[Z] in All_Alphabet_NoShift):
                # text[Z] เป็นตัวพิมพ์เล็ก text[Z-1] เป็นตัวพิมพ์เล็ก
                if(text[Z] in All_Alphabet_NoShift) and (text[Z-1] in All_Alphabet_NoShift):
                    # text[Z] เป็นตัวพิมพ์เล็ก text[Z-1] เป็นตัวพิมพ์เล็ก และอยู่ฝั่งซ้าย
                    if(text[Z] in KeyBroad_LeftNoShift) and(text[Z-1] in KeyBroad_LeftNoShift):
                        # อยู่ในนิ้ว ก น กล ทั้ง 2
                        if(text[Z] in KeyBroad_Left_lrm_NoShift) and (text[Z-1] in KeyBroad_Left_lrm_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_NoShift)):
                                if text[Z] in KeyBroad_Left_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            for Posi_Noshift_Z1 in range(len(KeyBroad_Left_NoShift)):
                                if text[Z-1] in KeyBroad_Left_NoShift[Posi_Noshift_Z1]:
                                    Posi_NoS_Z1 = Posi_Noshift_Z1
                                    break

                            if Posi_NoS_Z == Posi_NoS_Z1:
                                position = Posi_NoS_Z1
                                dis = abs(KeyBroad_Left_NoShift[position].index(text[Z]) - KeyBroad_Left_NoShift[position].index(text[Z-1]))
                                totaltime += timeText+(dis*timedistance)
                            else:
                                dis = abs(KeyBroad_Left_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_NoShift[Posi_NoS_Z].index(KeyBroad_Left_NoShift[Posi_NoS_Z][2]))
                                totaltime += timeText+(dis*timedistance)
                        # อยู่ในนิ้วชี้ทั้ง 2
                        elif (text[Z] in KeyBroad_Left_index_NoShift) and (text[Z-1] in KeyBroad_Left_index_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_Indexfinger_NoShift)):
                                if text[Z] in KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            for Posi_Noshift_Z1 in range(len(KeyBroad_Left_Indexfinger_NoShift)):
                                if text[Z-1] in KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z1]:
                                    Posi_NoS_Z1 = Posi_Noshift_Z1
                                    break
                            if Posi_NoS_Z == Posi_NoS_Z1:
                                position = Posi_NoS_Z1
                                dis = abs(KeyBroad_Left_Indexfinger_NoShift[position].index(text[Z]) - KeyBroad_Left_Indexfinger_NoShift[position].index(text[Z-1]))
                                totaltime += timeText+(dis*timedistance)
                            else:
                                dis = abs(KeyBroad_Left_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_Indexfinger_NoShift[Posi_NoS_Z1].index(text[Z-1]))+1
                                totaltime += timeText+(dis*timedistance)
                        else:
                            if(text[Z] in KeyBroad_Left_lrm_NoShift):
                                for Posi_Noshift_Z in range(len(KeyBroad_Left_NoShift)):
                                    if text[Z] in KeyBroad_Left_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Left_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_NoShift[Posi_NoS_Z].index(KeyBroad_Left_NoShift[Posi_NoS_Z][2]))
                                
                                totaltime += timeText+(dis*timedistance)
                            elif (text[Z] in KeyBroad_Left_index_NoShift):
                                for Posi_Noshift_Z in range(len(KeyBroad_Left_Indexfinger_NoShift)):
                                    if text[Z] in KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z].index(text[Z]) - KeyBroad_Left_Indexfinger_NoShift[0].index(KeyBroad_Left_Indexfinger_NoShift[0][2]))+Posi_NoS_Z
                                totaltime += timeText+(dis*timedistance)

                    #ตัวเล็กอยู่ฝั่งขวาทั้งคู่
                    elif(text[Z] in KeyBroad_RigthNoShift) and(text[Z-1] in KeyBroad_RigthNoShift):
                        #นิ้วชี้ขวาทั้งสอง
                        if(text[Z] in KeyBroad_Rigth_index_NoShift) and (text[Z-1] in KeyBroad_Rigth_index_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                if text[Z] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            for Posi_Noshift_Z1 in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                if text[Z-1] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z1]:
                                    Posi_NoS_Z1 = Posi_Noshift_Z1
                                    break
                            if Posi_NoS_Z == Posi_NoS_Z1:
                                position = Posi_NoS_Z1
                                dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[position].index(text[Z]) - KeyBroad_Rigth_Indexfinger_NoShift[position].index(text[Z-1]))
                                totaltime += timeText+(dis*timedistance)
                            else:
                                dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Indexfinger_NoShift[Posi_NoS_Z1].index(text[Z-1]))+1
                                totaltime += timeText+(dis*timedistance)
                        #นิ้วกลาง นางขวาทั้งสอง
                        elif(text[Z] in KeyBroad_Rigth_mr_NoShift) and (text[Z-1] in KeyBroad_Rigth_mr_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_NoShift)):
                                if text[Z] in KeyBroad_Rigth_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            for Posi_Noshift_Z1 in range(len(KeyBroad_Rigth_NoShift)):
                                if text[Z-1] in KeyBroad_Rigth_NoShift[Posi_Noshift_Z1]:
                                    Posi_NoS_Z1 = Posi_Noshift_Z1
                                    break
                            if Posi_NoS_Z1 == Posi_NoS_Z:
                                position = Posi_NoS_Z
                                dis = abs(KeyBroad_Rigth_NoShift[position].index(text[Z]) - KeyBroad_Rigth_NoShift[position].index(text[Z-1]))
                                totaltime += timeText+(dis*timedistance)
                            else:
                                dis = abs(KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(KeyBroad_Rigth_NoShift[Posi_NoS_Z][2]))
                                totaltime += timeText+(dis*timedistance)

                        elif(text[Z] in KeyBroad_Rigth_little_NoShift) and (text[Z-1] in KeyBroad_Rigth_little_NoShift):

                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                                if text[Z] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            for Posi_Noshift_Z1 in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                                if text[Z-1] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_Noshift_Z1]:
                                    Posi_NoS_Z1 = Posi_Noshift_Z1
                                    break
                            if Posi_NoS_Z == Posi_NoS_Z1:
                                position = Posi_NoS_Z1
                                dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[position].index(text[Z]) - KeyBroad_Rigth_Littlefinger_NoShift[position].index(text[Z-1]))
                                totaltime += timeText+(dis*timedistance)
                            else:
                                distanceColume = abs(Posi_NoS_Z1 - Posi_NoS_Z)
                                dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Littlefinger_NoShift[Posi_NoS_Z1].index(text[Z-1]))+distanceColume
                                totaltime += timeText+(dis*timedistance)
                        else:
                            if text[Z] in KeyBroad_Rigth_index_NoShift:
                                for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                    if text[Z] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z].index(text[Z]) - KeyBroad_Rigth_Indexfinger_NoShift[0].index(KeyBroad_Rigth_Indexfinger_NoShift[0][2]))+Posi_NoS_Z
                                totaltime += timeText+(dis*timedistance)
                            elif text[Z] in KeyBroad_Rigth_mr_NoShift:
                                for Posi_Noshift_Z in range(len(KeyBroad_Rigth_NoShift)):
                                    if text[Z] in KeyBroad_Rigth_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(KeyBroad_Rigth_NoShift[Posi_NoS_Z][2]))

                                totaltime += timeText+(dis*timedistance)
                            elif text[Z] in KeyBroad_Rigth_little_NoShift:
                                for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                                    if text[Z] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Littlefinger_NoShift[0].index(KeyBroad_Rigth_Littlefinger_NoShift[0][2]))+Posi_Noshift_Z
                                totaltime += timeText+(dis*timedistance)
                    # กรณีที่ฝั่งซ้ายย้ายมากฝั่งขวา
                    elif(text[Z-1] in KeyBroad_LeftNoShift) and(text[Z] in KeyBroad_RigthNoShift):
                        if text[Z] in KeyBroad_Rigth_index_NoShift:
                                for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                    if text[Z] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z].index(text[Z]) - KeyBroad_Rigth_Indexfinger_NoShift[0].index(KeyBroad_Rigth_Indexfinger_NoShift[0][2]))+Posi_NoS_Z
                                totaltime += timeText+(dis*timedistance)
                        elif text[Z] in KeyBroad_Rigth_mr_NoShift:
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_NoShift)):
                                if text[Z] in KeyBroad_Rigth_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(KeyBroad_Rigth_NoShift[Posi_NoS_Z][2]))
                            totaltime += timeText+(dis*timedistance)

                        elif text[Z] in KeyBroad_Rigth_little_NoShift:
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                                if text[Z] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Littlefinger_NoShift[0].index(KeyBroad_Rigth_Littlefinger_NoShift[0][2]))+Posi_Noshift_Z
                            totaltime += timeText+(dis*timedistance)
                    # กรณีที่ฝั่งซ้ายขวามากฝั่งซ้าย
                    elif(text[Z-1] in KeyBroad_RigthNoShift) and(text[Z] in KeyBroad_LeftNoShift):
                        if(text[Z] in KeyBroad_Left_lrm_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_NoShift)):
                                if text[Z] in KeyBroad_Left_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Left_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_NoShift[Posi_NoS_Z].index(KeyBroad_Left_NoShift[Posi_NoS_Z][2]))
                            totaltime += timeText+(dis*timedistance)
                        elif (text[Z] in KeyBroad_Left_index_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_Indexfinger_NoShift)):
                                if text[Z] in KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z].index(text[Z]) - KeyBroad_Left_Indexfinger_NoShift[0].index(KeyBroad_Left_Indexfinger_NoShift[0][2]))+Posi_NoS_Z
                            totaltime += timeText+(dis*timedistance)
                # กรณีที่ตัว Z-1 เป็นตัวพิมพ์ใหญ่ แล้ว Z เป็นตัวพิมพ์เล็ก
                elif(text[Z] in All_Alphabet_NoShift) and (text[Z-1] in All_Alphabet_Shift):
                    
                    # กรณีที่ตัว Z-1 เป็นตัวพิมพ์ใหญ่ แล้ว Z เป็นตัวพิมพ์เล็ก อยู่ฝั่งซ้ายเหมือนกัน
                    if(text[Z] in KeyBroad_LeftNoShift) and (text[Z-1] in KeyBroad_LeftShift):
                        
                        if(text[Z] in KeyBroad_Left_lrm_NoShift) and (text[Z-1] in KeyBroad_Left_LRM_Shift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_NoShift)):
                                if text[Z] in KeyBroad_Left_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break

                            for Posi_shift_Z1 in range(len(KeyBroad_Left_Shift)):
                                if text[Z-1] in KeyBroad_Left_Shift[Posi_shift_Z1]:
                                    Posi_S_Z1 = Posi_shift_Z1
                                    break

                            if Posi_NoS_Z == Posi_S_Z1:
                                position = Posi_S_Z1
                                if KeyBroad_Left_NoShift[position].index(text[Z]) == KeyBroad_Left_Shift[position].index(text[Z-1]):
                                    totaltime += timeDuplicate
                                else:
                                    dis = abs(KeyBroad_Left_NoShift[position].index(text[Z]) - KeyBroad_Left_Shift[position].index(text[Z-1]))
                                    totaltime += timeText+(dis*timedistance)
                            else:
                                dis = abs(KeyBroad_Left_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_NoShift[Posi_NoS_Z].index(KeyBroad_Left_NoShift[Posi_NoS_Z][2]))
                                totaltime += timeText+(dis*timedistance)

                        elif(text[Z] in KeyBroad_Left_index_NoShift) and (text[Z-1] in KeyBroad_Left_Index_Shift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_Indexfinger_NoShift)):
                                if text[Z] in KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break

                            for Posi_shift_Z1 in range(len(KeyBroad_Left_Indexfinger_Shift)):
                                if text[Z-1] in KeyBroad_Left_Indexfinger_Shift[Posi_shift_Z1]:
                                    Posi_S_Z1 = Posi_shift_Z1
                                    break
                            if Posi_NoS_Z == Posi_S_Z1:
                                position = Posi_S_Z1
                                if KeyBroad_Left_Indexfinger_NoShift[position].index(text[Z]) == KeyBroad_Left_Indexfinger_Shift[position].index(text[Z-1]):
                                    totaltime += timeDuplicate
                                else:
                                    dis = abs(KeyBroad_Left_Indexfinger_NoShift[position].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[position].index(text[Z-1]))
                                    totaltime += timeText+(dis*timedistance)
                            else:
                                dis = abs(KeyBroad_Left_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_Indexfinger_Shift[Posi_S_Z1].index(text[Z-1]))+1
                                totaltime += timeText+(dis*timedistance)
                        else:
                            if(text[Z] in KeyBroad_Left_lrm_NoShift):
                                for Posi_Noshift_Z in range(len(KeyBroad_Left_NoShift)):
                                    if text[Z] in KeyBroad_Left_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Left_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_NoShift[Posi_NoS_Z].index(KeyBroad_Left_NoShift[Posi_NoS_Z][2]))
                                totaltime += timeText+(dis*timedistance)

                            elif(text[Z] in KeyBroad_Left_index_NoShift):
                                for Posi_Noshift_Z in range(len(KeyBroad_Left_Indexfinger_NoShift)):
                                    if text[Z] in KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Left_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_Indexfinger_NoShift[0].index(KeyBroad_Left_Indexfinger_NoShift[0][2]))+Posi_NoS_Z
                                totaltime += timeText+(dis*timedistance)
                    # กรณีที่ตัว Z-1 เป็นตัวพิมพ์ใหญ่ แล้ว Z เป็นตัวพิมพ์เล็ก อยู่ฝั่งขวาเหมือนกัน
                    elif(text[Z] in KeyBroad_RigthNoShift) and (text[Z-1] in KeyBroad_RigthShift):
                        if(text[Z] in KeyBroad_Rigth_index_NoShift) and (text[Z-1] in KeyBroad_Rigth_index_Shift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                if text[Z] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            for Posi_Noshift_Z1 in range(len(KeyBroad_Rigth_Indexfinger_Shift)):
                                if text[Z-1] in KeyBroad_Rigth_Indexfinger_Shift[Posi_Noshift_Z1]:
                                    Posi_S_Z1 = Posi_Noshift_Z1
                                    break

                            if Posi_S_Z1 == Posi_NoS_Z:
                                position = Posi_NoS_Z
                                if KeyBroad_Rigth_Indexfinger_NoShift[position].index(text[Z]) == KeyBroad_Rigth_Indexfinger_Shift[position].index(text[Z-1]):
                                    timeText += timeDuplicate
                                else:
                                    dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[position].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[position].index(text[Z-1]))
                                    totaltime += timeText+(dis*timedistance)
                            else:
                                dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[Posi_S_Z1].index(text[Z-1]))+1
                                totaltime += timeText+(dis*timedistance)

                        elif(text[Z] in KeyBroad_Rigth_mr_NoShift) and (text[Z-1] in KeyBroad_Rigth_MR_Shift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_NoShift)):
                                if text[Z] in KeyBroad_Rigth_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            for Posi_Noshift_Z1 in range(len(KeyBroad_Rigth_Shift)):
                                if text[Z-1] in KeyBroad_Rigth_Shift[Posi_Noshift_Z1]:
                                    Posi_S_Z1 = Posi_Noshift_Z1
                                    break
                            if Posi_S_Z1 == Posi_NoS_Z:
                                position = Posi_NoS_Z
                                if KeyBroad_Rigth_NoShift[position].index(text[Z]) == KeyBroad_Rigth_Shift[position].index(text[Z-1]):
                                    timeText += timeDuplicate
                                else:
                                    dis = abs(KeyBroad_Rigth_NoShift[position].index(text[Z]) - KeyBroad_Rigth_Shift[position].index(text[Z-1]))
                                    totaltime += timeText+(dis*timedistance)
                            else:
                                dis = abs(KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_NoS_Z].index(KeyBroad_Rigth_Shift[Posi_NoS_Z][2]))
                                totaltime += timeText+(dis*timedistance)
                        
                        elif(text[Z] in KeyBroad_Rigth_little_NoShift) and (text[Z-1] in KeyBroad_Rigth_Little_Shift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                                if text[Z] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            for Posi_Noshift_Z1 in range(len(KeyBroad_Rigth_Littlefinger_Shift)):
                                if text[Z-1] in KeyBroad_Rigth_Littlefinger_Shift[Posi_Noshift_Z1]:
                                    Posi_S_Z1 = Posi_Noshift_Z1
                                    break
                            if Posi_S_Z1 == Posi_NoS_Z:
                                position = Posi_NoS_Z
                                if KeyBroad_Rigth_Littlefinger_NoShift[position].index(text[Z]) == KeyBroad_Rigth_Littlefinger_Shift[position].index(text[Z-1]):
                                    timeText += timeDuplicate
                                else:
                                    dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[position].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[position].index(text[Z-1]))
                                    totaltime += timeText+(dis*timedistance)
                            else:
                                distanceColume = abs(Posi_S_Z1 - Posi_NoS_Z)
                                dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[Posi_S_Z1].index(text[Z-1]))+distanceColume
                                totaltime += timeText+(dis*timedistance)
                        else:
                            if(text[Z] in KeyBroad_Rigth_index_NoShift):
                                for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                    if text[Z] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index(KeyBroad_Rigth_Indexfinger_Shift[0][2]))+Posi_NoS_Z

                                totaltime += timeText+(dis*timedistance)
                            elif(text[Z] in KeyBroad_Rigth_mr_NoShift):
                                for Posi_Noshift_Z in range(len(KeyBroad_Rigth_NoShift)):
                                    if text[Z] in KeyBroad_Rigth_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_NoS_Z].index(KeyBroad_Rigth_Shift[Posi_NoS_Z][2]))

                                totaltime += timeText+(dis*timedistance)
                            elif(text[Z] in KeyBroad_Rigth_little_NoShift):
                                for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                                    if text[Z] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[0].index(KeyBroad_Rigth_Littlefinger_Shift[0][2]))+Posi_NoS_Z
                                totaltime += timeText+(dis*timedistance)
                    # กรณีที่ Z-1 อยู่ซ้าย แล้ว Z ต้องกดขวา
                    elif (text[Z-1] in KeyBroad_LeftShift) and (text[Z] in KeyBroad_RigthNoShift):
                        if(text[Z] in KeyBroad_Rigth_index_NoShift):
                                for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                    if text[Z] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index(KeyBroad_Rigth_Indexfinger_Shift[0][2]))+Posi_NoS_Z

                                totaltime += timeText+(dis*timedistance)
                        elif(text[Z] in KeyBroad_Rigth_mr_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_NoShift)):
                                if text[Z] in KeyBroad_Rigth_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_NoS_Z].index(KeyBroad_Rigth_Shift[Posi_NoS_Z][2]))
                            totaltime += timeText+(dis*timedistance)
                        elif(text[Z] in KeyBroad_Rigth_little_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                                if text[Z] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[0].index(KeyBroad_Rigth_Littlefinger_Shift[0][2]))+Posi_NoS_Z
                            totaltime += timeText+(dis*timedistance)
                    
                    # กรณีที่ Z-1 อยู่ซ้าย แล้ว Z ต้องกดขวา
                    elif (text[Z-1] in KeyBroad_RigthShift) and (text[Z] in KeyBroad_LeftNoShift):
                        if(text[Z] in KeyBroad_Left_lrm_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_NoShift)):
                                if text[Z] in KeyBroad_Left_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Left_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_NoShift[Posi_NoS_Z].index(KeyBroad_Left_NoShift[Posi_NoS_Z][2]))
                            totaltime += timeText+(dis*timedistance)

                        elif(text[Z] in KeyBroad_Left_index_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_Indexfinger_NoShift)):
                                if text[Z] in KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Left_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_Indexfinger_NoShift[0].index(KeyBroad_Left_Indexfinger_NoShift[0][2]))+Posi_NoS_Z
                            totaltime += timeText+(dis*timedistance)
                # กรณีที่ตัว Z-1 เป็นตัวพิมพ์ใหญ่ แล้ว Z เป็นตัวพิมพ์เล็ก
                elif(text[Z] in All_Alphabet_NoShift) and (text[Z-1].isspace()):

                    if(text[Z] in KeyBroad_LeftNoShift):
                        if(text[Z] in KeyBroad_Left_lrm_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_NoShift)):
                                if text[Z] in KeyBroad_Left_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Left_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_NoShift[Posi_NoS_Z].index(KeyBroad_Left_NoShift[Posi_NoS_Z][2]))
                            totaltime += timeText+(dis*timedistance)

                        elif(text[Z] in KeyBroad_Left_index_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Left_Indexfinger_NoShift)):
                                if text[Z] in KeyBroad_Left_Indexfinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Left_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Left_Indexfinger_NoShift[0].index(KeyBroad_Left_Indexfinger_NoShift[0][2]))+Posi_NoS_Z
                            totaltime += timeText+(dis*timedistance)

                    elif(text[Z] in KeyBroad_RigthNoShift):
                        if(text[Z] in KeyBroad_Rigth_index_NoShift):
                                for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Indexfinger_NoShift)):
                                    if text[Z] in KeyBroad_Rigth_Indexfinger_NoShift[Posi_Noshift_Z]:
                                        Posi_NoS_Z = Posi_Noshift_Z
                                        break
                                dis = abs(KeyBroad_Rigth_Indexfinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Indexfinger_Shift[0].index(KeyBroad_Rigth_Indexfinger_Shift[0][2]))+Posi_NoS_Z

                                totaltime += timeText+(dis*timedistance)
                        elif(text[Z] in KeyBroad_Rigth_mr_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_NoShift)):
                                if text[Z] in KeyBroad_Rigth_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Rigth_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Shift[Posi_NoS_Z].index(KeyBroad_Rigth_Shift[Posi_NoS_Z][2]))
                            totaltime += timeText+(dis*timedistance)
                        elif(text[Z] in KeyBroad_Rigth_little_NoShift):
                            for Posi_Noshift_Z in range(len(KeyBroad_Rigth_Littlefinger_NoShift)):
                                if text[Z] in KeyBroad_Rigth_Littlefinger_NoShift[Posi_Noshift_Z]:
                                    Posi_NoS_Z = Posi_Noshift_Z
                                    break
                            dis = abs(KeyBroad_Rigth_Littlefinger_NoShift[Posi_NoS_Z].index(text[Z]) - KeyBroad_Rigth_Littlefinger_Shift[0].index(KeyBroad_Rigth_Littlefinger_Shift[0][2]))+Posi_NoS_Z
                            totaltime += timeText+(dis*timedistance)

    # print(text[z],'เวลาที่ได้ %.4f'%(totaltime),"นาที")
    timeAvg = float('%.3f'%(totaltime/1000))
    return timeAvg
        
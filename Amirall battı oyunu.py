
import random,os
def gemiler():
    while True:
        g1x1 = random.randint(1, boyut)
        g1y1 = random.randint(1, boyut)

        dikey_yatay1 = random.randint(1, 2)
        if dikey_yatay1 == 1:
            g2x1 = random.randint(1, boyut - 1)
            g2y1 = random.randint(1, boyut)
            g2x2 = g2x1 + 1
            g2y2 = g2y1
        elif dikey_yatay1 == 2:
            g2x1 = random.randint(1, boyut)
            g2y1 = random.randint(1, boyut - 1)
            g2x2 = g2x1
            g2y2 = g2y1 + 1

        dikey_yatay2 = random.randint(1, 2)
        if dikey_yatay2 == 1:
            g3x1 = random.randint(1, boyut - 2)
            g3y1 = random.randint(1, boyut)
            g3x2 = g3x1 + 1
            g3y2 = g3y1
            g3x3 = g3x1 + 2
            g3y3 = g3y1
        elif dikey_yatay2 == 2:
            g3x1 = random.randint(1, boyut)
            g3y1 = random.randint(1, boyut - 2)
            g3x2 = g3x1
            g3y2 = g3y1 + 1
            g3x3 = g3x1
            g3y3 = g3y1 + 2

        dikey_yatay3 = random.randint(1, 2)
        if dikey_yatay3 == 1:
            g4x1 = random.randint(1, boyut - 3)
            g4y1 = random.randint(1, boyut)
            g4x2 = g4x1 + 1
            g4y2 = g4y1
            g4x3 = g4x1 + 2
            g4y3 = g4y1
            g4x4 = g4x1 + 3
            g4y4 = g4y1

        elif dikey_yatay3 == 2:
            g4x1 = random.randint(1, boyut)
            g4y1 = random.randint(1, boyut - 3)
            g4x2 = g4x1
            g4y2 = g4y1 + 1
            g4x3 = g4x1
            g4y3 = g4y1 + 2
            g4x4 = g4x1
            g4y4 = g4y1 + 3
        Gemiler = [[g1x1, g1y1], [g2x1, g2y1, g2x2, g2y2], [g3x1, g3y1, g3x2, g3y2, g3x3, g3y3],
                   [g4x1, g4y1, g4x2, g4y2, g4x3, g4y3, g4x4, g4y4]]

        if Gemiler[0][0] in Gemiler[1] or Gemiler[0][0] in Gemiler[2] or Gemiler[0][0] in Gemiler[3]:
            continue
        elif Gemiler[0][1] in Gemiler[1] or Gemiler[0][1] in Gemiler[2] or Gemiler[0][1] in Gemiler[3]:
            continue
        elif Gemiler[1][0] in Gemiler[2] or Gemiler[1][0] in Gemiler[3]:
            continue
        elif Gemiler[1][1] in Gemiler[2] or Gemiler[1][1] in Gemiler[3]:
            continue
        elif Gemiler[1][2] in Gemiler[2] or Gemiler[1][2] in Gemiler[3]:
            continue

        elif Gemiler[1][3] in Gemiler[2] or Gemiler[1][3] in Gemiler[3]:
            continue

        elif Gemiler[2][0] in Gemiler[3]:
            continue

        elif Gemiler[2][1] in Gemiler[3]:
            continue

        elif Gemiler[2][2] in Gemiler[3]:
            continue

        elif Gemiler[2][3] in Gemiler[3]:
            continue

        elif Gemiler[2][4] in Gemiler[3]:
            continue

        elif Gemiler[2][5] in Gemiler[3]:
            continue

        return Gemiler
def acıkmod():
    oyunsonu=0
    atıshakkı = int((boyut * boyut) / 3)
    Gemiler=gemiler()
    Gemi1=Gemiler[0]
    Gemi2=Gemiler[1]
    Gemi3=Gemiler[2]
    Gemi4=Gemiler[3]

    print("Açık Mod")

    harita=[]
    for i in range(0, boyut):

        harita2 = []

        for j in range(0, boyut):
            harita2.append("?")

        harita.append(harita2)
    harita[Gemi1[0]-1][Gemi1[1]-1] = "*"
    harita[Gemi2[0]-1][Gemi2[1]-1] = "*"
    harita[Gemi2[2]-1][Gemi2[3]-1] = "*"
    harita[Gemi3[0]-1][Gemi3[1]-1] = "*"
    harita[Gemi3[2]-1][Gemi3[3]-1] = "*"
    harita[Gemi3[4]-1][Gemi3[5]-1] = "*"
    harita[Gemi4[0]-1][Gemi4[1]-1] = "*"
    harita[Gemi4[2]-1][Gemi4[3]-1] = "*"
    harita[Gemi4[4]-1][Gemi4[5]-1] = "*"
    harita[Gemi4[6]-1][Gemi4[7]-1] = "*"
    print("\n\n")

    while True:
        os.system("cls")
        if atıshakkı==0:
            bitti=input("Oyunu Kaybettiniz.Oyundan Çıkmak İçin (ç) Menüye Dönmek İçin Herhangi Bir Tuşa Basınız.")
            if bitti=="Ç" or bitti=="ç":
                exit()
            else:
                return 1

        for i in harita:
            for j in i:
                print(j, end="   ")
            print()
        print("Atış Hakkınız:{}" .format(atıshakkı))
        while True:
            satır = input("Satır>")
            sutun = input("Sutun>")
            try:
                satır=int(satır)
                sutun=int(sutun)
                break

            except:
                print("Lütfen Tam Sayı Giriniz")
                continue
        if satır > boyut or sutun > boyut:
            print("Lütfen Boyut Aralıklarında Değer Giriniz.")
            satır = input("Satır>")
            sutun = input("Sutun>")

        if(harita[satır-1][sutun-1]=="?") or (harita[satır-1][sutun-1]=="X") or (harita[satır-1][sutun-1]=="*"):
            if (satır==Gemi1[0]) and (sutun==Gemi1[1]):
                print("1 Numaralı Gemiyi Vurdunuz,Gemi ALABORA")
                harita[satır-1][sutun-1]="X"
                atıshakkı-=1
                oyunsonu+=1

            elif(satır==Gemi2[0]and sutun==Gemi2[1]) or (satır==Gemi2[2]and sutun==Gemi2[3]):
                print("2 Numaralı Gemiyi Vurdunuz")
                harita[satır - 1][sutun - 1] = "X"
                atıshakkı -= 1
                if (harita[Gemi2[0]-1][Gemi2[1]-1]=="X" and harita[Gemi2[2]-1][Gemi2[3]-1]=="X"):
                    print("2 Numaralı Gemi Alabora")
                    oyunsonu+=1
            elif(satır == Gemi3[0] and sutun == Gemi3[1]) or (satır == Gemi3[2] and sutun == Gemi3[3])or (satır == Gemi3[4] and sutun == Gemi3[5]):
                print("3 Numaralı Gemiyi Vurdunuz")
                harita[satır - 1][sutun - 1] = "X"
                atıshakkı -= 1
                if (harita[Gemi3[0] - 1][Gemi3[1] - 1] == "X" and harita[Gemi3[2] - 1][Gemi3[3] - 1] == "X" and harita[Gemi3[4] - 1][Gemi3[5] - 1] == "X"):
                    print("3 Numaralı Gemi Alabora")
                    oyunsonu += 1

            elif (satır == Gemi4[0] and sutun == Gemi4[1]) or (satır == Gemi4[2] and sutun == Gemi4[3])or (satır == Gemi4[4] and sutun == Gemi4[5]) or (satır == Gemi4[6] and sutun == Gemi4[7]):
                print("4 Numaralı Gemiyi Vurdunuz")
                harita[satır - 1][sutun - 1] = "X"
                atıshakkı -= 1
                if (harita[Gemi4[0] - 1][Gemi4[1] - 1] == "X" and harita[Gemi4[2] - 1][Gemi4[3] - 1] == "X" and harita[Gemi4[4] - 1][Gemi4[5] - 1] == "X" and harita[Gemi4[6] - 1][Gemi4[7] - 1] == "X" ):
                    print("4 Numaralı Gemi Alabora")
                    oyunsonu += 1
            else:

                print("MAALESEF İSABET ETTİREMEDİNİZ")
                harita[satır - 1][sutun - 1] = "/"
            if oyunsonu==4:
                print("Skorunuz = {}" .format(atıshakkı))
                devammı=input("Oyunu Kazandınız.Oyundan Çıkmak İçin (ç) AnaMenüye Dönmek İçin Herhangi Bir Tuşa Basınız.")
                if devammı=="Ç" or devammı=="ç":
                    exit()
                else:
                    return 1
        else:
            print("Daha Önce Atış Yaptınız")











def gizlimod():
    oyunsonu = 0
    atıshakkı = int((boyut * boyut) / 3)
    Gemiler = gemiler()
    Gemi1 = Gemiler[0]
    Gemi2 = Gemiler[1]
    Gemi3 = Gemiler[2]
    Gemi4 = Gemiler[3]

    print("Gizli Mod")

    harita = []
    for i in range(0, boyut):

        harita2 = []

        for j in range(0, boyut):
            harita2.append("?")

        harita.append(harita2)

    print("\n\n")

    while True:
        os.system("cls")
        if atıshakkı == 0:
            bitti = input("Oyunu Kaybettiniz.Oyundan Çıkmak İçin (ç) Menüye Dönmek İçin Herhangi Bir Tuşa Basınız.")
            if bitti == "Ç" or bitti == "ç":
                exit()
            else:
                return 1

        for i in harita:
            for j in i:
                print(j, end="   ")
            print()
        print("Atış Hakkınız:{}".format(atıshakkı))
        while True:
            satır = input("Satır>")
            sutun = input("Sutun>")
            try:
                satır = int(satır)
                sutun = int(sutun)
                break

            except:
                print("Lütfen Tam Sayı Giriniz")
                continue
        if satır > boyut or sutun > boyut:
            print("Lütfen Boyut Aralıklarında Değer Giriniz.")
            satır = input("Satır>")
            sutun = input("Sutun>")

        if (harita[satır - 1][sutun - 1] == "?") or (harita[satır - 1][sutun - 1] == "X") :
            if (satır == Gemi1[0]) and (sutun == Gemi1[1]):
                print("1 Numaralı Gemiyi Vurdunuz,Gemi ALABORA")
                harita[satır - 1][sutun - 1] = "X"
                atıshakkı -= 1
                oyunsonu += 1

            elif (satır == Gemi2[0] and sutun == Gemi2[1]) or (satır == Gemi2[2] and sutun == Gemi2[3]):
                print("2 Numaralı Gemiyi Vurdunuz")
                harita[satır - 1][sutun - 1] = "X"
                atıshakkı -= 1
                if (harita[Gemi2[0] - 1][Gemi2[1] - 1] == "X" and harita[Gemi2[2] - 1][Gemi2[3] - 1] == "X"):
                    print("2 Numaralı Gemi Alabora")
                    oyunsonu += 1
            elif (satır == Gemi3[0] and sutun == Gemi3[1]) or (satır == Gemi3[2] and sutun == Gemi3[3]) or (
                    satır == Gemi3[4] and sutun == Gemi3[5]):
                print("3 Numaralı Gemiyi Vurdunuz")
                harita[satır - 1][sutun - 1] = "X"
                atıshakkı -= 1
                if (harita[Gemi3[0] - 1][Gemi3[1] - 1] == "X" and harita[Gemi3[2] - 1][Gemi3[3] - 1] == "X" and
                        harita[Gemi3[4] - 1][Gemi3[5] - 1] == "X"):
                    print("3 Numaralı Gemi Alabora")
                    oyunsonu += 1

            elif (satır == Gemi4[0] and sutun == Gemi4[1]) or (satır == Gemi4[2] and sutun == Gemi4[3]) or (
                    satır == Gemi4[4] and sutun == Gemi4[5]) or (satır == Gemi4[6] and sutun == Gemi4[7]):
                print("4 Numaralı Gemiyi Vurdunuz")
                harita[satır - 1][sutun - 1] = "X"
                atıshakkı -= 1
                if (harita[Gemi4[0] - 1][Gemi4[1] - 1] == "X" and harita[Gemi4[2] - 1][Gemi4[3] - 1] == "X" and
                        harita[Gemi4[4] - 1][Gemi4[5] - 1] == "X" and harita[Gemi4[6] - 1][Gemi4[7] - 1] == "X"):
                    print("4 Numaralı Gemi Alabora")
                    oyunsonu += 1
            else:

                print("MAALESEF İSABET ETTİREMEDİNİZ")
                harita[satır - 1][sutun - 1] = "/"
            if oyunsonu == 4:
                print("Skorunuz = {}".format(atıshakkı))
                devammı = input(
                    "Oyunu Kazandınız.Oyundan Çıkmak İçin (ç) AnaMenüye Dönmek İçin Herhangi Bir Tuşa Basınız.")
                if devammı == "Ç" or devammı == "ç":
                    exit()
                else:
                    return 1
        else:
            print("Daha Önce Atış Yaptınız")


while True:
    os.system("cls")
    print("Mod Seçiniz")
    print("1-)Açık Mod")
    print("2-)Gizli Mod")

    while True:
        secim = input("Seçiminiz:")
        if secim=="1" or secim=="2" or secim=="3":
            break
        else:
            print("Hatalı İşlem.")
    if secim=="1":
        while True:
            boyut = input("Oyun Alanı Boyutunu Giriniz(Min 10):")
            try:
                boyut = int(boyut)
                if boyut < 10:
                    boyut = input("Oyun Alanı Boyutunu Giriniz:")
                else:
                    break
            except:
                print("Lütfen Tam Sayı Giriniz.")

        acıkmodk=acıkmod()
        if acıkmodk==1:
            continue

    if secim=="2":
        while True:
            boyut = input("Oyun Alanı Boyutunu Giriniz(Min 10):")
            try:
                boyut = int(boyut)
                if boyut < 10:
                    boyut = input("Oyun Alanı Boyutunu Giriniz:")
                else:
                    break
            except:
                print("Lütfen Tam Sayı Giriniz.")

        gizlimodk=gizlimod()
        if gizlimodk==1:
            continue


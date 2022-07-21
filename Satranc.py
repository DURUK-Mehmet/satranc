def Kontrol(deger):
    if deger>0:
        if deger%8==0:
            x_point=8
        else: 
            x_point=deger%8
        if deger%8==0:
            y_point=int(deger/8)
        else:
            y_point=int(deger/8)+1
        kordinatlar=[x_point,y_point]
        return kordinatlar
    else: 
        kordinatlar=[0,0]
        return kordinatlar

x=8
y=8
start_index=1
end_index=x*y
deger=45
print(Kontrol(deger))

#taşlar
#Kale
Kale={"x1":1,
       "y1":1,
       "x8":8,
       "y8":1,
       "x57":1,
       "y57":8,
       "x64":8,
       "y64":8
       }
while True:#Skale57
    deger=int(input("Kale57'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]!=Kale["x57"] and kordinatlar[1]==Kale["y57"]:
            Kale["x57"]=kordinatlar[0]
            break
        elif kordinatlar[0]==Kale["x57"] and kordinatlar[1]!=Kale["y57"]:
            Kale["y57"]=kordinatlar[1]
            break
        elif kordinatlar[0]!=Kale["x57"] and kordinatlar[1]!=Kale["y57"]:
            print("Kale sadece bir eksende ilerleyebilir")
            break
        else:
            print("Kale yerinde durmuştur")
            break
        print(Kale["x57"],Kale["y57"])
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while True:#Skale64
    deger=int(input("Kale64'ü nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]!=Kale["x64"] and kordinatlar[1]==Kale["y64"]:
            Kale["x64"]=kordinatlar[0]
            break
        elif kordinatlar[0]==Kale["x64"] and kordinatlar[1]!=Kale["y64"]:
            Kale["y64"]=kordinatlar[1]
            break
        elif kordinatlar[0]!=Kale["x64"] and kordinatlar[1]!=Kale["y64"]:
            print("Kale sadece bir eksende ilerleyebilir")
            break
        else:
            print("Kale yerinde durmuştur")
            break
        print(Kale["x64"],Kale["y64"])
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while True:#Skale8
    deger=int(input("Kale8'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]!=Kale["x8"] and kordinatlar[1]==Kale["y8"]:
            Kale["x8"]=kordinatlar[0]
            break
        elif kordinatlar[0]==Kale["x8"] and kordinatlar[1]!=Kale["y8"]:
            Kale["y8"]=kordinatlar[1]
            break
        elif kordinatlar[0]!=Kale["x8"] and kordinatlar[1]!=Kale["y8"]:
            print("Kale sadece bir eksende ilerleyebilir")
            break
        else:
            print("Kale yerinde durmuştur")
            break
        print(Kale["x8"],Kale["y8"])
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
    
while True:#Skale1
    deger=int(input("Kale1'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]!=Kale["x1"] and kordinatlar[1]==Kale["y1"]:
            Kale["x1"]=kordinatlar[0]
            break
        elif kordinatlar[0]==Kale["x1"] and kordinatlar[1]!=Kale["y1"]:
            Kale["y1"]=kordinatlar[1]
            break
        elif kordinatlar[0]!=Kale["x1"] and kordinatlar[1]!=Kale["y1"]:
            print("Kale sadece bir eksende ilerleyebilir")
            break
        else:
            print("Kale yerinde durmuştur")
            break
        print(Kale["x1"],Kale["y1"])
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

#At
At={"x2":2,
    "y2":1,
    "x7":7,
    "y7":1,
    "x58":2,
    "y58":8,
    "x63":7,
    "y63":8
    }
while True:
    deger=int(input("At2'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==(At["x2"]+1 or At["x2"]-1) and kordinatlar[1]==(At["y2"]+2 or At["y2"]-2):
            At["x2"]=kordinatlar[0]
            At["y2"]=kordinatlar[1]
            break
        elif kordinatlar[0]==(At["x2"]+2 or At["x2"]-2) and kordinatlar[1]==(At["y2"]+1 or At["y2"]-1):
            At["x2"]=kordinatlar[0]
            At["y2"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x2"] and kordinatlar[1]==At["y2"]:
            print("At yerinde kalmıştır")
            break
        else:
            print("Hareket yanlış yapılmıştır")
            break
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while True:
    deger=int(input("At7'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==(At["x7"]+1 or At["x7"]-1) and kordinatlar[1]==(At["y7"]+2 or At["y7"]-2):
            At["x7"]=kordinatlar[0]
            At["y7"]=kordinatlar[1]
            break
        elif kordinatlar[0]==(At["x7"]+2 or At["x7"]-2) and kordinatlar[1]==(At["y7"]+1 or At["y7"]-1):
            At["x7"]=kordinatlar[0]
            At["y7"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x7"] and kordinatlar[1]==At["y7"]:
            print("At yerinde kalmıştır")
            break
        else:
            print("Hareket yanlış yapılmıştır")
            break
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while True:
    deger=int(input("At58'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==(At["x58"]+1 or At["x58"]-1) and kordinatlar[1]==(At["y58"]+2 or At["y58"]-2):
            At["x58"]=kordinatlar[0]
            At["y58"]=kordinatlar[1]
            break
        elif kordinatlar[0]==(At["x58"]+2 or At["x58"]-2) and kordinatlar[1]==(At["y58"]+1 or At["y58"]-1):
            At["x58"]=kordinatlar[0]
            At["y58"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x58"] and kordinatlar[1]==At["y58"]:
            print("At yerinde kalmıştır")
            break
        else:
            print("Hareket yanlış yapılmıştır")
            break
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while True:
    deger=int(input("At63'ü nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==(At["x63"]+1 or At["x63"]-1) and kordinatlar[1]==(At["y63"]+2 or At["y63"]-2):
            At["x63"]=kordinatlar[0]
            At["y63"]=kordinatlar[1]
            break
        elif kordinatlar[0]==(At["x63"]+2 or At["x63"]-2) and kordinatlar[1]==(At["y63"]+1 or At["y63"]-1):
            At["x63"]=kordinatlar[0]
            At["y63"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x63"] and kordinatlar[1]==At["y63"]:
            print("At yerinde kalmıştır")
            break
        else:
            print("Hareket yanlış yapılmıştır")
            break
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

#Fil
Fil={"x3":3,
     "y3":1,
     "x6":6,
     "y6":1,
     "x59":3,
     "y59":8,
     "x62":6,
     "y62":8
     }
#while True:
#    deger=int(input("Fil3'ü nereye ilerletmek istiyorsunuz="))
#    kordinatlar=Kontrol(deger)
#    print(kordinatlar)
#    for i in range(9):
#        if deger==
    
    
    
#deger=input("Siyah Fil2'i nereye ilerletmek istiyorsunuz=")

#deger=input("Beyaz Fil1'i nereye ilerletmek istiyorsunuz=")
#deger=input("Beyaz Fil2'i nereye ilerletmek istiyorsunuz=")

#vezir
Vezir={"x4":4,
       "y4":1,
       "x60":4,
       "y60":8
       }
#deger=input("Siyah Vezir'i nereye ilerletmek istiyorsunuz=")

#deger=input("Beayz Vezir'i nereye ilerletmek istiyorsunuz=")

#Şah
Sah={"x5":5,
     "y5":8,
     "x61":5,
     "y61":8
     }
while True:
    deger=int(input("Şah5'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==(Sah["x5"] or Sah["x5"]+1 or Sah["x5"]-1) and kordinatlar[1]==(Sah["y5"] or Sah["y5"]+1 or Sah["y5"]-1):
            Sah["x5"]=kordinatlar[0]
            Sah["y5"]=kordinatlar[1]
            break
        else:
            print("Şah böyle ilerleyemez")
            break
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while True:
    deger=int(input("Şah61'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==(Sah["x61"] or Sah["x61"]+1 or Sah["x61"]-1) and kordinatlar[1]==(Sah["y61"] or Sah["y61"]+1 or Sah["y61"]-1):
            Sah["x61"]=kordinatlar[0]
            Sah["y61"]=kordinatlar[1]
            break
        else:
            print("Şah böyle ilerleyemez")
            break
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")




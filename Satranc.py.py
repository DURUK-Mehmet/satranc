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
    else: print("deger 0 dan büyük olmalı ")

x=8
y=8

start_index=1
end_index=x*y

deger=45
print(Kontrol(deger))


#taşlar
#Kale
SKale={"x1":1,
       "y1":1,
       "x8":8,
       "y8":1,
       "x57":1,
       "y57":8,
       "x64":8,
       "y64":8
       }
while True:#Skale57
    deger=int(input("Siyah Kale57'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    print(kordinatlar)
    if kordinatlar[0]!=SKale["x57"] and kordinatlar[1]==SKale["y57"]:
        SKale["x57"]=kordinatlar[0]
        break
    elif kordinatlar[0]==SKale["x57"] and kordinatlar[1]!=SKale["y57"]:
        SKale["y57"]=kordinatlar[1]
        break
    elif kordinatlar[0]!=SKale["x57"] and kordinatlar[1]!=SKale["y57"]:
        print("Kale sadece bir eksende ilerleyebilir")
        break
    else:
        print("Kale yerinde durmuştur")
        break
    print(SKale["x57"],SKale["y57"])
    
while True:#Skale64
    deger=int(input("Siyah Kale64'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    print(kordinatlar)
    if kordinatlar[0]!=SKale["x64"] and kordinatlar[1]==SKale["y64"]:
        SKale["x64"]=kordinatlar[0]
        break
    elif kordinatlar[0]==SKale["x64"] and kordinatlar[1]!=SKale["y64"]:
        SKale["y64"]=kordinatlar[1]
        break
    elif kordinatlar[0]!=SKale["x64"] and kordinatlar[1]!=SKale["y64"]:
        print("Kale sadece bir eksende ilerleyebilir")
        break
    else:
        print("Kale yerinde durmuştur")
        break
    print(SKale["x64"],SKale["y64"])

#deger=input("Beyaz Kale1'i nereye ilerletmek istiyorsunuz=")
#deger=input("Beyaz Kale2'i nereye ilerletmek istiyorsunuz=")
#At
SAt={"x1":2,
     "y1":8,
     "x2":7,
     "y2":8
     }
#deger=input("Siyah At1'i nereye ilerletmek istiyorsunuz=")
#deger=input("Siyah At2'i nereye ilerletmek istiyorsunuz=")

BAt={"x1":2,
     "y1":1,
     "x2":7,
     "y2":1
     }
#deger=input("Beyaz At1'i nereye ilerletmek istiyorsunuz=")
#deger=input("Beyaz At2'i nereye ilerletmek istiyorsunuz=")

#Fil
SFil={"x1":3,
      "y1":8,
      "x2":6,
      "y2":8
      }
#deger=input("Siyah Fil1'i nereye ilerletmek istiyorsunuz=")
#deger=input("Siyah Fil2'i nereye ilerletmek istiyorsunuz=")

BFil={"x1":3,
      "y1":1,
      "x2":6,
      "y2":1
      }
#deger=input("Beyaz Fil1'i nereye ilerletmek istiyorsunuz=")
#deger=input("Beyaz Fil2'i nereye ilerletmek istiyorsunuz=")

#vezir
SVezir={"x":4,
        "y":8
        }
#deger=input("Siyah Vezir'i nereye ilerletmek istiyorsunuz=")

BVezir={"x":4,
        "y":1
        }
#deger=input("Beayz Vezir'i nereye ilerletmek istiyorsunuz=")
#Şah
SSah={"x":5,
      "y":8
      }
#deger=input("Siyah Şah'ı nereye ilerletmek istiyorsunuz=")

BSah={"x":5,
      "y":1
      }
#deger=input("Beyaz Şah'ı nereye ilerletmek istiyorsunuz=")




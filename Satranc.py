def Kontrol(deger):
    if 65>deger>0:
        if deger%8==0:
            x_point=8
            y_point=int(deger/8)
        else: 
            x_point=deger%8
            y_point=int(deger/8)+1
        kordinatlar=[x_point,y_point]
        return kordinatlar
    else: 
        kordinatlar=[0,0]
        return kordinatlar

def filKordinat(deger,degerFil,x):
    if deger==(degerFil+(7*x)) or deger==(degerFil-(7*x)) or deger==(degerFil+(9*x)) or deger==(degerFil-(9*x)):
        return True
    else:
        return False

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
while False:#kale57
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
            print("Lütfen yeniden ve doğru değer giriniz")
        else:
            print("Kale yerinde durmuştur")
            break
        print(Kale["x57"],Kale["y57"])
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:#kale64
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
            print("Lütfen yeniden ve doğru değer giriniz")
        else:
            print("Kale yerinde durmuştur")
            break
        print(Kale["x64"],Kale["y64"])
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:#kale8
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
            print("Lütfen yeniden ve doğru değer giriniz")
        else:
            print("Kale yerinde durmuştur")
            break
        print(Kale["x8"],Kale["y8"])
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
    
while False:#kale1
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
            print("Lütfen yeniden ve doğru değer giriniz")
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
while False:
    deger=int(input("At2'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==At["x2"]+1 or kordinatlar[0]==At["x2"]-1 and kordinatlar[1]==At["y2"]+2 or kordinatlar[1]==At["y2"]-2:
            At["x2"]=kordinatlar[0]
            At["y2"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x2"]+2 or kordinatlar[0]==At["x2"]-2 and kordinatlar[1]==At["y2"]+1 or kordinatlar[1]==At["y2"]-1:
            At["x2"]=kordinatlar[0]
            At["y2"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x2"] and kordinatlar[1]==At["y2"]:
            print("At yerinde kalmıştır")
            break
        else:
            print("Hareket yanlış yapılmıştır")
            print("Lütfen yeniden ve doğru değer giriniz")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("At7'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==At["x7"]+1 or kordinatlar[0]==At["x7"]-1 and kordinatlar[1]==At["y7"]+2 or kordinatlar[1]==At["y7"]-2:
            At["x7"]=kordinatlar[0]
            At["y7"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x7"]+2 or kordinatlar[0]==At["x7"]-2 and kordinatlar[1]==At["y7"]+1 or kordinatlar[1]==At["y7"]-1:
            At["x7"]=kordinatlar[0]
            At["y7"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x7"] and kordinatlar[1]==At["y7"]:
            print("At yerinde kalmıştır")
            break
        else:
            print("Hareket yanlış yapılmıştır")
            print("Lütfen yeniden ve doğru değer giriniz")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("At58'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==At["x58"]+1 or kordinatlar[0]==At["x58"]-1 and kordinatlar[1]==At["y58"]+2 or kordinatlar[1]==At["y58"]-2:
            At["x58"]=kordinatlar[0]
            At["y58"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x58"]+2 or kordinatlar[0]==At["x58"]-2 and kordinatlar[1]==At["y58"]+1 or kordinatlar[1]==At["y58"]-1:
            At["x58"]=kordinatlar[0]
            At["y58"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x58"] and kordinatlar[1]==At["y58"]:
            print("At yerinde kalmıştır")
            break
        else:
            print("Hareket yanlış yapılmıştır")
            print("Lütfen yeniden ve doğru değer giriniz")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("At63'ü nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==At["x63"]+1 or kordinatlar[0]==At["x63"]-1 and kordinatlar[1]==At["y63"]+2 or kordinatlar[1]==At["y63"]-2:
            At["x63"]=kordinatlar[0]
            At["y63"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x63"]+2 or kordinatlar[0]==At["x63"]-2 and kordinatlar[1]==At["y63"]+1 or kordinatlar[1]==At["y63"]-1:
            At["x63"]=kordinatlar[0]
            At["y63"]=kordinatlar[1]
            break
        elif kordinatlar[0]==At["x63"] and kordinatlar[1]==At["y63"]:
            print("At yerinde kalmıştır")
            break
        else:
            print("Hareket yanlış yapılmıştır")
            print("Lütfen yeniden ve doğru değer giriniz")
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
degerFil=[3,6,59,62]
islem=True
while islem:
    deger=int(input("Fil3'ü nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    print(degerFil[0],Fil["x3"],Fil["y3"])
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        for i in range(7):
            durum=filKordinat(deger, degerFil[0], i)
            if durum==True:
                degerFil[0]=deger
                Fil["x3"]=kordinatlar[0]
                Fil["y3"]=kordinatlar[1]
                print("Hareket doğru yapıldı")
                break
            elif i==6 and durum==False:
                print("hareket yanlış yapılmıştır")
                break
    else: 
        print("Verilen değer yanlıştır lütfen tekrar giriniz")
        
while False:
    deger=int(input("Fil6'ı nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[1]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        for i in range(1,10):
           for i in range(7):
               durum=filKordinat(deger, degerFil[1],i)
               if durum==True:
                   degerFil[1]=deger
                   Fil["x6"]=kordinatlar[0]
                   Fil["y6"]=kordinatlar[1]
                   print("Hareket doğru yapıldı")
                   break
               elif i==6 and durum==False:
                   print("hareket yanlış yapılmıştır")
                   break
               else: print("hata")
    else: 
        print("Verilen değer yanlıştır lütfen tekrar giriniz")
        

"""while False:
    deger=int(input("Fil6'ı nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[1]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        for i in range(1,10):
           if deger==degerFil[1]+(i*7) or deger==degerFil[1]-(i*7):
               degerFil[1]=deger
               Fil["x6"]=kordinatlar[0]
               Fil["y6"]=kordinatlar[1]
               break
           elif deger==degerFil[1]+(i*9) or deger==degerFil[1]-(i*9):
               degerFil[1]=deger
               Fil["x6"]=kordinatlar[0]
               Fil["y6"]=kordinatlar[1]
               break
           else: 
               print("Hareket yanlış yapılmışıtr") 
               print("Lütfen yeniden ve doğru değer giriniz")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")"""


while False:
    deger=int(input("Fil59'u nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        for i in range(7):
            durum=filKordinat(deger, degerFil[2],i)
            if durum==True:
                degerFil[2]=deger
                Fil["x59"]=kordinatlar[0]
                Fil["y59"]=kordinatlar[1]
                print("Hareket doğru yapıldı")
                break
            elif i==6 and durum==False:
                print("hareket yanlış yapılmıştır")
                break
            else: print("hata")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("Fil62'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        for i in range(7):
            durum=filKordinat(deger, degerFil[3],i)
            if durum==True:
                degerFil[3]=deger
                Fil["x62"]=kordinatlar[0]
                Fil["y62"]=kordinatlar[1]
                print("Hareket doğru yapıldı")
                break
            elif i==6 and durum==False:
                print("hareket yanlış yapılmıştır")
                break
            else: print("hata")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
    
#vezir
Vezir={"x4":4,
       "y4":1,
       "x60":4,
       "y60":8
       }
degerVezir=[4,60]
yediler=[7,14,21,28,35,42,49]
dokuzlar=[9,18,27,36,45,54,63]
while False:
    deger=int(input("Vezir4'ü nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]!=Vezir["x4"] and kordinatlar[1]==Vezir["y4"]:
            degerVezir[0]=deger
            Vezir["x4"]=kordinatlar[0]
            break
        elif kordinatlar[0]==Vezir["x4"] and kordinatlar[1]!=Vezir["y4"]:
            Vezir["y4"]=kordinatlar[1]
            degerVezir[0]=deger
            break
        elif kordinatlar[0]!=Vezir["x4"] and kordinatlar[1]!=Vezir["y4"]:
            for i in range(7):
                durum=filKordinat(deger, degerVezir[0],i)
                if durum==True:
                    degerVezir[0]=deger
                    Vezir["x4"]=kordinatlar[0]
                    Vezir["y4"]=kordinatlar[1]
                    print("Hareket doğru yapıldı")
                    break
                elif i==6 and durum==False:
                    print("hareket yanlış yapılmıştır")
                    break
                else: print("hata")
        else:
            print("Vezir yerinde durmuştur")
            break
        print(Vezir["x4"],Vezir["y4"])
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("Vezir60'ı nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]!=Vezir["x60"] and kordinatlar[1]==Vezir["y60"]:
            degerVezir[1]=deger
            Vezir["x60"]=kordinatlar[0]
            break
        elif kordinatlar[0]==Vezir["x60"] and kordinatlar[1]!=Vezir["y60"]:
            Vezir["y60"]=kordinatlar[1]
            degerVezir[1]=deger
            break
        elif kordinatlar[0]!=Vezir["x60"] and kordinatlar[1]!=Vezir["y60"]:
            for i in range(7):
                durum=filKordinat(deger, degerVezir[1],i)
                if durum==True:
                    degerVezir[1]=deger
                    Vezir["x60"]=kordinatlar[0]
                    Vezir["y60"]=kordinatlar[1]
                    print("Hareket doğru yapıldı")
                    break
                elif i==6 and durum==False:
                    print("hareket yanlış yapılmıştır")
                    break
                else: print("hata")
        else:
            print("Vezir yerinde durmuştur")
            break
        print(Vezir["x60"],Vezir["y60"])
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
  

#Şah
Sah={"x5":5,
     "y5":1,
     "x61":5,
     "y61":8
     }
while False:
    deger=int(input("Şah5'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==Sah["x5"] or kordinatlar[0]==Sah["x5"]+1 or kordinatlar[0]==Sah["x5"]-1 and kordinatlar[1]==Sah["y5"] or kordinatlar[1]==Sah["y5"]+1 or kordinatlar[1]==Sah["y5"]-1:
            Sah["x5"]=kordinatlar[0]
            Sah["y5"]=kordinatlar[1]
            break
        else:
            print("Şah böyle ilerleyemez")
            print("Lütfen yeniden ve doğru değer giriniz")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("Şah61'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Kontrol(deger)
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        if kordinatlar[0]==Sah["x61"] or kordinatlar[0]==Sah["x61"]+1 or kordinatlar[0]==Sah["x61"]-1 and kordinatlar[1]==Sah["y61"] or kordinatlar[1]==Sah["y61"]+1 or kordinatlar[1]==Sah["y61"]-1:
            Sah["x61"]=kordinatlar[0]
            Sah["y61"]=kordinatlar[1]
            break
        else:
            print("Şah böyle ilerleyemez")
            print("Lütfen yeniden ve doğru değer giriniz")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")




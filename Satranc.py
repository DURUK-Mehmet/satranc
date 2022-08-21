def Control(deger):
    if 64>=deger>=1:
        if deger%8==0:
            x_point=8
            y_point=int(deger/8)
        else: 
            x_point=deger%8
            y_point=int(deger/8)+1
        return [x_point,y_point]
    else: 
        return [0,0]

def CrossCoordinate(x_point,y_point,x,y,i):
    if x_point==(x+i) and y_point==(y+i):
        return True
    elif x_point==(x+i) and y_point==(y-i):
        return True
    elif x_point==(x-i) and y_point==(y+i):
        return True
    elif x_point==(x-i) and y_point==(y-i):
        return True
    else:
        return False
    
def FlatCoordinate(x_point,y_point,x,y):
    if x_point!=x and y_point==y:
        return True
    elif x_point==x and y_point!=y:
        return True
    elif x_point==x and y_point==y:
        return True
    else:
        return False
    
def KingCoordinate(x_point,y_point,x,y):
    if (x_point==x or x_point==x+1 or x_point==x-1) and (y_point==y or y_point==y+1 or y_point==y-1):
        return True
    else:
        return False
    
def LCoordinate(x_point,y_point,x,y):
    if (x_point==x+1 or x_point==x-1) and (y_point==y+2 or y_point==y-2):
        return True
    elif (x_point==x+2 or x_point==x-2) and (y_point==y+1 or y_point==y-1):
        return True
    elif (x_point==x) and (y_point==y):
        return True
    else:
        return False
    
x=8
y=8
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
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=flatCoordinate(kordinatlar[0],kordinatlar[1], Kale["x57"], Kale["y57"])
        if durum==True:
            Kale["x57"]=kordinatlar[0]
            Kale["y57"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Kale["x57"],Kale["y57"]))
            break
        elif durum==False:
            print("Kale böyle hareket edemez,kordinatlar:{}-{}".format(Kale["x57"],Kale["y57"]))
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
    
while False:#kale64
    deger=int(input("Kale64'ü nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=flatCoordinate(kordinatlar[0],kordinatlar[1], Kale["x64"], Kale["y64"])
        if durum==True:
            Kale["x64"]=kordinatlar[0]
            Kale["y64"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Kale["x64"],Kale["y64"]))
            break
        elif durum==False:
            print("Kale böyle hareket edemez,kordinatlar:{}-{}".format(Kale["x64"],Kale["y64"]))
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:#kale8
    deger=int(input("Kale8'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=flatCoordinate(kordinatlar[0],kordinatlar[1], Kale["x8"], Kale["y8"])
        if durum==True:
            Kale["x8"]=kordinatlar[0]
            Kale["y8"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Kale["x8"],Kale["y8"]))
            break
        elif durum==False:
            print("Kale böyle hareket edemez,kordinatlar:{}-{}".format(Kale["x8"],Kale["y8"]))
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
    
while False:#kale1
    deger=int(input("Kale1'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=flatCoordinate(kordinatlar[0],kordinatlar[1], Kale["x1"], Kale["y1"])
        if durum==True:
            Kale["x1"]=kordinatlar[0]
            Kale["y1"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Kale["x1"],Kale["y1"]))
            break
        elif durum==False:
            print("Kale böyle hareket edemez,kordinatlar:{}-{}".format(Kale["x1"],Kale["y1"]))
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
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=LCoordinate(kordinatlar[0], kordinatlar[1], At["x2"], At["y2"])
        if durum==True:
            At["x2"]=kordinatlar[0]
            At["y2"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(At["x2"],At["y2"]))
            break
        else:print("Hareket yanlış yapıldı, yeni kordinatlar:{}-{}".format(At["x2"],At["y2"]))
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("At7'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=LCoordinate(kordinatlar[0], kordinatlar[1], At["x7"], At["y7"])
        if durum==True:
            At["x7"]=kordinatlar[0]
            At["y7"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(At["x7"],At["y7"]))
            break
        else:print("Hareket yanlış yapıldı, yeni kordinatlar:{}-{}".format(At["x7"],At["y7"]))
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("At58'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=LCoordinate(kordinatlar[0], kordinatlar[1], At["x58"], At["y58"])
        if durum==True:
            At["x58"]=kordinatlar[0]
            At["y58"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(At["x58"],At["y58"]))
            break
        else:print("Hareket yanlış yapıldı, yeni kordinatlar:{}-{}".format(At["x58"],At["y58"]))
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("At63'ü nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=LCoordinate(kordinatlar[0], kordinatlar[1], At["x63"], At["y63"])
        if durum==True:
            At["x63"]=kordinatlar[0]
            At["y63"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(At["x63"],At["y63"]))
            break
        else:print("Hareket yanlış yapıldı, yeni kordinatlar:{}-{}".format(At["x63"],At["y63"]))
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

while False:
    deger=int(input("Fil3'ü nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        for i in range(1,9):
            durum=crossCoordinate(kordinatlar[0],kordinatlar[1],Fil["x3"],Fil["y3"],i)
            if durum==True:
                Fil["x3"]=kordinatlar[0]
                Fil["y3"]=kordinatlar[1]
                print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Fil["x3"],Fil["y3"]))
                break
            elif i==6 and durum==False:
                print("hareket yanlış yapılmıştır,kordinatlar:{}-{}".format(Fil["x3"],Fil["y3"]))
            else: print("hata")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
        
while False:
    deger=int(input("Fil6'ı nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[1]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        for i in range(1,9):
            durum=crossCoordinate(kordinatlar[0],kordinatlar[1],Fil["x6"],Fil["y6"],i)
            if durum==True:
                Fil["x6"]=kordinatlar[0]
                Fil["y6"]=kordinatlar[1]
                print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Fil["x6"],Fil["y6"]))
                break
            elif i==6 and durum==False:
                print("hareket yanlış yapılmıştır,kordinatlar:{}-{}".format(Fil["x6"],Fil["y6"]))
            else: print("hata")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
        
while False:
    deger=int(input("Fil59'u nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        for i in range(1,9):
            durum=crossCoordinate(kordinatlar[0],kordinatlar[1],Fil["x59"],Fil["y59"],i)
            if durum==True:
                Fil["x59"]=kordinatlar[0]
                Fil["y59"]=kordinatlar[1]
                print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Fil["x59"],Fil["y59"]))
                break
            elif i==6 and durum==False:
                print("hareket yanlış yapılmıştır,kordinatlar:{}-{}".format(Fil["x59"],Fil["y59"]))
            else: print("hata")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("Fil62'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        print(kordinatlar)
        for i in range(1,9):
            durum=crossCoordinate(kordinatlar[0],kordinatlar[1],Fil["x62"],Fil["y62"],i)
            if durum==True:
                Fil["x62"]=kordinatlar[0]
                Fil["y62"]=kordinatlar[1]
                print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Fil["x62"],Fil["y62"]))
                break
            elif i==6 and durum==False:
                print("hareket yanlış yapılmıştır,kordinatlar:{}-{}".format(Fil["x62"],Fil["y62"]))
            else: print("hata")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
    
#vezir
Vezir={"x4":4,
       "y4":1,
       "x60":4,
       "y60":8
       }
while False:
    deger=int(input("Vezir4'ü nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=flatCoordinate(kordinatlar[0],kordinatlar[1], Vezir["x4"], Vezir["y4"])
        if durum==True:
            Vezir["x4"]=kordinatlar[0]
            Vezir["y4"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format( Vezir["x4"], Vezir["y4"]))
            break
        elif durum==False:
            for i in range(1,9):
                durum=crossCoordinate(kordinatlar[0],kordinatlar[1], Vezir["x4"],Vezir["y4"],i)
                if durum==True:
                    Vezir["x4"]=kordinatlar[0]
                    Vezir["y4"]=kordinatlar[1]
                    print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format( Vezir["x4"], Vezir["y4"]))
                    break
                elif i==6 and durum==False:
                    print("hareket yanlış yapılmıştır,kordinatlar:{}-{}".format(Fil["x4"],Fil["y4"]))
                else: print("hata")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("Vezir60'ı nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
       durum=flatCoordinate(kordinatlar[0],kordinatlar[1], Vezir["x60"], Vezir["y60"])
       if durum==True:
           Vezir["x60"]=kordinatlar[0]
           Vezir["y60"]=kordinatlar[1]
           print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format( Vezir["x60"], Vezir["y60"]))
           break
       elif durum==False:
            for i in range(1,9):
                durum=crossCoordinate(kordinatlar[0],kordinatlar[1], Vezir["x60"],Vezir["y60"],i)
                if durum==True:
                    Vezir["x60"]=kordinatlar[0]
                    Vezir["y60"]=kordinatlar[1]
                    print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format( Vezir["x60"], Vezir["y60"]))
                    break
                elif i==6 and durum==False:
                    print("hareket yanlış yapılmıştır,kordinatlar:{}-{}".format(Fil["x60"],Fil["y60"]))
                else: print("hata")
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")
  
#Şah
Sah={"x5":5,
     "y5":1,
     "x61":5,
     "y61":8
     }
while False:
    deger=int(input("Şah5'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=kingCoordinate(kordinatlar[0],kordinatlar[1],Sah["x5"],Sah["y5"])
        if durum==True:
            Sah["x5"]=kordinatlar[0]
            Sah["y5"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Sah["x5"],Sah["y5"]))
            break
        else:print("hareket yanlış yapılmıştır,kordinatlar:{}-{}".format(Sah["x5"],Sah["y5"]))
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")

while False:
    deger=int(input("Şah61'i nereye ilerletmek istiyorsunuz="))
    kordinatlar=Control(deger)
    print("girilen kordinatlar:{}".format(kordinatlar))
    if kordinatlar[0]!=0 and kordinatlar[1]!=0:
        durum=kingCoordinate(kordinatlar[0],kordinatlar[1],Sah["x61"],Sah["y61"])
        if durum==True:
            Sah["x5"]=kordinatlar[0]
            Sah["y5"]=kordinatlar[1]
            print("Hareket doğru yapıldı, yeni kordinatlar:{}-{}".format(Sah["x61"],Sah["y61"]))
            break
        else:print("hareket yanlış yapılmıştır,kordinatlar:{}-{}".format(Sah["x61"],Sah["y61"]))
    else: print("Verilen değer yanlıştır lütfen tekrar giriniz")




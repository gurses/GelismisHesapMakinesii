import math
import time


def BirBilinmeyenliDenklem(a,b):
    sonuc = -b/a
    print("SONUÇ = {}x+{}=0 --> x={}".format(a,b,sonuc))


def IkıBilinmeyenliDenklem(a,b,c):
    D = (b**2)-(4*(a*c))
    if(D > 0):
        x2 = (-b + (D**0.5)) /(2*a)
        x1= (-b - (D**0.5)) /(2*a)

        print("BİRİNCİ KÖK = {}   IKINCI KÖK = {}".format(x1,x2))

    elif(D==0):
        x1= -b/(2*a)
        x2=x1

        print("BİRİNCİ KÖK = {}    IKINCI KÖK = {}".format(x1,x2))


    elif(D < 0 ):
        print("KÖKÜ YOKTUR...")


print(""""************************************************************


                 HESAP MAKİNESİ


************************************************************""")

print("""

              ------İŞLEMLER------

1 -> TOPLAMA
2 -> ÇIKARMA
3 -> BÖLME
4 -> ÇARPMA
5 -> LOGARITMA
6 -> FAKTORIYEL
7 -> KAREKÖK
8 -> COS()
9 -> SIN()
10-> TAN()
11-> USLU SAYI BUL
12-> HIPOTENUS BULMA
13-> ARCTAN()
14-> BİRİNCİ DERECEDEN BİR BİLİNMEYENLİ DENK.
15-> İKİNCİ DERECEDEN BİR BİLİNMEYENLİ DENK.
16-> BELİRLİ İNTEGRAL HESAPLA

************************************************************

""")


seçim=int(input("LÜTFEN İŞLEM SEÇİMİNİ YAP:"))

print("""
------------------------------------------------------
""")

if(seçim==1):
    sayi1 = int(input("LÜTFEN BİRİNCİ SAYİYİ GİR:"))
    sayi2 = int(input("LÜTFEN İKİNCİ SAYİYİ GİR:"))

    print("TOPLAMA İŞLEMİ YAPILIYOR...")
    time.sleep(1)
    print("{} + {} = {}".format(sayi1,sayi2,sayi1+sayi2))

elif(seçim==2):
    sayi1 = int(input("LÜTFEN BİRİNCİ SAYİYİ GİR:"))
    sayi2 = int(input("LÜTFEN İKİNCİ SAYİYİ GİR:"))

    print("ÇIKARMA İŞLEMİ YAPILIYOR...")
    time.sleep(1)
    print("{} - {} = {}".format(sayi1,sayi2,sayi1-sayi2))

elif(seçim==3):
    sayi1 = int(input("LÜTFEN BİRİNCİ SAYİYİ GİR:"))
    sayi2 = int(input("LÜTFEN İKİNCİ SAYİYİ GİR:"))

    print("BÖLME İŞLEMİ YAPILIYOR...")
    time.sleep(1)
    print("{} / {} = {}".format(sayi1,sayi2,sayi1/sayi2))

elif(seçim==4):
    sayi1 = int(input("LÜTFEN BİRİNCİ SAYİYİ GİR:"))
    sayi2 = int(input("LÜTFEN İKİNCİ SAYİYİ GİR:"))

    print("ÇARPMA İŞLEMİ YAPILIYOR...")
    time.sleep(1)
    print("{} x {} = {}".format(sayi1,sayi2,sayi1*sayi2))

elif (seçim==5):
    taban=int(input("TABAN SAYISINI GİR:"))
    x = int(input("{} TABANINDA ALMAK İSTEDİĞİN SAYIYI GİR:".format(taban)))
    print("LOGARİTMASI ALINIYOR...")
    time.sleep(1)
    print("IŞLEMİN SONUCU =",math.log(taban,x))

elif (seçim==6):
    sayi=int(input("FAKTORİYELİNİ İSTEDİĞİN SAYİYİ GİR:"))
    print("{}! FAKTORİYEL ALINIYOR...".format(sayi))
    time.sleep(1)
    print("{}! SONUCU =".format(sayi),math.factorial(sayi))

elif(seçim==7):
    sayi=int(input("KAREKÖKÜNÜ ALMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ:"))
    print("'{}' KAREKÖKÜ ALINIYOR...".format(sayi))
    time.sleep(1)
    print("IŞLEMİN SONUCU =",sayi**0.5)

elif(seçim==8):
    sayi=int(input(("COS NÜ ALMAK İSTEDİĞİN AÇIYI GİR:")))
    print("'{}' COS Ü ALINIYOR...".format(sayi))
    time.sleep(1)
    print("IŞLEMİN SONUCU =",math.cos(sayi))

elif(seçim==9):
    sayi=int(input((" SIN NÜ ALMAK İSTEDİĞİN AÇIYI GİR:")))
    print("'{}' SIN Ü ALINIYOR...".format(sayi))
    time.sleep(1)
    print("IŞLEMİN SONUCU =",math.sin(sayi))

elif(seçim==10):
    sayi=int(input(("TAN NI ALMAK İSTEDİĞİN AÇIYI GİR:")))
    print("'{}' TAN I ALINIYOR...".format(sayi))
    time.sleep(1)
    print("IŞLEMİN SONUCU =",math.tan(sayi))

elif(seçim==11):
    taban=int(input("LÜTFEN TABANI GİR:"))
    üs=int(input("LÜTFEN ÜSSÜ GİR:"))
    print("{} ÜZERİ {} HESAPLANIYOR...".format(taban,üs))
    time.sleep(1)
    print("{} ÜZERİ {} = {}".format(taban,üs,taban**üs))


elif(seçim==12):
    açı1=int(input("BIRINCI KENARI GIR:"))
    açı2=int(input("IKINCI KENARI GİR:"))
    print("HESAPLANIYOR...")
    time.sleep(1)
    print("UCUNCU KENAR=",math.hypot(açı1,açı2))


elif(seçim==13):
    sayi = int(input(("ARCTAN NÜ ALMAK İSTEDİĞİN AÇIYI GİR:")))
    print("'{}' ARCTAN I ALINIYOR...".format(sayi))
    time.sleep(1)
    print("IŞLEMİN SONUCU =",math.atan(sayi))

elif(seçim==14):
    a=int(input("ax+b=0 --> a yı gir:"))
    b=int(input("ax+b=0 --> b yi gir:"))
    print("SONUÇ HESAPLANIYOR...")
    time.sleep(1)
    BirBilinmeyenliDenklem(a,b)

elif(seçim==15):
    a = int(input("ax^2+bx+c=0 --> a yı gir:"))
    b = int(input("ax^2+bx+c=0 --> b yi gir:"))
    c = int(input("ax^2+bx+c=0 --> c yi gir:"))

    print("SONUÇ HESAPLANIYOR...")
    time.sleep(1)
    IkıBilinmeyenliDenklem(a,b,c)

elif(seçim==16):

    üstdeğer = int(input("İNTEGRAL ÜST DEĞERİ GİR:"))
    altdeğer = int(input("İNTEGRAL ALT DEĞERİ GİR:"))

    print(" 'x' SAYISININ SAYISINI GİR:")
    print("""

                 -----İŞLEMLER-----
            İŞLEM YAPACAĞINIZ ŞEKLİ SEÇİN
                 
     1 ---> (∫ax)
     2 ---> (∫ax1+bx2)
     3 ---> (∫ax1+bx2+cx3)
     4 ---> (∫ax1+bx2+cx3+dx4)


     """)

    seçenek = int(input("İŞLEMİNİ SEÇ:"))

    if (seçenek == 1):

        a = int(input("a DEĞERİNİ GİR:"))
        n = int(input("x^n --> n DEĞERİNİ GİR:"))


        sonuc = (((a * (üstdeğer ** (n + 1))) / (n + 1)) - ((a * (altdeğer ** (n + 1))) / (n + 1)))

        print("""
        
        YAPTIĞINIZ İŞLEM ŞU ŞEKİLDE = altdeğer ={} üst değer ={} ∫{}x^{} dx)
        
        """.format(altdeğer,üstdeğer,a,n))

        print("SONUÇ HESAPLANIYOR...")

        time.sleep(2)

        print("SONUÇ = {} + c".format(sonuc))

    elif(seçenek==2):

        a = int(input("a DEĞERİNİ GİR:"))
        n1 = int(input("x1^n --> n DEĞERİNİ GİR:"))
        b = int(input("b DEĞERİNİ GİR:"))
        n2 = int(input("x2^n --> n DEĞERİNİ GİR:"))

        sonuc = ((((a * (üstdeğer ** (n1 + 1))) / (n1 + 1))

                    + ((b * (üstdeğer ** (n2 + 1))) / (n2 + 1)))


                    - (((a * (altdeğer ** (n1 + 1))) / (n1 + 1))

                    + ((b * (altdeğer ** (n2 + 1))) / (n2 + 1))))

        print("""

               YAPTIĞINIZ İŞLEM ŞU ŞEKİLDE = altdeğer ={} üst değer ={} ∫{}x^{}(+/-){}x^{} dx)

               """.format(altdeğer, üstdeğer, a, n1,b,n2))

        print("SONUÇ HESAPLANIYOR...")
        time.sleep(2)
        print("SONUÇ = {} + c".format(sonuc))

    elif(seçenek == 3):
        a  = int(input("a DEĞERİNİ GİR:"))
        n1 = int(input("x1^n --> n DEĞERİNİ GİR:"))
        b  = int(input("b DEĞERİNİ GİR:"))
        n2 = int(input("x2^n --> n DEĞERİNİ GİR:"))
        c  = int(input("c DEĞERİNİ GİR:"))
        n3 = int(input("x3^n --> n DEĞERİNİ GİR:"))

        sonuc = ((((a * (üstdeğer ** (n1 + 1))) / (n1 + 1))

                    + ((b * (üstdeğer ** (n2 + 1))) / (n2 + 1))

                    + ((c * (üstdeğer ** (n3 + 1))) / (n3 + 1)))


                    - (((a * (altdeğer ** (n1 + 1))) / (n1 + 1))

                    + ((b * (altdeğer ** (n2 + 1))) / (n2 + 1))

                    + ((c * (altdeğer ** (n3 + 1))) / (n3 + 1))))

        print("""

                      YAPTIĞINIZ İŞLEM ŞU ŞEKİLDE = altdeğer ={} üst değer ={} ∫{}x^{}(+/-){}x^{}(+/-){}x^{} dx)

                      """.format(altdeğer,üstdeğer,a,n1,b,n2,c,n3))

        print("SONUÇ HESAPLANIYOR...")
        time.sleep(2)
        print("SONUÇ = {} + c".format(sonuc))

    elif(seçenek==4):
        a = int(input("a DEĞERİNİ GİR:"))
        n1 = int(input("x1^n --> n DEĞERİNİ GİR:"))
        b = int(input("b DEĞERİNİ GİR:"))
        n2 = int(input("x2^n --> n DEĞERİNİ GİR:"))
        c = int(input("c DEĞERİNİ GİR:"))
        n3 = int(input("x3^n --> n DEĞERİNİ GİR:"))
        d = int(input("d DEĞERİNİ GİR:"))
        n4 = int(input("x4^n --> n DEĞERİNİ GİR:"))

        sonuc = ((((a * (üstdeğer ** (n1 + 1))) / (n1 + 1))

                    + ((b * (üstdeğer ** (n2 + 1))) / (n2 + 1))

                    + ((c * (üstdeğer ** (n3 + 1))) / (n3 + 1))

                    + ((d * (üstdeğer ** (n4 + 1))) / (n4 + 1)))



                    - (((a * (altdeğer ** (n1 + 1))) / (n1 + 1))

                    + ((b * (altdeğer ** (n2 + 1))) / (n2 + 1))

                    + ((c * (altdeğer ** (n3 + 1))) / (n3 + 1))

                    +((d * (altdeğer ** (n4 + 1))) / (n4 + 1))))

        print("""

                YAPTIĞINIZ İŞLEM ŞU ŞEKİLDE = altdeğer ={} üst değer ={} ∫{}x^{}(+/-){}x^{}(+/-){}x^{}(+/-){}x^{} dx)

                              """.format(altdeğer,üstdeğer,a,n1,b,n2,c,n3,d,n4))

        print("SONUÇ HESAPLANIYOR...")
        time.sleep(2)
        print("SONUÇ = {} + c".format(sonuc))





else:
    print("""
     
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
             HATALI İŞLEM YAPTINIZ!!
             
                BİR DAHA DENEYİN..
    
     """)





















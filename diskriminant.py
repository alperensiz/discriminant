
print("██████╗ ██╗███████╗██╗  ██╗██████╗ ██╗███╗   ███╗██╗███╗   ██╗ █████╗ ███╗   ██╗████████╗")
print("██╔══██╗██║██╔════╝██║ ██╔╝██╔══██╗██║████╗ ████║██║████╗  ██║██╔══██╗████╗  ██║╚══██╔══╝")
print("██║  ██║██║███████╗█████╔╝ ██████╔╝██║██╔████╔██║██║██╔██╗ ██║███████║██╔██╗ ██║   ██║")   
print("██║  ██║██║╚════██║██╔═██╗ ██╔══██╗██║██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║╚██╗██║   ██║")   
print("██████╔╝██║███████║██║  ██╗██║  ██║██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║██║ ╚████║   ██║")   
print("╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝")
print("=======================================================================================")
print("=======================================================================================")
a1=int(input("ax²+bx+c=0 ifadesi için a değerini giriniz: "))
b1=int(input("ax²+bx+c=0 ifadesi için b değerini giriniz: "))                          
c1=int(input("ax²+bx+c=0 ifadesi için c değerini giriniz: "))


ilkd=int(pow(b1,2))
ikd=int(4*(a1*c1))
delta=ilkd-ikd
print("Δ'nız şuan",delta)

onayz=int(input("Kökleri bulmak için 3'e bas | x1+x2 veya x1.x2 için 4'e bas: "))
if onayz==3:
    if delta>0:
        print("Farklı 2 reel kök vardır")
        onay=(int(input("Kökleri bulmak için 1'e bas: ")))                         #made by alperen g
        if onay==1:
            kökz=int(1/2)
            kök1=int(-b1)+(delta**kökz)
            kök2=int(-b1)-(delta**kökz)
            print("x1=",kök1,"x2=",kök2,"dir")

    if delta==0:
        print("Çakışık,aynı 2 reel kök vardır")
        onay=(int(input("Kökü bulmak için 1'e bas: ")))                                        
        if onay==1:
            kökz=2*a1
            kök0=int(-b1/kökz)
            print("x1=x2",kök0,"dir")

    if delta<0:
        print("Denklemin gerçek kökü yok :/")
        

if onayz==4:
    topl=int(-b1/a1)
    çar=int(c1/a1)
    print("x1+x2= ",topl,"ve x1.x2 ise ",çar,"'dır")
    

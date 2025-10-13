#Izbornik za kalkulator

while True:
    print("izbornik")
    print("----------------------")
    print("1. Izračun V u mV")
    print("----------------------")
    print("2. Izračun Ω u kΩ")
    print("----------------------")
    print("3. Izračun A u mA")
    print("----------------------")
    print("0. Prekid programa")
    print("-----------------------")
    try:
        opcija=int(input("Izaberite operaciju (1/2/3/0): "))
    except Exception as greska:
        print("pogrešan unos...",greska)
        continue

    #Struktura grananja


        #volti

    if opcija == 1:    
        print("izračun volta u milivolte")
        volt=float(input("Upisi vrijednost u voltima: "))
        milivolt=volt*1000
        print("vrijednost u milivoltima je ",milivolt,"mV")

        #ohmi

    elif opcija == 2:
        print("Izračun ohma u kiloohme")
        ohm=float(input("Upisi vrijednost u ohmima: "))
        kiloohm=ohm/1000
        print("vrijednost u KΩ je",kiloohm,"KΩ")

        #amperi

    elif opcija == 3:
        print("izračun ampera u miliampere")
        amper=float(input("upisi vrijednost u amperima: "))
        miliamper=amper*1000
        print("vrijednost u mA je ",miliamper,"mA")

        #prekid

    elif opcija == 0:
        print("prekid programa, doviđenja ;)")
        break

        #nevažeća vrijednost
    else:
      print("ne prepoznajem, upisite važeću vrijednost")

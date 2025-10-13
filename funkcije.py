#Izbornik za kalkulator

def ispisi_izbornik():
    print("izbornik")
    print("----------------------")
    print("1. Izračun V u mV")
    print("----------------------")
    print("2. Izračun Ω u kΩ")
    print("----------------------")
    print("3. Izračun A u mA")
    print("----------------------")
    print("0. Prekid programa")
    print("----------------------")

def pretvori_V_u_mV():
    # Ovdje dolazi kod za pretvorbu volti
      if opcija == 1:    
        try:
            print("izračun volta u milivolte")
            volt=float(input("Upisi vrijednost u voltima: "))
            milivolt=volt*1000
            print("vrijednost u milivoltima je ",milivolt,"mV")
        except ValueError:
             print("GREŠKA: Unesena vrijednost nije ispravan broj.")

while True:
    ispisi_izbornik()
    #Unos opcije

    try:
        opcija=int(input("Izaberite operaciju (1/2/3/0): "))
    except Exception as greska:
        print("pogrešan unos...",greska)
        continue

    



  


        

    elif opcija == 2:
        try:
            print("Izračun ohma u kiloohme")
            ohm=float(input("Upisi vrijednost u ohmima: "))
            kiloohm=ohm/1000
            print("vrijednost u KΩ je",kiloohm,"KΩ")
        except ValueError:
            print("GREŠKA: Unesena vrijednost nije ispravan broj.")


        #amperi

    elif opcija == 3:
        try:
            print("izračun ampera u miliampere")
            amper=float(input("upisi vrijednost u amperima: "))
            miliamper=amper*1000
            print("vrijednost u mA je ",miliamper,"mA")
        except ValueError:
            print("GREŠKA: Unesena vrijednost nije ispravan broj.")

        #prekid

    elif opcija == 0:
        try:
            print("prekid programa, doviđenja ;)")
        except ValueError:
            print("GREŠKA: Unesena vrijednost nije ispravan broj.")
            break

        #nevažeća vrijednost
    else:
      print("ne prepoznajem, upisite važeću vrijednost")
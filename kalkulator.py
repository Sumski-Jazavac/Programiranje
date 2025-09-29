#Izbornik za kalkulator
print("izbornik")
print("----------------------")
print("1. Izračun napona")
print("2. Izračun otpora")
print("3. Izračun jakosti struje")
print("4. Izračun otpora paralelnog spoja opornika")
print("5. Izračun otpora serijskog spoja otpornika")
print("-----------------------")
opcija=int(input("Izaberite operaciju (1/2/3/4/5): "))

#Struktura grananja
if opcija == 1:         # == != < > <> >= <=
    print("izračun napona struje")
    Jakost=int(input("Upisi jakos struje: "))
    otpor=int(input("upisi otpor: "))
    Napon=Jakost*otpor
    print("napon je ",Napon,"V")
elif opcija == 2:
    print("Izračun otpora struje")
    napon=int(input("Upisi napon: "))
    Jakost=int(input("Upisi jakost struje: "))
    otpor = napon/Jakost
    print("otpor je",otpor,"ohma")
elif opcija == 3:
    print("izračun jakosti struje")
    napon=int(input("upisi napon: "))
    otpor=int(input("upisi otpor: "))
    jakost=napon/otpor
    print("jakost struje je ",jakost,"A")
elif opcija == 4:
    print("izračun orpora paralelnog spoja otpornika")
    otpornik1=int(input("upisi otpor prvog otpornika: "))
    otpornik2=int(input("upisi otpor drugog otpornika: "))
    otpor12=(1/otpornik1) + (1/otpornik2)
    print("ukupan otpor je",otpor12,"ohma")
elif opcija == 5:
    print("izračun otpora serijskog spoja")
    otpornik1=int(input("upisi otpor prvog otpornika: "))
    otpornik2=int(input("upisi otpor drugog otpornika: "))
    otpor12=otpornik1 + otpornik2 
    print("ukupan otpor je ",otpor12,"ohma")
else:
    print("pogrešan unos")


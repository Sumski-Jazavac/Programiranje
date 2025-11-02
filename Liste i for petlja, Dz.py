#Izbornik za kalkulator

def izracunaj_sumu_liste(lista_vrijednosti):
    """Prima listu brojeva i vraća njihovu sumu."""
    suma = 0
    for vrijednost in lista_vrijednosti:
        suma += vrijednost
    return suma


def ispisi_izbornik():
    # Izbornik za kalkulator
    print("----------------------")
    print("Izbornik za kalkulator")
    print("----------------------")
    print("1. Izračun napona struje")
    print("2. Izračun otpora struje")
    print("3. Izračun jakosti struje")
    print("4. Izračun ukupnog serijskog otpora (N otpornika)")
    print("0. Izlaz")
    print("----------------------")


def izracunaj_napon(jakost, otpor):
    return jakost * otpor 




def izracunaj_otpor(napon, jakost):
    return napon / jakost




def izracunaj_struju(napon, otpor):
    return napon / otpor






while True:

    ispisi_izbornik()


    try:
        opcija = int(input("Izaberite operaciju (1 / 2 / 3 / 0):"))
    except Exception as greska:
        print(f"pogrešan unos, molim unesi broj od 1 do 3. \nOdaberite 0 za izlaz.")
        continue



    #Struktura grananja
    if opcija == 1:     # == != < > <> >= <= - operatori usporedbe
        print("Izračun napona struje")
        try:
            jakost = int(input("Upiši jakost struje: "))
            otpor = int(input("Upiši otpor: "))
        except Exception as greska:
            print(f"pogrešan unos: {greska}. \nMolim unesite brojeve.")
            continue
        napon = izracunaj_napon(jakost, otpor)
        print(f"Napon struje je: {napon} V")
    elif opcija == 2:
        print("Izračun otpora struje")
        try:
            napon = int(input("Upiši napon: "))
            jakost = int(input("Upiši jakost struje: "))
            otpor = izracunaj_otpor(napon, jakost)
        except ValueError:
            print("Pogrešan unos, upisi broj")
            continue
        except ZeroDivisionError:
            print("ne mogu dijeliti s 0")
            continue
        except Exception as greska:
            print(f"pogrešan unos: {greska}. \nMolim unesite brojeve.")
            continue





        print(f"Otpor je: {otpor} Ohm")
    elif opcija == 3:
        print("Izračun jakosti struje")
        try:
            napon = int(input("Upiši napon: "))
            otpor = int(input("Upiši otpor: "))
            jakost = izracunaj_struju(napon, otpor)
        except ValueError:
            print("Pogrešan unos, upisi broj")
            continue
        except ZeroDivisionError:
            print("ne mogu dijeliti s 0")
            continue
        except Exception as greska:
            print(f"pogrešan unos: {greska}. \nMolim unesite brojeve.")
            continue
        print(f"Jakost struje je: {jakost} A")


    elif opcija == 4:
        print("\n--- Izračun serijskog otpora (N otpornika) ---")

        # 1. Kreiramo praznu "vrećicu" (listu)
        lista_otpora = []

        # 2. Pokrećemo NOVU petlju samo za unos otpornika
        while True:
            # :.2f formatira ispis liste na 2 decimale (samo za ljepši prikaz)
            print(f"   Trenutni otpornici u listi: {[f'{x:.2f} Ω' for x in lista_otpora]}") 
            unos_str = input("Unesite vrijednost otpora (ili 'kraj' za izračun): ")

            # 3. Provjera želi li korisnik izaći iz unosa
            if unos_str.lower() == 'kraj':
                break # Prekida se SAMO unutarnja petlja

            # 4. Ako nije 'kraj', pokušavamo pretvoriti u broj
            try:
                vrijednost = float(unos_str)
                # Osiguravamo se da otpor ne bude negativan
                if vrijednost <= 0:
                    print("GREŠKA: Otpor mora biti pozitivan broj.")
                else:
                    # 5. Ako je sve u redu, dodajemo u listu
                    lista_otpora.append(vrijednost)
                    print(f"   -> Dodan otpornik: {vrijednost} Ω")
            except ValueError:
                print("GREŠKA: Unos mora biti ispravan broj ili riječ 'kraj'.")

        # 6. Nakon što je unutarnja petlja gotova (korisnik je upisao 'kraj')
        # provjeravamo je li lista prazna
        if len(lista_otpora) > 0:
            # 7. Ako nije prazna, zovemo našeg novog "Radnika"
            ukupni_otpor = izracunaj_sumu_liste(lista_otpora)
            print(f"\nREZULTAT: Ukupan serijski otpor za {len(lista_otpora)} otpornika je: {ukupni_otpor:.4f} Ω")
        else:
            # 8. Ako je prazna, samo javljamo
            print("\nNiste unijeli nijedan otpornik. Povratak na izbornik.")

        input("\nPritisnite Enter za povratak na glavni izbornik...")

    elif opcija == 0:
        print("Izlaz iz programa. Doviđenja!")
        break
        

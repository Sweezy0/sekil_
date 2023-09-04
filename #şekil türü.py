#şekil türü
sekil_turu=input("üçgen mi dörtgen mi?:".strip().lower())
if sekil_turu=="dörtgen":
    kenar1=float(input("birinci kenarın uzunluğunu girin:"))
    kenar2=float(input("ikinci kenarın uzunluğunu girin:"))
    kenar3=float(input("üçüncü kenarın uzunluğunu girin:"))
    kenar4=float(input("dördüncü kenarın uzunluğunu girin:"))
    if kenar1==kenar1==kenar3==kenar4:
        print("bu bir karedir.")
    elif kenar1==kenar3 and kenar2==kenar4:
        print("bu bir diktörgendir.")
    else:
        print("bu bir sıradan dörtgendir.")
elif sekil_turu=="üçgen":
    kenar1=float(input("birinci kenarın uzunluğunu girin:"))
    kenar2=float(input("ikincikenarın uzunluğunu girin:"))
    kenar3=float(input("üçüncü kenarın uzunluğunu girin:"))
    if kenar1==kenar2==kenar3:
        print("bu bir eşkenar üçgendir")
    elif kenar1==kenar2 or kenar1==kenar3 or kenar2==kenar3:
        print("bu bir ikizkenar üçgendir")    
    else:
        print("bu bir sıradan üçgendir")
else:
    print("geçersiz giriş! Lütfen 'üçgen' veya 'dörtgen' girin")
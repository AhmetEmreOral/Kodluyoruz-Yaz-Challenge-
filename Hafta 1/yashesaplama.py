import datetime

def yas_hesapla(dogum_tarihi):
    simdi = datetime.datetime.now()
    yas = simdi.year - dogum_tarihi.year
    if simdi.month < dogum_tarihi.month or (simdi.month == dogum_tarihi.month and simdi.day < dogum_tarihi.day):
        yas -= 1
    return yas

# Kullanıcıdan doğum tarihini girmesini iste
gun = int(input("Doğum gününü girin: "))
ay = int(input("Doğum ayını girin: "))
yil = int(input("Doğum yılını girin: "))

dogum_tarihi = datetime.datetime(yil, ay, gun)

# Yaşı hesapla ve ekrana yazdır
yas = yas_hesapla(dogum_tarihi)
print("Yaşınız:", yas)

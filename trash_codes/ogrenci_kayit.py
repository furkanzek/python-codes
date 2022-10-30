ogrenciler = {}

number = input('Öğrenci numaranız: ')
name = input('Adınız: ')
surname = input('Soyadınız: ')
phone = input('Telefon numaranız: ')


# ogrenciler[number] = {
#     'ad' : name,
#     'soyad' : surname,
#     'telefon' : phone,
# }

ogrenciler.update({
    number : {
        'ad' : name,
        'soyad' : surname,
        'telefon' : phone,      
    }
})


ogrenciNo = input('Bilgilerini görmek istediğiniz öğrencinin numarası: ')
ogrenci = ogrenciler[ogrenciNo]

print(ogrenci)
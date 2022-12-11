import random

rndSayi = random.randint(1,101)
sayac = 0
hak = 5

while (hak > 0):
    hak -= 1
    sayac += 1
    tahmin = int(input('Yeni tahmininiz: '))
    
    if (tahmin == rndSayi):
        print(f'\nDoğru bildiniz, seçilen sayı: {rndSayi}, deneme adedi: {sayac}')
    elif (tahmin > rndSayi):
        print('\nİn\n')
    else:
        print('\nÇık\n')
        
    if (hak == 0):
        print('\nHakkınız kalmadı, oyunu baştan başlatın')
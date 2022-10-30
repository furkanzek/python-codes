sayi = int(input('Bir sayı giriniz: '))
asalMi = True

if (sayi == 1):
    print('1, bir asal sayı değildir')
    
for i in range(2,sayi):
    if (sayi % i == 0):
        asalMi = False
        break
    
if asalMi == True:
    print('Sayı asaldır')
else:
    print('Sayı asal değildir')
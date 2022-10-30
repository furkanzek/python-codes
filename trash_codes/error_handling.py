# list = ["1","2","5a","10b","abc","10","50"]

# for deger in list:
#     try:
#         print(int(deger))
#     except ValueError:
#         continue

#****************************************************

# while True:
#   deger = input('Bir değer girin: ')
#   if deger == 'q':
#       break
#   try:
#       res = float(deger)
#       print('Sayı: ', res) 
#   except ValueError:
#       print('Hatalı giriş')
#       continue

#****************************************************

# pwd = input('Şifre oluşturunuz: ')

# def checkPassword(pwd):
#     trkKrktr = 'ğıİçöşü'

#     for i in pwd:
#         if i in trkKrktr:
#             raise TypeError('Parola, Türkçe karakter içeremez')
#         else:
#             pass
    
#     print('geçerli parola')

# try:
#     checkPassword(pwd)
# except TypeError as err:
#     print(err)

#****************************************************


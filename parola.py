import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Parolanızın kaç karakter olmasını istersiniz? "))
parola = ""
for i in range(uzunluk):
    parola += random.choice(karakterler)
print(parola)

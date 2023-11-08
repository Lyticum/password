import random
import string
import sys


while True:
    alfabe=list(string.ascii_letters + string.digits)
    şifre=input("Yeni bir şifre oluşturmak istiyormusunuz (Evet için;E Hayır için;H)").lower()
    if şifre=="e":
        şifre1=[]
        sayi=int(input("Karakter sayısı giriniz;"))
        for i in range(1, sayi):
            şifre1.append(random.choice(alfabe))
        random.shuffle(şifre1)
        şifre1="".join(şifre1)
        print(şifre1)
        
    elif şifre =="h":
        sys.exit("Tekrar bekleriz!")
    

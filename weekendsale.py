#Muhammad Reza Ubaidillah
#2109106084
hari = [" Sabtu"," Minggu"," Hari Raya"]

def menu():
    print("========================================================")
    print("1. Diskon" +  hari[0])
    print("2. Diskon" +  hari[1])
    print("3. Diskon" +  hari[2])
    print("4. Stop Program")
    print("========================================================")


def menu2():
    print("========================================================")
    print("1. Hitung Lagi")
    print("2. Ganti Hari Atau Stop Program")
    print("========================================================")


def sabtu():
    harga = int(input("Masukkan Total Harga : "))
    diskon = harga * (10/100)
    harga = harga - diskon
    print("Selamat Anda Mendapatkan Diskon 10% Karena Hari ini" + hari[0])
    print("Harga Menjadi",int(harga))
    while True:
        menu2()
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            return sabtu()            
        elif pilih == ("2"):
            break
        else:
            print("Ngantuk Bang?")

def minggu():
    harga = int(input("Masukkan Total Harga : "))
    diskon = harga * (25/100)
    harga = harga - diskon
    print("Selamat Anda Mendapatkan Diskon 25% Karena Hari ini" + hari[2])
    print("Harga Menjadi",int(harga))
    while True:
        menu2()
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            return minggu()
        elif pilih == ("2"):
            break
        else:
            print("Ngantuk Bang?")

def raya():
    harga = int(input("Masukkan Total Harga : "))
    diskon = harga * (90/100)
    harga = harga - diskon
    print("Selamat Anda Mendapatkan Diskon 90% Karena Hari ini" + hari[2])
    print("Harga Menjadi",int(harga))
    while True:
        menu2()
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            return raya()
        elif pilih == ("2"):
            break    
        else:
            print("Ngantuk Bang?")

def milih():
    while True: 
        menu()
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            sabtu()
        elif pilih == ("2"):
            minggu()
        elif pilih == ("3"):
            raya()
        elif pilih == ("4"):
            print("Program Telah Dimatikan")
            print("========================================================")
            break
        else:
            print("Ngantuk Bang")

#PROGRAM UTAMA
print("Selamat Datang Di Program Kalkulator Diskon Hari Spesial")
milih()





        






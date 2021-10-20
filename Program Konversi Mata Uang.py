#Muhammad Reza Ubaidillah
#2109106084

#MENU
def menu():
    print("Menu Pilihan")
    print("1. IDR - USD")
    print("2. IDR - SGD")
    print("3. IRD - EUR")
    print("4. IDR - JPY")

#MENGKONVERSI KE USD
def usd():
    idr = float(input("Masukkan Nilai Rupiah : "))
    usd = idr / 14100.5
    usd = round(usd,3)
    print(usd, "USD")

#MENGKONVERSI KE SGD
def sgd():
    idr = float(input("Masukkan Nilai Rupiah : "))
    sgd = idr / 10490.37
    sgd = round(sgd,3)
    print(sgd, "SGD")

#MENGKONVERSI KE EUR
def eur():
    idr = float(input("Masukkan Nilai Rupiah : "))
    eur = idr / 16411.61
    eur = round(eur,3)
    print(eur, "EUR")

#MENGKONVERSI KE JPY
def jpy():
    idr = float(input("Masukkan Nilai Rupiah : "))
    jpy = idr / 123.07
    jpy = round(jpy,3)
    print(jpy, "JPY")

#PROGRAM UTAMA
print("Selamat Datang Di Program Konversi Mata Uang Rupiah Ke Mata Uang USD, SGD, EUR dan JPY")
print("======================================================================================")

menu()
pilih = input("Masukkan Pilihan : ")
if pilih == ("1"):
    usd()
elif pilih == ("2"):
     sgd()
elif pilih == ("3"):
    eur()
elif pilih == ("4"):
    jpy()
else:
    print("Ngantuk Bang?")
def menu():
    print("Menu Pilihan")
    print("1. Form Mahasiswa")
    print("2. Form Orang Tua")

print("Program Mengisi Bio Data")
form1 = {
    "Nama":str(input("Masukkan Nama : ")),
    "NIM":int(input("Masukkan NIM : ")),
    "BB":float(input("Berat Badan :")),
    "TB":float(input("Tinggi Badan : ")),
    "Umur":int(input("Umur : ")),
}

form2 = {"Nama":str(input("Masukkan Nama Orang Tua : ")),
    "pekerjaan":str(input("Masukkan Pekerjaan Orang Tua : ")),
    "BB":int(input("Berat Badan Orang Tua :")),
    "TB":float(input("Tinggi Badan Orang Tua : ")),
    "Umur":int(input("Umur Orang Tua : ")),
}

formlist = {1:form1, 2:form2}

menu()
pilih = input("Masukkan Pilihan ")
if pilih == ("1"):
    print(formlist[1])
elif pilih == ("2"):
    print(formlist[2])
else:
    ("Ngantuk Bang?")

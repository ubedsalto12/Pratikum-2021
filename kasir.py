barang = []
harga_satuan = [] 
jumlah_barang = []
total_harga = []
pesanan = []
bank = []

minuman = ["Latte     ","Espresso  ","Cappuccino","Americano ","Cold Brew ","Affogato  "]

def daftar_menu():
    print("=============================================")
    print("                    Menu                     ")
    print("=============================================")
    print("1. ",minuman[0],"                   Rp 15.000")  
    print("2. ",minuman[1],"                   Rp 16.000")
    print("3. ",minuman[2],"                   Rp 17.000")
    print("4. ",minuman[3],"                   Rp 18.000")
    print("5. ",minuman[4],"                   Rp 19.000")
    print("6. ",minuman[5],"                   Rp 20.000")
    print("=============================================")
    
def batalkan_pesanan():
    print("=============================================")
    print("1. Simpan Pesanan")
    print("2. Untuk Batalkan Pesanan")
    print("=============================================")
    

def program_kasir():
    print("=============================================")
    print("    Selamat Datang Di Program Kasir REZA     ")
    print("=============================================")
    while True:

        daftar_menu()
        pilih = input("Masukkan Pilihan : ")
        jumlah = int(input("Masukkan Jumlah Barang : "))
        if pilih == ("1"):
            barang.append(minuman[0])
            jumlah_barang.append(jumlah)
            harga_satuan.append(15000)
            total_harga.append(jumlah*15000)
            batalkan_pesanan()
            pilih1 = input("Masukkan Pilihan : ")
            if pilih1 == ("2"):
                barang.remove(minuman[0])
                jumlah_barang.remove(jumlah)
                harga_satuan.remove(15000)
                total_harga.remove(jumlah*15000)
            elif pilih == ("1"):
                print("")
            else:
                False
                print("Masukkan Tidak Tersedia Silahkan Input lagi")
                continue
    
        elif pilih == ("2"):
            barang.append(minuman[1])
            jumlah_barang.append(jumlah)
            harga_satuan.append(16000)
            total_harga.append(jumlah*16000)
            batalkan_pesanan()
            pilih1 = input("Masukkan Pilihan : ")
            if pilih1 == ("2"):
                barang.remove(minuman[1])
                jumlah_barang.remove(jumlah)
                harga_satuan.remove(16000)
                total_harga.remove(jumlah*16000)
            elif pilih == ("1"):
                print("")

        elif pilih == ("3"):
            barang.append(minuman[2])
            jumlah_barang.append(jumlah)
            harga_satuan.append(17000)
            total_harga.append(jumlah*17000)
            batalkan_pesanan()
            pilih1 = input("Masukkan Pilihan : ")
            if pilih1 == ("2"):
                barang.remove(minuman[2])
                jumlah_barang.remove(jumlah)
                harga_satuan.remove(17000)
                total_harga.remove(jumlah*17000)
            elif pilih == ("1"):
                print("")
    
        elif pilih == ("4"):
            barang.append(minuman[3])
            jumlah_barang.append(jumlah)
            harga_satuan.append(18000)
            total_harga.append(jumlah*18000)
            batalkan_pesanan()
            pilih1 = input("Masukkan Pilihan : ")
            if pilih1 == ("2"):
                barang.remove(minuman[3])
                jumlah_barang.remove(jumlah)
                harga_satuan.remove(18000)
                total_harga.remove(jumlah*18000)
            elif pilih == ("1"):
                print("")

        elif pilih == ("5"):
            barang.append(minuman[4])
            jumlah_barang.append(jumlah)
            harga_satuan.append(19000)
            total_harga.append(jumlah*19000)
            batalkan_pesanan()
            pilih1 = input("Masukkan Pilihan : ")
            if pilih1 == ("2"):
                barang.remove(minuman[4])
                jumlah_barang.remove(jumlah)
                harga_satuan.remove(19000)
                total_harga.remove(jumlah*19000)
            elif pilih == ("1"):
                print("")

        elif pilih == ("6"):
            barang.append(minuman[5])
            jumlah_barang.append(jumlah)
            harga_satuan.append(20000)
            total_harga.append(jumlah*20000)
            batalkan_pesanan()
            pilih1 = input("Masukkan Pilihan : ")
            if pilih1 == ("2"):
                barang.remove(minuman[5])
                jumlah_barang.remove(jumlah)
                harga_satuan.remove(20000)
                total_harga.remove(jumlah*20000)
            elif pilih == ("1"):
                print("")
        else:
            print("Pilihan Tidak Tersedia Silahkan Input Lagi")
         
        print("=============================================")
        print("1. Untuk Lanjut Berbelanja")
        print("2. Untuk Berhenti")
        print("=============================================")
        lanjut = input("Masukkan Pilihan : ")
        if lanjut == ("2"):
            print("")
            break
        if lanjut == ("1"):
            print("")
        else:
            print("Pilihan Tidak Tersedia Silahkan Input Lagi")     
        
    print_nota()
    
def print_nota():   
    print("=========================================================================================")
    print("                                          Nota                                           ")
    print("=========================================================================================")
    print("No.     Nama Barang                     Harga satuan         Jumlah             Total    ")
    for x in range(0,len(barang)):
		    print("{}        {}                        Rp{}               {}             Rp{} ".format(x+1, barang[x], harga_satuan[x], jumlah_barang[x],total_harga[x]))

    print("=========================================================================================")
    print("Total Harga : RP ", sum(total_harga))

    bayar = int(input("Masukkan Uang Pembayaran : "))
    print("Total Harga : RP ",sum(total_harga))
    print("Jumlah uang : RP ", bayar)
    print("Kembalian : RP ", (bayar-sum(total_harga)))
    print("")
    print("=============================================")
    pesanan.append(1)
    sum(pesanan)
    bank.append(sum(total_harga))
    
    ulang_program()
    
    

def ulang_program():    
    print("=============================================")
    print("1. Program Kasir")
    print("2. Menu Utama")
    print("3. Matikan Program")
    print("=============================================")
    pilih3 =input("Masukkan Pilihan: ")
    while True: 
        if pilih3 == ("1"):
            program_kasir()
            break
        elif pilih3 == ("2"):
            menu_utama()
        elif pilih3 == ("3"):
            break

def menu_utama():
    username = input("Masukkan Username : ")
    print("=============================================")
    print("Masukkan Password 3 NIM Terakhir Untuk Masuk Ke  Program Admin")
    print("Masukkan Password 3 NIM Awal Untuk Masuk Ke program Kasir (User)")
    print("=============================================")
    password =input("Masukkan Password: ")
    while True:
        if password == ("084"):
            print(f"Selamat Datang {username} Anda Masuk Ke Program Admin")
            program_admin()
        elif password == ("210"):
            print(f"Selamat Datang {username} Anda Masuk Ke Program Kasir (User)")
            program_kasir()
        else:
            print("Password Salah")
            return menu_utama()
def program_admin():
    print("=============================================")
    print("1. Keuntungan  Harian")
    print("2. Kembali Ke Menu Utama")
    pilih = input("Masukkan Pilihan : ")
    if pilih == ("1"):
        print(f"Pesanan Hari Ini{pesanan}\nDuit Di Kasir{bank}")
        program_admin()
    elif pilih == ("2"):
        menu_utama()

menu_utama()


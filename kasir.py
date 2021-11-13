jumlah_pesanan_hari_ini = []
total_uang_kasir = []
barang = []
harga_satuan = [] 
jumlah_barang = []
total_harga = []
minuman = [ "Latte     ","Espresso  ","Cappuccino","Americano ","Cold Brew ","Affogato  "]
harga = [ 15000, 16000, 17000, 18000, 19000, 20000]

def program_menu_awal():
    print("=============================================")
    print("1. Program Admin Password 3 NIM Akhir")
    print("2. Program Kasir Password 3 NIM Awal")
    print("=============================================")
    while True:
        pilih = input("Masukkan Password : ")
        if pilih == ("084"):
            program_admin()
            break
        elif pilih == ("210"):
            program_user()
        else:
            print("Masukkan Tidak Tersedia Silahkan Input lagi")

def program_admin():
    print("=============================================")
    print("1. Data Penjualan Hari Ini")
    print("2. Tambah Menu")
    print("3. Hapus Menu")
    print("4. Kembali Ke Menu Awal")
    print("5. Matikan Program")
    print("6. Menu")
    print("=============================================")
    while True:
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            program_data_penjualan()
            break
        elif pilih == ("2"):
            program_tambah_menu()
        elif pilih == ("3"):
            program_hapus_menu()
        elif pilih == ("4"):
            program_menu_awal() 
        elif pilih == ("5"):
            print("=============================================")
            print("           Program Telah Dimatikan           ")
            print("=============================================")
            break
        elif pilih == ("6"):
            program_tampilan_menu()
            program_admin()
        
        else:
            print("Masukkan Tidak Tersedia Silahkan Input Lagi")

def program_user():
    print("=============================================")
    print("1. Menu")
    print("2. Pesan ")
    print("3. Hapus pesanan")
    print("4. Ubah Jumlah Pesanan")
    print("5. Bayar Pesanan")
    print("6. Menu Awal")
    print("=============================================")
    while True:
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            program_tampilan_menu()
            program_user()
        elif pilih == ("2"):
            program_kasir()
        elif pilih == ("3"):
            program_hapus_pesanan()
        elif pilih == ("4"):
            program_ubah_pesanan()
        elif pilih == ("5"):
            program_print_nota()
        elif pilih == ("6"):
            program_menu_awal()

def program_ubah_pesanan():
    print("=========================================================================================")
    print("                                          Nota                                           ")
    print("=========================================================================================")
    print("No.     Nama Barang                     Harga satuan         Jumlah")
    for x in range(0,len(barang)):
		    print("{}        {}                        Rp{}               {} ".format(x+1, barang[x], harga_satuan[x], jumlah_barang[x],))
    print("=========================================================================================")
    print(barang)
    print(harga_satuan)
    print(jumlah_barang)
    print(total_harga)
    del (total_harga[-1])
    print(total_harga)

        

def program_milih_ubah():
    print("1. Ubah Jumlah Lagi")
    print("2. Kembali Ke Menu")
    pilih = input("Masukkan Pilihan : ")
    while True:
        if pilih == ("1"):
            program_ubah_pesanan()
        elif pilih == ("2"):
            program_user()

def program_hapus_pesanan():
    print("=========================================================================================")
    print("                                          Nota                                           ")
    print("=========================================================================================")
    print("No.     Nama Barang                     Harga satuan         Jumlah")
    for x in range(0,len(barang)):
		    print("{}        {}                        Rp{}               {} ".format(x+1, barang[x], harga_satuan[x], jumlah_barang[x],))
    print("=========================================================================================")
    while True: 
        hapus = int(input("Masukkan Nomor Menu Yang Ingin Di Hapus (Ketik 0 Untuk Kembali Ke Menu User) : "))
        hapus -= 1
        if hapus != (-1):
            del barang[hapus]
            del harga_satuan[hapus]
            del jumlah_barang[hapus]
            program_hapus_pesanan()
        else:
            program_user()
        


def program_tambah_menu():
    tambah = input("Masukkan Nama Menu Yang Ingin Ditambah : ")
    tambah_harga = int(input("Masukkan Harga"))
    minuman.append(tambah)
    harga.append(tambah_harga)
    print("=============================================")
    print("1. Tambah Menu Lagi")
    print("2. Kembali Ke program Admin")
    print("=============================================")
    while True: 
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            program_tambah_menu()
        elif pilih == ("2"):
            program_admin()
        else:
            print("Masukkan Tidak Tersedia Silahkan Input Lagi")

def program_hapus_menu():
    program_tampilan_menu()
    hapus = int(input("Masukkan Nomor Menu Yang Ingin Di Hapus (Ketik 0 Untuk Kembali Menu User) : "))
    hapus -= 1
    del minuman[hapus]
    del harga[hapus]
    print("=============================================")
    print("1. Hapus Menu Lagi")
    print("2. Kembali Ke program Admin")
    print("=============================================")  
    while True: 
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            program_hapus_menu()
        elif pilih == ("2"):
            program_admin()
        else:
            print("Masukkan Tidak Tersedia Silahkan Input Lagi")


def program_data_penjualan():
    print(f"Pesanan Hari Ini : {sum(jumlah_pesanan_hari_ini)}\nTotal Uang Yang Ada Dikasir : {sum(total_uang_kasir)}")
    print("=============================================")
    print("1. Kembali Ke Menu Awal")
    print("2. Matikan Program")
    print("=============================================")
    while True:
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            program_menu_awal()
        elif pilih == ("2"):
            print("=============================================")
            print("           Program Telah Dimatikan           ")
            print("=============================================")
            break
        else:
            print("Masukkan Tidak Tersedia Silahkan Input Lagi")

def program_kasir():
    program_tampilan_menu()
    while True:
        pilih = int(input("Masukkan Pilihan : "))
        jumlah = int(input("Masukkan Jumlah Barang : "))
        pilih -= 1
        if pilih == pilih:
            barang.append(minuman[pilih])
            jumlah_barang.append(jumlah)
            harga_satuan.append(harga[pilih])
            total_harga.append(jumlah*harga_satuan)
            program_simpan_batalkan_pesanan()

        else: 
            print("Masukkan Tidak Tersedia Silahkan Input lagi")

def program_tampilan_menu():
    print(" ========= Menu Coffe Shop APD3 =========")
    for i in range(0, len(minuman)):
        print(f"        {i+1}. {minuman[i]}  Rp{harga[i]}")

def program_simpan_batalkan_pesanan():
    print("=============================================")
    print("1. Simpan Pesanan")
    print("2. Batalkan Pesanan")
    print("=============================================")
    while True:
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            program_menu_pesan_lagi()
        elif pilih == ("2"):
            program_batalkan_pesanan()
        else:
            print("Masukkan Tidak Tersedia Silahkan Input Lagi")

def program_batalkan_pesanan():
    del barang[-1]
    del jumlah_barang[-1]
    del total_harga[-1]
    del harga_satuan[-1]
    program_menu_pesan_lagi()

def program_menu_pesan_lagi():
    print("=============================================")
    print("1. Pesan Lagi")
    print("2. Selesai (print Nota)")
    print("3. Menu User")
    print("=============================================")
    while True:
        pilih = input("Masukkan Pilihan : ")
        if pilih == ("1"):
            program_kasir()
        elif pilih == ("2"):
            program_print_nota()
        elif pilih == ("3"):
            program_user()
        else:
            print("Masukkan Tidak Tersedia Silahkan Input Lagi")

def program_print_nota():
    print("=========================================================================================")
    print("                                          Nota                                           ")
    print("=========================================================================================")
    print("No.     Nama Barang                     Harga satuan         Jumlah")
    for x in range(0,len(barang)):
		    print("{}        {}                        Rp{}               {} ".format(x+1, barang[x], harga_satuan[x], jumlah_barang[x],))
 
    print("=========================================================================================")
    print("Total Harga : RP ", sum(total_harga[x]))
    uang_dibayar = sum(total_harga[x])
    
    bayar = int(input("Masukkan Uang Pembayaran : "))
    if bayar >= uang_dibayar:
        print("Terima Kasih Telah Berbelanja")
    else:
        print("Uang Anda Tidak Cukup")
        program_print_nota()
            
        
    print("Total Harga : RP ",sum(total_harga[x]))
    print("Jumlah uang : RP ", bayar)
    print("Kembalian : RP ", (bayar-sum(total_harga[x])))
    print("")
    print("=============================================")
    jumlah_pesanan_hari_ini.append(1)
    total_uang_kasir.append(sum(total_harga[x]))
    
    a = 0
    while a <= len(barang):
        for y in barang[:]:
            y == barang[0]
            barang.remove(y)
            a+=1
    b = 0           
    while b <= len(harga_satuan):
        for y in harga_satuan[:]:
            y == harga_satuan[0]
            harga_satuan.remove(y)
            b+=1
    c = 0
    while c <= len(jumlah_barang):
        for y in jumlah_barang[:]:
            y == jumlah_barang[0]
            jumlah_barang.remove(y)
            c+=1
    d = 0
    while d <= len(total_harga):
        for y in total_harga[:]:
            y == total_harga[0]
            total_harga.remove(y)
            d+=1

    program_user()
        



#PROGRAM UTAMA
print("=============================================")
print("    Selamat Datang Di Program Kasir REZA     ")
print("=============================================")
program_menu_awal()
            

import sys, os

class Data:
  nama=''
  no_telp=''

kontak = []
menu = 0

def start():
  os.system('cls')
  print("Selamat Datang!")
  print("---------------")
  print("---Menu---")
  print("1. Daftar Kontak")
  print("2. Tambah Kontak")
  print("3. Keluar")
  menu = int(input("Pilih Menu : "))
  if menu == 1 :
    daftarKontak()
    input("Tekan Apapun, Enter")
    start()
  elif menu == 2:
    tambahKontak()
    start()
  elif menu == 3 :
    print("Program selesai, Sampai Jumpa!")
    sys.exit()
  else:
    print("Menu tidak tersedia")
    start()

def daftarKontak():
  for data in kontak:
    print("Daftar Kontak:")
    print("Nama : " + data.nama)
    print("No Telepon : " + str(data.no_telp))

def tambahKontak():
  kontakBaru = Data()
  kontakBaru.nama = (input("Nama : "))
  kontakBaru.no_telp = (int(input("No Telepon : ")))
  kontak.append(kontakBaru)
  print("Kontak Berhasil ditambahkan")

start()


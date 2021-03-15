#Soal 3
nilai1 = float(input('Masukan nilai ujian teori: '))
nilai2 = float(input('Masukan nilai ujian praktek: '))
if (nilai1 >= 70 and nilai2 >= 70):
  print('Selamat, Anda lulus!')
elif (nilai1 >= 70 and nilai2 < 70):
  print('Anda harus mengulang ujian praktek')
elif (nilai1 < 70 and nilai2 >= 70):
  print('Anda harus mengulang ujian teori')
else:
  print('Anda harus mengulang ujian teori dan praktek.')

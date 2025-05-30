#! /usr/bin/env python3

angka = int(input("Masukan Angka: "))
if angka % 2 == 0:
  print("Angka tersebut genap.")
else:
  print("Angka tersebut ganjil.")

input("Press to continue (Penjumlahan)")

angka1 = int(input("Masukan angka pertama"))
angka2 = int(input("Masukan angka kedua"))

jumlah = angka1 + angka2

print("Jumlah dari %d+%d=%d" % (angka1, angka2, jumlah))

input("Press to continue (Loop)")

i = 1
while i <= 10:
  print(i)
  i += 1

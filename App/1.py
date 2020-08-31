from json import load, dump
from os import system
from time import sleep

import ayam

o = ayam.faiz()

system("cls")

if o :

	meteor = ayam.naruto()
	if meteor:
		print("Selamat datang Di Toko Tahu")
		sleep(1.49)
		system("cls")
		generation = ""

		while generation != "1":
			system("cls")
			ayam.Nobunaga()
			henshin = input("Tulis angka atau huruf : ").upper()

			if henshin == "A":
				ayam.Ryoma()
				ayam.Isi()
				input("ENTER TO EXIT")

			elif henshin == "B":
				ayam.menambah()
				input("ENTER TO EXIT")


			elif henshin == "C":
				ayam.membuang()
				input("ENTER TO EXIT")

			elif henshin == "D":
				ayam.mencari()
				input("ENTER TO EXIT")

			elif henshin == "1":
				break

			else:
				print("Input Menu Yang Benar")
				input("ENTER untuk keluar")





	else:
		print("ANDA GAGAL")
else:
	print("Ini Rusak")



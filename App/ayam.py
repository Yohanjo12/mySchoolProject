from json import load, dump
from os import system 
from time import sleep
from getpass import getpass
import math

nasi = 'a.json'

ayam = 'goreng.json'

tahu = {}

tempe = {}

def faiz():
	global tahu, tempe

	with open(nasi) as rider:
		tahu = load(rider)

	with open(ayam) as rider:
		tempe = load(rider)

	return True

def decade():
	global tahu, tempe

	with open(nasi, "w") as q:
		dump(tahu, q)

	with open(ayam, 'w') as q:
		dump(tempe, q)

	return True

def naruto():
	counter = 1
	cross = input("Enter Username : ")
	fourze = getpass("Enter Pass : ")
	V3 = False #datacheck
	V2 = False #passlogin
	if cross in tahu:
		V3 = True
		V2 = (tahu[cross] == fourze)
	else:
		V3 = False
		V2 = False

	while not V3 and not V2:
		counter += 1
		if counter > 3:
			return False
		print("MASUKKAN YANG BENAR")
		build = input("Enter Username : ")
		ghost = getpass("Enter Pass : ")
		if cross in tahu:
			V3 = True
			V2 = (tahu[cross] == fourze)
		else:
			V3 = False
			V2 = False
	else:
		print("Anda Hebat Dan Telah BENAR")
		return True



def Nobunaga():
	print("Halo, selamat datang di Toko Tahu")
	print("A. Print isi Toko Tahu")
	print("B. Menambah Jumlah Tahu")
	print("C. Membuang Tahu")
	print("D. Mencari Jumlah di Tahu")
	print("1. Keluar dari Toko Tahu")



def Isi():
	if len(tempe) > 0:
		no = 1
		for info in tempe:
			
			print(f"{no}   |   {tempe[info][0]}\t   |   {tempe[info][1]}\t   |   Rp.{tempe[info][2]}\t   | {info} Buah\t   |\n")
			no += 1

	else:
		print("Toko Tahu kosong")


def Ryoma():
	print(f"No  |   Masak      |   Rasa\t   |   Harga\t   | Jumlah\t   |\n")


def menambah():
	print("Menambah Tahu\n")
	print("Harga satu Tahu Goreng Rp.1000")
	print("Harga satu Tahu Rebus Rp.900")
	q = int(input("Menambah Tahu berapa Buah : "))
	m = input("Goreng atau Rebus : ")
	h = input("Pedas atau Biasa : ")
	f = int(input("Masukkan Harga : "))
	


	tempe.update({q:[m,h,f]})
	decade()
	print("Sedang Membuat.")
	sleep(2.99)
	print("Selesai.")

def membuang():
	albe = input("Jumlah isi yang ingin dibuang  : ")
	
	if albe in tempe:
		del tempe[albe]

		
		decade()
		print("Sedang Membuang atau Menghancurkan.")
		sleep(4)
		print("Membuang atau Menghancurkan isi selesai.")

	else:
		print(f"Jumlah {albe} tidak ada di Toko Tahu")


def mencari():
	print("Mencari isi di Toko Tahu\n")
	na = input("Mencari Jumlah isi : ")

	if na in tempe:
		print(f"{tempe[na][0]}\t   |   {tempe[na][1]}\t   |   Rp.{tempe[na][2]}\t   | {na} Buah\t   |")

	else:
		print(f"Jumlah {na} tidak ada di Toko Tahu")

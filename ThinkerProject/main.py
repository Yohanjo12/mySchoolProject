
from tkinter import Tk,ttk

my_apps = Tk()

my_apps.title("My First Python Apps")
my_apps.resizable(True, True)



label1 = ttk.Label(my_apps, text="Nama Lengkap \t:")
label1.grid(column=0, row=0)
label2 = ttk.Label(my_apps, text="Tanggal Lahir \t:")
label2.grid(column=0, row=1)
label3 = ttk.Label(my_apps, text="Alamat \t: ")
label3.grid(column=0, row=2)
label4 = ttk.Label(my_apps, text="Tempat Lahir \t: ")
label4.grid(column=0, row=3)
label5 = ttk.Label(my_apps, text="Agama \t: ")
label5.grid(column=0, row=4)
label6 = ttk.Label(my_apps, text="Nomor Hp \t: ")
label6.grid(column=0, row=5)
label7 = ttk.Label(my_apps, text="Kode Pos \t: ")
label7.grid(column=0, row=6)
label8 = ttk.Label(my_apps, text="Perkejaan \t: ")
label8.grid(column=0, row=7)

def change_color():
	button1.configure(text= 'Color Has Been Changed')
	label1.configure(foreground='Magenta')
	label1.configure(text='Nama Lengkap \t:')
	label2.configure(foreground='Magenta')
	label2.configure(text="Tanggal Lahir \t:")
	label3.configure(foreground='Magenta')
	label3.configure(text="Alamat \t: ")
	label4.configure(foreground='Magenta')
	label4.configure(text="Tempat Lahir \t: ")
	label5.configure(foreground='Magenta')
	label5.configure(text="Agama \t: ")
	label6.configure(foreground='Magenta')
	label6.configure(text="Nomor Hp \t: ")
	label7.configure(foreground='Magenta')
	label7.configure(text="Kode Pos \t: ")
	label8.configure(foreground='Magenta')
	label8.configure(text="Perkejaan \t: ")

button1 = ttk.Button(my_apps, text="change Color", command=change_color)
button1.grid(row=8, column=0)

if __name__ == "__main__":
	my_apps.mainloop()

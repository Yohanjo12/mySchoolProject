from json import load, dump
from tkinter import Tk, ttk, StringVar

q = "all.json"

student = {}
def faiz():
	global student

	with open(q) as rider:
		student = load(rider)

	return True


def decade():
	global student

	with open(q, 'w') as j:
		dump(student, j)

	return True


myApps = Tk()
myApps.title("My Toko Tahu")
#myApps.resizable(False,False)

label1 = ttk.Label(myApps, text="Masak Goreng/Rebus")
label1.grid(column=0, row=0)

label2 = ttk.Label(myApps, text="Jumlah Tahu")
label2.grid(column=1, row=0)

label3 = ttk.Label(myApps, text="Pilih Rasa")
label3.grid(column=2, row=0)

label4 = ttk.Label(myApps, text="")
label4.grid(column=0, row=1)

label5 = ttk.Label(myApps, text="")
label5.grid(column=1, row=1)

label6 = ttk.Label(myApps, text="")
label6.grid(column=2, row=1)

label7 = ttk.Label(myApps, text="")
label7.grid(column=3, row=1)

def action_button1():
	global counterButton1, student
	global data_name
	button1.configure(text="Already Clicked")
	if counterButton1 % 2 == 0:
		label1.configure(foreground = "magenta")
		label2.configure(foreground = "magenta")
		label3.configure(foreground = "magenta")
		label4.configure(foreground = "red")
		label5.configure(foreground = "red")
		label6.configure(foreground = "red")

	else:
		label1.configure(foreground = "gold")
		label2.configure(foreground = "gold")
		label3.configure(foreground = "gold")
		label4.configure(foreground = "yellow")
		label5.configure(foreground = "yellow")
		label6.configure(foreground = "yellow")
		
	label4.configure(text=data_name.get())
	label5.configure(text=data_age.get())
	label6.configure(text=data_spicy.get())
	counterButton1 += 1
	student[data_name.get()] = data_age.get(), data_spicy.get()
	decade()
	print(student)

counterButton1 = 0
button1 = ttk.Button(myApps, text="Click Here", command=action_button1)
button1.grid(column=3, row=2)

data_name = StringVar()
data_name_entry = ttk.Entry(myApps, width=12, textvariable=data_name)
data_name_entry.grid(column=0, row=2)

#data_name = input("Name : ")

data_name_entry.focus()


data_age = StringVar()
#data_age_combobox = ttk.Combobox(myApps, width=12, textvariable=data_age)
data_age_combobox = ttk.Combobox(myApps, width=12, textvariable=data_age, state = "readonly")

data_age_combobox['values'] = ["Jumlah",1,10,20,30,40,50,"Tahu"]
data_age_combobox.grid(column=1, row=2)
data_age_combobox.current(1)

data_spicy = StringVar()
data_spicy_combobox = ttk.Combobox(myApps, width=12, textvariable=data_spicy, state = "readonly")
data_spicy_combobox['values'] = ["Pedas", "Biasa", "Very Spicy"]
data_spicy_combobox.grid(column=2, row=2)
data_spicy_combobox.current(0)


if __name__ == "__main__":
	myApps.mainloop()


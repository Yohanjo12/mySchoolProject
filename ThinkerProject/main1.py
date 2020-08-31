
from tkinter import Tk, ttk, StringVar

student = {}

myApps = Tk()
myApps.title("My Apps")
#myApps.resizable(False,False)

label1 = ttk.Label(myApps, text="Enter Name")
label1.grid(column=0, row=0)

label2 = ttk.Label(myApps, text="My Age")
label2.grid(column=1, row=0)


def action_button1():
	global counterButton1, student
	global data_name
	button1.configure(text="Already Clicked")
	if counterButton1 % 2 == 0:
		label1.configure(foreground = "magenta")
		label2.configure(foreground = "magenta")

	else:
		label1.configure(foreground = "gold")
		label2.configure(foreground = "magenta")

	label1.configure(text=data_name.get())
	label2.configure(text=data_age.get())
	counterButton1 += 1
	student[data_name.get()] = data_age.get()
	print(student)

counterButton1 = 0
button1 = ttk.Button(myApps, text="Click Here", command=action_button1)
button1.grid(column=2, row=1)

data_name = StringVar()
data_name_entry = ttk.Entry(myApps, width=12, textvariable=data_name)
data_name_entry.grid(column=0, row=1)

#data_name = input("Name : ")

data_name_entry.focus()


data_age = StringVar()
#data_age_combobox = ttk.Combobox(myApps, width=12, textvariable=data_age)
data_age_combobox = ttk.Combobox(myApps, width=12, textvariable=data_age, state = "readonly")

data_age_combobox['values'] = ["YOUNGER",12,13,14,15,"OLDER"]
data_age_combobox.grid(column=1, row=1)
data_age_combobox.current(0)

if __name__ == "__main__":
	myApps.mainloop()


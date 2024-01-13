import tkinter as tk
import tkinter.messagebox
import time
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Countdown Timer')
frame = tk.Frame(master=window, bg = "White", padx = 10,)
frame.pack()
entry = tk.Entry(master = frame, relief = SUNKEN, borderwidth = 10, width = 20)
entry.grid(row = 0, column = 0, columnspan = 3, ipady = 2, pady = 2)

hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

hour.set("00")
minute.set("00")
second.set("00")

def myclick(number):
	hour_box = entry(textvariable = hour)
	mins_box = entry(textvariable = minute)
	sec_box = entry(textvariable = second)


def countdowntimer():
	try:
		user_input = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		tkinter.messagebox.showinfo('', 'Invalid!')

	while user_input > -1:
		mins, secs = divmod(user_input, 60)
		hour = 0
		if mins > 60:
			hours, mins = divmod(mins, 60)
		
		hour.set("{0:2d}".format(hour))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		root.update()
		time.sleep(1)

		if(user_input == 0):
			tkinter.messagebox.showinfo("Time Countdown", "Time Over")
		user_input -= 1


# Buttons for Numbers

button_1 = tk.Button(master = frame, text = '1', padx = 15, pady = 5, width = 3, command = lambda: myclick(1))
button_1.grid(row = 1, column = 0, pady = 2)

button_2 = tk.Button(master = frame, text = '2', padx = 15, pady = 5, width = 3, command = lambda: myclick(2))
button_2.grid(row = 1, column = 1, pady = 2)

button_3 = tk.Button(master = frame, text = '3', padx = 15, pady = 5, width = 3, command = lambda: myclick(3))
button_3.grid(row = 1, column = 2, pady = 2)

button_4 = tk.Button(master = frame, text = '4', padx = 15, pady = 5, width = 3, command = lambda: myclick(4))
button_4.grid(row = 2, column = 0, pady = 2)

button_5 = tk.Button(master = frame, text = '5', padx = 15, pady = 5, width = 3, command = lambda: myclick(5))
button_5.grid(row = 2, column = 1, pady = 2)

button_6 = tk.Button(master = frame, text = '6', padx = 15, pady = 5, width = 3, command = lambda: myclick(6))
button_6.grid(row = 2, column = 2, pady = 2)

button_7 = tk.Button(master = frame, text = '7', padx = 15, pady = 5, width = 3, command = lambda: myclick(7))
button_7.grid(row = 3, column = 0, pady = 2)

button_8 = tk.Button(master = frame, text = '8', padx = 15, pady = 5, width = 3, command = lambda: myclick(8))
button_8.grid(row = 3, column = 1, pady = 2)

button_9 = tk.Button(master = frame, text = '9', padx = 15, pady = 5, width = 3, command = lambda: myclick(9))
button_9.grid(row = 3, column = 2, pady = 2)

button_0 = tk.Button(master = frame, text = '0', padx = 15, pady = 5, width = 3, command = lambda: myclick(0))
button_0.grid(row = 4, column = 1, pady = 2)


# Buttons for Editing/Getting answers

button_start = tk.Button(master = frame, text = "Start", padx = 15, pady = 5, width = 3, command = countdowntimer)
button_start.grid(row = 5, column = 2, pady = 2)

window.mainloop()
from tkinter import *
from tkinter import font

root = Tk()
root.title("Trial frame")
root.geometry("700x700")

diplay_font = font.Font(family = "Arial", size = 30)

main_frame = Frame(root)
main_frame.pack(pady = 15, padx = 15)

def switch_item_1():
	if button_1['text'] == ' ' or button_1['text'] == "O":
		button_1['text'] = "X"
	elif button_1['text'] == "X" :
		button_1['text'] = "O"
def switch_item_2():
	if button_2['text'] == ' ' or button_2['text'] == "O":
		button_2['text'] = "X"
	elif button_2['text'] == "X" :
		button_2['text'] = "O"
def switch_item_3():
	if button_3['text'] == ' ' or button_3['text'] == "O":
		button_3['text'] = "X"
	elif button_3['text'] == "X" :
		button_3['text'] = "O"
def switch_item_4():
	if button_4['text'] == ' ' or button_4['text'] == "O":
		button_4['text'] = "X"
	elif button_4['text'] == "X" :
		button_4['text'] = "O"
def switch_item_5():
	if button_5['text'] == ' ' or button_5['text'] == "O":
		button_5['text'] = "X"
	elif button_5['text'] == "X" :
		button_5['text'] = "O"
def switch_item_6():
	if button_6['text'] == ' ' or button_6['text'] == "O":
		button_6['text'] = "X"
	elif button_6['text'] == "X" :
		button_6['text'] = "O"
def switch_item_7():
	if button_7['text'] == ' ' or button_7['text'] == "O":
		button_7['text'] = "X"
	elif button_7['text'] == "X" :
		button_7['text'] = "O"
def switch_item_8():
	if button_8['text'] == ' ' or button_8['text'] == "O":
		button_8['text'] = "X"
	elif button_8['text'] == "X" :
		button_8['text'] = "O"
def switch_item_9():
	if button_9['text'] == ' ' or button_9['text'] == "O":
		button_9['text'] = "X"
	elif button_9['text'] == "X":
		button_9['text'] = "O"

button_1 = Button(main_frame, text = " ",font=diplay_font, command = switch_item_1, width = 8, height = 3)
button_2 = Button(main_frame, text = " ",font=diplay_font, command = switch_item_2, width = 8, height = 3)
button_3 = Button(main_frame, text = " ",font=diplay_font, command = switch_item_3, width = 8, height = 3)
button_4 = Button(main_frame, text = " ",font=diplay_font, command = switch_item_4, width = 8, height = 3)
button_5 = Button(main_frame, text = " ",font=diplay_font, command = switch_item_5, width = 8, height = 3)
button_6 = Button(main_frame, text = " ",font=diplay_font, command = switch_item_6, width = 8, height = 3)
button_7 = Button(main_frame, text = " ",font=diplay_font, command = switch_item_7, width = 8, height = 3)
button_8 = Button(main_frame, text = " ",font=diplay_font, command = switch_item_8, width = 8, height = 3)
button_9 = Button(main_frame, text = " ",font=diplay_font, command = switch_item_9, width = 8, height = 3)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

root.mainloop()
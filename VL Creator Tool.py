
# === Setup =======================================================================
import tkinter as tk
from tkinter import StringVar, IntVar
import csv

root = tk.Tk()
root.title("VL Creator Tool")
root.resizable(False, False)
root.geometry("500x400+2500+300")

bookSelect = tk.Frame(root, width=500)
book1 = tk.Frame(bookSelect, bg="#E5E7E9", width=100)
book2 = tk.Frame(bookSelect, bg="#ECF0F1", width=100)
book3 = tk.Frame(bookSelect, bg="#E5E7E9", width=100)
book4 = tk.Frame(bookSelect, bg="#ECF0F1", width=100)
book5 = tk.Frame(bookSelect, bg="#E5E7E9", width=100)

wordSelectCanvas = tk.Canvas(root, bg="white")
wordSelectFrame = tk.Frame(wordSelectCanvas, bg="white")
vscrollbar = tk.Scrollbar(root, orient="vertical", command=wordSelectCanvas.yview)
hscrollbar = tk.Scrollbar(root, orient="horizontal", command=wordSelectCanvas.xview)
wordSelectCanvas.configure(yscrollcommand=vscrollbar.set)
wordSelectCanvas.configure(xscrollcommand=hscrollbar.set)


#-----------------------------------------------------------------------------------



# === Retrieve Entries from Files ==================================================
def submitBook(bookName, textA, textB):
	if (bookName == "SBS 1"):
		with open('Books/Side By Side/sbs1.csv') as csv_sbs1:
			csv_reader = csv.reader(csv_sbs1, delimiter=';')
			for row in csv_reader:
				if ((row[0] >= textA) and (row[0] <= textB)):
					with open('dataHandler.csv', mode='a', newline="") as dataHandler:
						dataHandler_write = csv.writer(dataHandler, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
						dataHandler_write.writerow([row[1], row[2], row[3]])
					print(row[1], row[2], row[3])
	if (bookName == "Phonics A"):
		with open('Books/Phonics/phonicsA.csv') as csv_phonA:
			csv_reader = csv.reader(csv_phonA, delimiter=';')
			for row in csv_reader:
				if ((row[0] >= textA) and (row[0] <= textB)):
					with open('dataHandler.csv', mode='a', newline="") as dataHandler:
						dataHandler_write = csv.writer(dataHandler, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
						dataHandler_write.writerow([row[1], row[2], row[3]])
					print(row[1], row[2], row[3])
	if (bookName == "Reading 1"):
		with open('Books/Reading/reading1.csv') as csv_read1:
			csv_reader = csv.reader(csv_read1, delimiter=';')
			for row in csv_reader:
				if ((row[0] >= textA) and (row[0] <= textB)):
					with open('dataHandler.csv', mode='a', newline="") as dataHandler:
						dataHandler_write = csv.writer(dataHandler, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
						dataHandler_write.writerow([row[1], row[2], row[3]])
					print(row[1], row[2], row[3])
	if (bookName == "Writing 1"):
		with open('Books/Writing/writing1.csv') as csv_write1:
			csv_reader = csv.reader(csv_write1, delimiter=';')
			for row in csv_reader:
				if ((row[0] >= textA) and (row[0] <= textB)):
					with open('dataHandler.csv', mode='a', newline="") as dataHandler:
						dataHandler_write = csv.writer(dataHandler, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
						dataHandler_write.writerow([row[1], row[2], row[3]])
					print(row[1], row[2], row[3])
	if (bookName == "SBS WB 1"):
		with open('Books/Side By Side Workbook/sbswork1.csv') as csv_sbswb1:
			csv_reader = csv.reader(csv_sbswb1, delimiter=';')
			for row in csv_reader:
				if ((row[0] >= textA) and (row[0] <= textB)):
					with open('dataHandler.csv', mode='a', newline="") as dataHandler:
						dataHandler_write = csv.writer(dataHandler, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
						dataHandler_write.writerow([row[1], row[2], row[3]])
					print(row[1], row[2], row[3])
#-----------------------------------------------------------------------------------


# === Book Select Functions ================================================================
def handleStuff2():
	with open('dataHandler.csv', mode='w', newline="") as dataHandler:
		dataHandler_write = csv.writer(dataHandler, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		dataHandler_write.writerow([])
	submitBook(readDrop1(), readText1a(), readText1b())
	submitBook(readDrop2(), readText2a(), readText2b())
	submitBook(readDrop3(), readText3a(), readText3b())
	submitBook(readDrop4(), readText4a(), readText4b())
	submitBook(readDrop5(), readText5a(), readText5b())
	clearDisplay()
	displayData()
	# --- Update Status Bar ---
	bookStats1 = readDrop1() + ": p" + readText1a() + "-" + readText1b()
	bookStats2 = readDrop2() + ": p" + readText2a() + "-" + readText2b()
	bookStats3 = readDrop3() + ": p" + readText3a() + "-" + readText3b()
	bookStats4 = readDrop4() + ": p" + readText4a() + "-" + readText4b()
	bookStats5 = readDrop5() + ": p" + readText5a() + "-" + readText5b()
	statusText.set(bookStats1 + "  |  " + bookStats2 + "  |  " + bookStats3 + "  |  " + bookStats4 + "  |  " + bookStats5)

# ---Book 1---
def readDrop1():
	drop1read = dropVal1.get()
	return drop1read
def readText1a():
	text1a = entry1a.get("1.0", "end-1c")
	return text1a
def readText1b():
	text1b = entry1b.get("1.0", "end-1c")
	return text1b
# --- Book 2---
def readDrop2():
	drop2read = dropVal2.get()
	return drop2read
def readText2a():
	text2a = entry2a.get("1.0", "end-1c")
	return text2a
def readText2b():
	text2b = entry2b.get("1.0", "end-1c")
	return text2b
# ---Book 3---
def readDrop3():
	drop3read = dropVal3.get()
	return drop3read
def readText3a():
	text3a = entry3a.get("1.0", "end-1c")
	return text3a
def readText3b():
	text3b = entry3b.get("1.0", "end-1c")
	return text3b
# ---Book 4---
def readDrop4():
	drop4read = dropVal4.get()
	return drop4read
def readText4a():
	text4a = entry4a.get("1.0", "end-1c")
	return text4a
def readText4b():
	text4b = entry4b.get("1.0", "end-1c")
	return text4b
# ---Book 5---
def readDrop5():
	drop5read = dropVal5.get()
	return drop5read
def readText5a():
	text5a = entry5a.get("1.0", "end-1c")
	return text5a
def readText5b():
	text5b = entry5b.get("1.0", "end-1c")
	return text5b
#-----------------------------------------------------------------------------------


def displayData():
	buttonBuildVL.pack(side="bottom", pady=10)
	vscrollbar.pack(side="right", fill="y")
	hscrollbar.pack(side="bottom", anchor="w", fill="x")
	wordSelectCanvas.pack(side="left", pady=10)
	wordSelectCanvas.create_window((0, 0), window=wordSelectFrame, anchor='n')
	wordSelectFrame.bind("<Configure>", scroll_CB)
	with open('dataHandler.csv', mode='r') as dataHandler:
		data=list(csv.reader(dataHandler, delimiter=';', quotechar='"'))
		for row in data:
			if (len(row)>0):
				word = StringVar()
				word.set(row)
				display = tk.Checkbutton(wordSelectFrame, textvariable=word, fg="blue", bg="white", bd=1, relief="sunken")
				display.pack(side="top", anchor="w")

		

def clearDisplay():
	for display in wordSelectFrame.winfo_children():
		display.destroy()

def scroll_CB(event):
	wordSelectCanvas.configure(scrollregion=wordSelectCanvas.bbox("all"))
	wordSelectCanvas.xview_moveto(0)


# ---Titles ---
bookTitle1 = tk.Label(book1, text="Book 1", bg="#E5E7E9", fg="purple")
bookTitle2 = tk.Label(book2, text="Book 2", bg="#ECF0F1", fg="purple")
bookTitle3 = tk.Label(book3, text="Book 3", bg="#E5E7E9", fg="purple")
bookTitle4 = tk.Label(book4, text="Book 4", bg="#ECF0F1", fg="purple")
bookTitle5 = tk.Label(book5, text="Book 5", bg="#E5E7E9", fg="purple")
# ---Drop Menus---
options = ["SBS 1", "Phonics A", "Reading 1", "Writing 1", "SBS WB 1"]
dropVal1 = StringVar()
dropVal2 = StringVar()
dropVal3 = StringVar()
dropVal4 = StringVar()
dropVal5 = StringVar()
drop1 = tk.OptionMenu(book1, dropVal1, *options)
drop2 = tk.OptionMenu(book2, dropVal2, *options)
drop3 = tk.OptionMenu(book3, dropVal3, *options)
drop4 = tk.OptionMenu(book4, dropVal4, *options)
drop5 = tk.OptionMenu(book5, dropVal5, *options)
# ---Page Number Entries---
entry1a = tk.Text(book1, height=1, width=4)
entry1b = tk.Text(book1, height=1, width=4)
entry2a = tk.Text(book2, height=1, width=4)
entry2b = tk.Text(book2, height=1, width=4)
entry3a = tk.Text(book3, height=1, width=4)
entry3b = tk.Text(book3, height=1, width=4)
entry4a = tk.Text(book4, height=1, width=4)
entry4b = tk.Text(book4, height=1, width=4)
entry5a = tk.Text(book5, height=1, width=4)
entry5b = tk.Text(book5, height=1, width=4)
#-----------------------------------------------------------------------------------

# === Book Select Bar ==============================================================
bookSelect.pack(side="top", pady=10)
# ---Book 1---
book1.grid(row=0, column=0)
bookTitle1.grid(row=0, column=0, columnspan=2)
drop1.grid(row=1, column=0, columnspan=2)
entry1a.grid(row=2, column=0, padx=5)
entry1b.grid(row=2, column=1, padx=5)
# ---Book 2---
book2.grid(row=0, column=1)
bookTitle2.grid(row=0, column=0, columnspan=2)
drop2.grid(row=1, column=0, columnspan=2)
entry2a.grid(row=2, column=0, padx=5)
entry2b.grid(row=2, column=1, padx=5)
# ---Book 3---
book3.grid(row=0, column=2)
bookTitle3.grid(row=0, column=0, columnspan=2)
drop3.grid(row=1, column=0, columnspan=2)
entry3a.grid(row=2, column=0, padx=5)
entry3b.grid(row=2, column=1, padx=5)
# ---Book 4---
book4.grid(row=0, column=3)
bookTitle4.grid(row=0, column=0, columnspan=2)
drop4.grid(row=1, column=0, columnspan=2)
entry4a.grid(row=2, column=0, padx=5)
entry4b.grid(row=2, column=1, padx=5)
# ---Book 5---
book5.grid(row=0, column=4)
bookTitle5.grid(row=0, column=0, columnspan=2)
drop5.grid(row=1, column=0, columnspan=2)
entry5a.grid(row=2, column=0, padx=5)
entry5b.grid(row=2, column=1, padx=5)


# --- Submit ---
buttonSubmit = tk.Button(root, width=30, fg="purple", text="Submit", command=handleStuff2)
buttonSubmit.pack()
#-----------------------------------------------------------------------------------

# === Status Bar ===
statusText = StringVar(root)
statusText.set('Select books and pages...')
statusBar = tk.Label(root, textvariable=statusText, fg="blue", bd=1, relief="sunken", anchor="w")
statusBar.pack(side="bottom", fill="x")
#-----------------------------------------------------------------------------------

buttonBuildVL = tk.Button(root, width=30, fg="purple", text="Build!")







# === Run It! ===
root.mainloop()
#-----------------------------------------------------------------------------------
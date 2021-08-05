from tkinter import *

root = Tk()

root.title('Project Timer')
root.geometry("600x400")

frame = LabelFrame(root, text="Hello", padx=5, pady=5)
frame.pack(padx=10, pady=10)

test = Button(frame, text="Test")
test.pack()
 

root.mainloop()
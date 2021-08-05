from tkinter import *

root = Tk()

# Inputs
e = Entry(root)



# Input formatting
e.grid(row=2, column=0)



# Screen Button functions
def resetButtonStates(buttonClicked):
    mainButton.config(state=NORMAL)
    graphButton.config(state=NORMAL)

    buttonClicked.config(state = DISABLED)

def mainScreen():
    resetButtonStates(mainButton)
    myLabel = Label(root, text="Main screen")
    myLabel.grid(row=1)

def graphScreen():
    resetButtonStates(graphButton)
    myLabel = Label(root, text="Graph Screen")
    myLabel.grid(row=1)

def submitButton():
    inputLabel.config(text=e.get())

# Buttons
mainButton = Button(root, text="Main", padx=20, pady=10, command=mainScreen)
graphButton = Button(root, text="Graph", padx=20, pady=10, command=graphScreen)
submitInput = Button(root, text="Submit", command=submitButton)


# Button formatting
mainButton.grid(row=0, column=0)
graphButton.grid(row=0, column=1)
submitInput.grid(row=4, column=0)



# Labels
inputLabel = Label(root)


# Label formatting
inputLabel.grid(row=3,column=0)




root.mainloop()

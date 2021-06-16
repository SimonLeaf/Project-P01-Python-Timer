from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime

#Window setup
root = Tk()
root.geometry("600x400")


#Global variables
running = FALSE
started = FALSE
counter = 0


#Functions
def SetupStopwatch(timerLabel):
    global counter
    if counter < 1:
        display = "0"
    else:
        display = str(counter)
    
    timerLabel.config(text=display)

def Timer(timerLabel):
    global counter
    global running

    timeElapsed = datetime.datetime.fromtimestamp(counter)

    if counter < 10:
        timerLabel.config(text=timeElapsed.strftime('%M:%S'))
    else:
        timerLabel.config(text=timeElapsed.strftime('%H:%M:%S'))
    
    timerLabel.after(1000,lambda:Timer(timerLabel))
    
    if running:
        counter +=1

def StartTimer(timerLabel):
    global running
    global started
    running = TRUE
    if not started:
        SetupStopwatch(timerLabel)
        Timer(timerLabel)
        started = TRUE
    startButton.config(state=DISABLED)
    pauseButton.config(state=NORMAL)
    
def PauseTimer():
    global running
    running = FALSE
    startButton.config(state=NORMAL)
    pauseButton.config(state=DISABLED)

def FinishTimer():
    PauseTimer()
    response = messagebox.askyesno("Finish Timer", "Are you sure?")


#Create notebook
app_notebook = ttk.Notebook(root)
app_notebook.grid(row=1, column=1)


#Create tabs
main_menu = Frame(app_notebook, width=600, height=400)
timer_menu = Frame(app_notebook, width=600, height=400)
music_menu = Frame(app_notebook, width=600, height=400)
graph_menu = Frame(app_notebook, width=600, height=400)

main_menu.grid(row=2)
timer_menu.grid(row=2)
music_menu.grid(row=2)
graph_menu.grid(row=2)


#Add tabs to notebook
app_notebook.add(main_menu, text="Main")
app_notebook.add(timer_menu, text="Timer")
app_notebook.add(music_menu, text="Music")
app_notebook.add(graph_menu, text="Graph")


# Main Menu Screen
label1 = Label(main_menu, text="grid test 1")
label1.grid(row=1, column=1, sticky=NSEW)

label2 = Label(main_menu, text="grid test 2")
label2.grid(row=1, column=2, sticky=NSEW)

label3 = Label(main_menu, text="grid test 3")
label3.grid(row=2, column=1, sticky=NSEW)

label4 = Label(main_menu, text="grid test 4")
label4.grid(row=2, column=2, sticky=NSEW)

main_menu.grid_rowconfigure(0, weight=1)
main_menu.grid_rowconfigure(3, weight=1)
main_menu.grid_columnconfigure(0, weight=1)
main_menu.grid_columnconfigure(3, weight=1)


#Timer Screen
timerLabel = Label(timer_menu, text="")
timerLabel.grid(row=1, columnspan=3)

startButton = Button(timer_menu, text="Start", width=15, command=lambda:StartTimer(timerLabel))
pauseButton = Button(timer_menu, text="Pause", width=15, state=DISABLED, command=PauseTimer)
finishButton = Button(timer_menu, text="Finish", width=15, command=FinishTimer)

startButton.grid(row=2, column=1)
pauseButton.grid(row=2, column=2)
finishButton.grid(row=2, column=3)

root.mainloop()
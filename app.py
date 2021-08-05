from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime

#Window setup
root = Tk()
root.geometry("600x400")


#Global stopwatch variables
running = FALSE
started = FALSE
counter = 0


#Global record label
activityID = 0
activityName = "Test"

#Stopwatch Functions
def SetupStopwatch(timerLabel):
    global counter
    if counter < 1:
        display = "0"
    else:
        display = str(counter)
    
    timerLabel.config(text=datetime.datetime.fromtimestamp(counter).strftime('%M:%S'))
    
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

def SaveRecord():
    global activityName
    #insert new record
    completed = messagebox.askyesno("Record Saved", 
        "You have completed " + 
        datetime.datetime.fromtimestamp(counter).strftime('%M') + 
        " minutes of time on " + 
        activityName +
        "\n\nHave you completed this activity?")
    #if completed:
        #modify activity completed
    ResetTimer()

def ResetTimer():
    global counter
    global activityID
    counter = 0
    SetupStopwatch(timerLabel)
    activityID = 0
    app_notebook.select(0)

def FinishTimer():
    PauseTimer()
    finished = messagebox.askyesnocancel("Finish Timer", "Are you sure?")
    if finished:
        SaveRecord()
    else:
        ResetTimer()


#Notebook Functions
def HideTab(index):
    app_notebook.tab(index, state=HIDDEN)

def EnterStopwatch():
    global activityID
    activityID = 1
    app_notebook.select(2)

#Create notebook
app_notebook = ttk.Notebook(root)
app_notebook.grid(row=1, column=1)


#Create tabs
main_menu = Frame(app_notebook, width=600, height=400)
timer_menu = Frame(app_notebook, width=600, height=400)
stopwatch = Frame(app_notebook, width=600, height=400)
music_menu = Frame(app_notebook, width=600, height=400)
graph_menu = Frame(app_notebook, width=600, height=400)

main_menu.grid(row=2)
timer_menu.grid(row=2)
stopwatch.grid(row=2)
music_menu.grid(row=2)
graph_menu.grid(row=2)


#Add tabs to notebook
app_notebook.add(main_menu, text="Main")
app_notebook.add(timer_menu, text="Timer")
app_notebook.add(stopwatch, text="Stopwatch")
app_notebook.add(music_menu, text="Music")
app_notebook.add(graph_menu, text="Graph")
app_notebook.hide(2)


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

timerButton = Button(timer_menu, text="Start", width=15, command=EnterStopwatch)
timerButton.grid(row=2)


#Stopwatch Screen

timerLabel = Label(stopwatch, text="")
timerLabel.grid(row=1, columnspan=3)

startButton = Button(stopwatch, text="Start", width=15, command=lambda:StartTimer(timerLabel))
pauseButton = Button(stopwatch, text="Pause", width=15, state=DISABLED, command=PauseTimer)
finishButton = Button(stopwatch, text="Finish", width=15, command=FinishTimer)

startButton.grid(row=2, column=1)
pauseButton.grid(row=2, column=2)
finishButton.grid(row=2, column=3)


#Music Screen



#Chart Screen



#Binds
#NotebookTabChanged

def OnTabChange(event):
    if activityID < 1:
        HideTab(2)

app_notebook.bind('<<NotebookTabChanged>>', OnTabChange)

root.mainloop()
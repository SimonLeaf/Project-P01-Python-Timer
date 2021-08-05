from tkinter import *
from tkinter import messagebox
import datetime

root = Tk()

running = FALSE
started = FALSE
counter = 0

timerLabel = Label(root, text="")
timerLabel.grid(row=1, columnspan=3)

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
    #insert new record
    completed = messagebox.askyesno("Record Saved", "You have completed x time on x.\n\nHave you completed this activity?")
    #if completed:
        #modify activity completed
    ResetTimer()


def ResetTimer():
    global counter
    counter = 0
    SetupStopwatch(timerLabel)


def FinishTimer():
    PauseTimer()
    finished = messagebox.askyesnocancel("Finish Timer", "Are you sure?")
    if finished:
        SaveRecord()
    else:
        ResetTimer()
        



startButton = Button(root, text="Start", width=15, command=lambda:StartTimer(timerLabel))
pauseButton = Button(root, text="Pause", width=15, state=DISABLED, command=PauseTimer)
finishButton = Button(root, text="Finish", width=15, command=FinishTimer)

startButton.grid(row=2, column=1)
pauseButton.grid(row=2, column=2)
finishButton.grid(row=2, column=3)
root.mainloop()
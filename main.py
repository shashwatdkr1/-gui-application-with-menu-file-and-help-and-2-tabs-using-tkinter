from time import sleep
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Python GUI")
menu = Menu(root)
menu.add_command(label="File")
menu.add_command(label="Help")
root.config(menu=menu)
tabControl = ttk.Notebook(root)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 1')
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 2')
tabControl.pack(expand=1, fill="both")
theSnakeLabelFrame = ttk.LabelFrame(tab1, text="The Snake")
theSnakeLabelFrame.grid(column=0, row=0, padx=8, pady=4)
disabledCheckBox = ttk.Checkbutton(theSnakeLabelFrame, 
text="Disabled", state="disabled")
disabledCheckBox.grid(column=0, row=0, sticky=W)
checkBoxVar1 = IntVar(value=0)
checkBoxVar2 = IntVar(value=0)
unCheckedCheckBox = ttk.Checkbutton(theSnakeLabelFrame, 
text="Unchecked",variable=checkBoxVar1)
unCheckedCheckBox.grid(column=1, row=0, sticky=W)
enabledCheckBox = ttk.Checkbutton(theSnakeLabelFrame, 
text="Enabled", state="enabled",variable=checkBoxVar2)
enabledCheckBox.grid(column=2, row=0, sticky=W)
blueRadioButton = ttk.Radiobutton(theSnakeLabelFrame, text="Blue", 
value=0)
blueRadioButton.grid(column=0, row=1, sticky=W)
redRadioButton = ttk.Radiobutton(theSnakeLabelFrame, text="Red", 
value=1)
redRadioButton.grid(column=2, row=1, sticky=W)
goldRadioButton = ttk.Radiobutton(theSnakeLabelFrame, text="Gold", 
value=2)
goldRadioButton.grid(column=1, row=1, sticky=W)
progressBar = ttk.Progressbar(tab1, orient="horizontal", length=200, 
mode="determinate")
progressBar.grid(column=0, row=1, padx=8, pady=4)
progressBarLabelFrame = ttk.LabelFrame(theSnakeLabelFrame, 
text="Progress Bar")
progressBarLabelFrame.grid(column=0, row=2,sticky=W)
runProgressBarButton = ttk.Button(progressBarLabelFrame, text="Run 
Progress Bar",command=progressBar.start)
runProgressBarButton.grid(column=0, row=0, sticky=W)
startProgressBarButton = ttk.Button(progressBarLabelFrame, 
text="Start Progress Bar",command=progressBar.start)
startProgressBarButton.grid(column=0, row=1, sticky=W)
stopImmediatelyButton = ttk.Button(progressBarLabelFrame, text="Stop 
Immediately",command=progressBar.stop)
stopImmediatelyButton.grid(column=0, row=2, sticky=W)
def delayStop():
 progressBar.after(1000,progressBar.stop())
 
stopAfterSecondButton = ttk.Button(progressBarLabelFrame, text="Stop 
After Second",command=delayStop)
stopAfterSecondButton.grid(column=0, row=3, sticky=W)
root.mainloop()
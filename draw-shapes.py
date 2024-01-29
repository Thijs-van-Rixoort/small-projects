### Imports ###

import turtle
import tkinter as tk


### Functions ###

def userInput(event=""):
    """userInput checks wether the input of the user is valid or not. 
       It also checks wether there is a shape on the canvas or not. 
       If this is the case, the drawn shape is deleted"""

    global counter

    try:
        if counter != 0:
            t.clear()
        counter = 1

        if entry.get().lower() == "circle":
            drawShape(entry.get().lower())
        else:
            drawShape(shapeDict[entry.get().lower()])

    except:
        root.focus()
        entry.delete(0, tk.END)
        entry.config(fg="#472e22")
        entry.insert(0, "This is not a valid shape!")

def drawShape(amountOfCornersAndLength):
    """drawShape gives the turtle library the instructions to draw the shape that the user inputs"""

    global hexcode

    entry.delete(0, tk.END)
    root.focus()

    t.color(hexcode)

    if fillCheck.get() == True:
        t.begin_fill()

    if amountOfCornersAndLength == "circle":
        t.circle(60)
    else:
        for i in range(amountOfCornersAndLength[0]):
            t.forward(amountOfCornersAndLength[1])
            t.left(360/amountOfCornersAndLength[0])

    t.end_fill()

def colorUpdate(event=""):
    """colorUpdate updates the color of the hexcode label and the small canvas right of the color sliders"""

    global hexcode
    hexcode = "#%02x%02x%02x" % (redSlider.get(), greenSlider.get(), blueSlider.get())
    colorCanvas.config(bg=hexcode)
    hexcodeLabel.config(text=hexcode)

def entryFocusIn(event=""):
    """entryFocusIn checks wether the grey placeholder text is in the entry widget when the user clicks on the entry widget.
       If it is, it gets deleted and the entry textcolor is set to black"""

    if entry.get() == "Type your shape here" or entry.get() == "This is not a valid shape!":
        entry.config(fg="white")
        entry.delete(0, tk.END)

def entryFocusOut(event=""):
    """entryFocusOut checks wether the entry widget is empty or not.
       If it is, the textcolor is set to grey and the text 'Type your shape here' is inserted"""
    if entry.get() == "":
        entry.config(fg="white")
        entry.insert(0, "Type your shape here")



### Variables ###

shapeDict = {"triangle": [3, 100], "square": [4, 100], "pentagon": [5, 75], "hexagon": [6, 75], "septagon": [7, 60], "octagon": [8, 50], "nonagon": [9, 45], "decagon": [10, 35]}
counter = 0
hexcode = "#000000"

#initiate tkinter window
root = tk.Tk()
root.config(bg="#223D47")
root.title("Draw Shapes")

#initiate tkinter canvas
canvas = tk.Canvas(master = root, width=500, height=500)
canvas.pack(fill=tk.X, side=tk.TOP)

#initiate turtle embedded mode
t = turtle.RawTurtle(canvas)
t.hideturtle()

#Frames for different options
inputFrame = tk.Frame(master=root, bg="#223D47")
inputFrame.pack(fill=tk.X)
colorFrame = tk.Frame(master=root, bg="#223D47")
colorFrame.pack(fill=tk.X)

#Shape entry label and entry
entry = tk.Entry(master=inputFrame, width=34, relief=tk.FLAT, bg="#325A68", fg="white", insertbackground="white", font="Arial 14")
entry.insert(0, "Type your shape here")
entry.bind('<FocusIn>', entryFocusIn)
entry.bind('<FocusOut>', entryFocusOut)
entry.pack(side=tk.LEFT, padx=(5,0), pady=(5,0))

#Enter button for shape entry
entryButton = tk.Button(master=inputFrame, height=1, text="Enter input", command=userInput, bg="#325A68", fg="white", activebackground="#223D47", activeforeground="White", relief=tk.FLAT, overrelief=tk.FLAT)
entryButton.pack(side=tk.RIGHT, padx=(0,5), pady=(5,0))

#Color sliders
redSlider = tk.Scale(master=colorFrame, from_=0, to=255, showvalue=0, orient=tk.HORIZONTAL, command=colorUpdate, highlightthickness=0, bd=0, bg="white", sliderrelief=tk.FLAT, troughcolor="#325A68", sliderlength=23, width=15)
redSlider.pack(side=tk.LEFT, padx=(5,0), pady=(2,5))
greenSlider = tk.Scale(master=colorFrame, from_=0, to=255, showvalue=0, orient=tk.HORIZONTAL, command=colorUpdate, highlightthickness=0, bd=0, bg="white", sliderrelief=tk.FLAT, troughcolor="#325A68", sliderlength=23, width=15)
greenSlider.pack(side=tk.LEFT, padx=(5,0), pady=(2,5))
blueSlider = tk.Scale(master=colorFrame, from_=0, to=255, showvalue=0, orient=tk.HORIZONTAL, command=colorUpdate, highlightthickness=0, bd=0, bg="white", sliderrelief=tk.FLAT, troughcolor="#325A68", sliderlength=23, width=15)
blueSlider.pack(side=tk.LEFT, padx=(5,0), pady=(2,5))

#Color preview canvas and hexcode label
colorCanvas = tk.Canvas(master=colorFrame, width=15, height=15, bg="#000000", highlightthickness=0)
colorCanvas.pack(side=tk.LEFT, padx=(5,0), pady=(2,5))
hexcodeLabel = tk.Label(master=colorFrame, text="#000000", bg="#223D47", fg="white")
hexcodeLabel.pack(side=tk.LEFT, pady=(2,5))

#Fillshape checkbox
fillCheck = tk.BooleanVar()
fillButton = tk.Checkbutton(master=colorFrame, text="Fill Shape", variable=fillCheck,  bg="#223D47", fg="white", selectcolor="#325A68", activebackground="#223D47", activeforeground="white", borderwidth=0)
fillButton.pack(side=tk.RIGHT, padx=(0,3), pady=(0,5))

root.bind('<Return>', userInput)
root.mainloop()
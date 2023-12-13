import tkinter as tk
from tkinter import *
import sound

#initializes the window
root = tk.Tk()
root.title("Digital Synth")

#volume slider at bottom of window
volumeSliderLabel = Label(root, text="Volume Slider")
volumeSliderLabel.pack(side=BOTTOM)
volumeSlider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=lambda change: sound.changeVolume(change))
volumeSlider.set(50)
volumeSlider.pack(side=BOTTOM, expand="yes")

#menu for oscillator 3
menuText3 = StringVar()
menuText3.set("Wave type")
typeMenu3 = OptionMenu(root, menuText3, "sine", "square", "saw", "none", command=lambda wavetype3: sound.menuThreeHit(wavetype3))
typeMenu3.pack(side=BOTTOM, expand="yes")
osc3Label = Label(root, text="Oscillator 3")
osc3Label.pack(side=BOTTOM)

#menu for oscillator 2
menuText2 = StringVar()
menuText2.set("Wave type")
typeMenu2 = OptionMenu(root, menuText2, "sine", "square", "saw", "none", command=lambda wavetype2: sound.menuTwoHit(wavetype2))
typeMenu2.pack(side=BOTTOM, expand="yes")
osc2Label = Label(root, text="Oscillator 2")
osc2Label.pack(side=BOTTOM)

#menu to select wave type for 1
menuText = StringVar()
menuText.set("Wave type")
osc1Label = Label(root, text="Oscillator 1")
osc1Label.pack(side=TOP)
typeMenu = OptionMenu(root, menuText, "sine", "square", "saw", command=lambda wavetype: sound.menuOneHit(wavetype))
typeMenu.pack(side=TOP, expand="yes")

#populates the buttons by looping through each note in the dictionary and making a button that plays the note
for i in sound.noteDict:
    note = i
    i = Button(root, text=i, command=lambda note=note: sound.hitNote(note), repeatdelay=1, repeatinterval=1)
    i.pack(pady=20, side=LEFT, fill="both", expand="yes")

root.mainloop()

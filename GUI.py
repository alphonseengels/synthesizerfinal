from tkinter import *
import tkinter as tk
import sound

root = tk.Tk()
root.title("Select a Note")


volumeSliderLabel = Label(root, text="Volume Slider")
volumeSliderLabel.pack(side=BOTTOM)

volumeSlider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=lambda change: sound.changeVolume(change))
volumeSlider.set(50)
volumeSlider.pack(side=BOTTOM)

menuText = StringVar()
menuText.set("Wave type")

osc1Label = Label(root, text="Oscillator 1")
osc1Label.pack(side=TOP)
typeMenu = OptionMenu(root, menuText, "sine", "square", "saw", "triangle", command=lambda type: sound.menuHit(type))
typeMenu.pack(side=TOP)
'''
osc2Menu = OptionMenu(root, menuText, "sine", "square", "saw", "triangle", command= lambda type: sound.menuTwoHit(type))
osc2Menu.pack(side = BOTTOM)

osc3Label = Label(root, text="Oscillator 3")
osc3Label.pack(side = BOTTOM)
osc3Menu = OptionMenu(root, menuText, "sine", "square", "saw", "triangle", command= lambda type: sound.menuThreeHit(type))
osc3Menu.pack(side = BOTTOM)

osc2Label = Label(root, text="Oscillator 2")
osc2Label.pack(side = BOTTOM)
'''
#populates the buttons by looping through each note in the dictionary and making a button that plays the note
for i in sound.noteDict:
    note = i
    i = Button(root, text=i, command=lambda note=note: sound.hitNote(note), repeatdelay=1, repeatinterval=1)
    i.pack(pady=20, side=LEFT)

root.mainloop()

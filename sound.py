import time
import numpy as np
import pyaudio
import scipy
import images

#dictionary containing the frequency of each note in Hz
noteDict = {"C": 261.63,
            "C#": 277.18,
            "D": 293.66,
            "D#": 311.13,
            "E": 329.63,
            "F": 349.23,
            "F#": 369.99,
            "G": 392.00,
            "G#": 415.30,
            "A": 440.00,
            "A#": 466.16,
            "B": 493.88}

#these will be the parameters for the Wave class
attributesDict = {"volume": 0.5,
                   "sampleRate": 44100,
                   "duration": 0.1,
                   "frequency": 0,
                   "phase": 1,
                   "type": "sine",
                   "samples": None,
                   "output_bytes": None}

interval = 1.0/attributesDict["sampleRate"]
t = np.arange(0,1,interval)

#class of objects that will be the oscillators
class Wave:
   def __init__(self, volume, sampleRate, duration, frequency, phase, type, samples, output_bytes):
       self.volume = volume
       self.sampleRate = sampleRate
       self.duration = duration
       self.frequency = frequency
       self.phase = phase
       self.type = type
       self.samples = samples
       self.output_bytes = output_bytes

#actually calculates and samples the waveform for an oscillator
   def calcWave(self):
       if self.type == "sine":
           x = np.sin
       if self.type == "square":
           x = scipy.signal.square
       if self.type == "saw":
           x = scipy.signal.sawtooth

    #sampling the wave with x being the function that represents the wave's shape
       self.samples = self.phase * x(2 * np.pi * np.arange(self.sampleRate * self.duration) * self.frequency / self.sampleRate).astype(np.float32)
       self.output_bytes = (self.volume * self.samples).tobytes()


#plays the waveform out loud
   def play(oscillators):
       output_bytes = bytes(0)
       i = 0
       #sums up the waveforms out of the list of oscillators...
       while i < len(oscillators):
           output_bytes += oscillators[i].output_bytes
           i += 1
       p = pyaudio.PyAudio()
       stream = p.open(format=pyaudio.paFloat32,
                           channels=2,
                           rate=attributesDict["sampleRate"],
                           output=True)
       start_time = time.time()
       #plays the sum of waveforms
       stream.write(output_bytes)
       stream.stop_stream()
       stream.close()
       p.terminate()

   def plot(self):
       images.wavePlot(self.samples)

defaultOsc = Wave(**attributesDict)
oscillators = [defaultOsc]

#functions that are called when pressing buttons in the GUI

#changes the volume (affects all oscillators)
def changeVolume(change):
    for i in oscillators:
        i.volume = attributesDict["volume"] = float(change) * 0.01

#changes the frequency (affects all oscillators), plays and plots the waves
def hitNote(f):
    for i in oscillators:
        i.frequency = noteDict[f]
        i.calcWave()
        i.plot()
    Wave.play(oscillators)


#functions that initialize oscillators and/or change their shape
def updateOsc1():
    osc1 = Wave(**attributesDict)
    oscillators[0] = osc1

def updateOsc2():
    osc2 = Wave(**attributesDict)
    #adds oscillator 2 to the list of oscillators, depending on the length of the list...
    if len(oscillators) == 2:
        oscillators[1] = osc2
    if len(oscillators) == 1:
        oscillators.append(osc2)
    if osc2.type == "none":
        oscillators.remove(osc2)


def updateOsc3():
    osc3 = Wave(**attributesDict)
    if len(oscillators) == 3:
        oscillators[2] = osc3
    if len(oscillators) == 2:
        oscillators.append(osc3)
    if osc3.type == "none":
        oscillators.remove(osc3)



#functions that trigger when the option menus are clicked
def menuOneHit(type):
    attributesDict["type"] = str(type)
    updateOsc1()

def menuTwoHit(type):
    attributesDict["type"] = str(type)
    updateOsc2()

def menuThreeHit(type):
    attributesDict["type"] = str(type)
    updateOsc3()
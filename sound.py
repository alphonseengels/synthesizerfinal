import time
import numpy as np
import pyaudio
import scipy
import images

oscillators = [None]

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
                   "duration": 0.5,
                   "frequency": 0,
                   "phase": 1,
                   "type": "sine"}


interval = 1.0/attributesDict["sampleRate"]
t = np.arange(0,1,interval)

#class of objects that will be the oscillators
class Wave:
   def __init__(self, volume, sampleRate, duration, frequency, phase, type):
       self.volume = volume
       self.sampleRate = sampleRate
       self.duration = duration
       self.frequency = frequency
       self.phase = phase
       self.type = type

#actually calculates and samples the waveform
   def calcWave(self):
    if self.type == "sine":
        x = np.sin
    if self.type == "square":
        x = scipy.signal.square
    if self.type == "saw":
        x = scipy.signal.sawtooth

#sampling the wave with x being the function that represents the wave's shape
    samples = self.phase * x(2 * np.pi * np.arange(self.sampleRate * self.duration) * self.frequency / self.sampleRate).astype(np.float32)
    output_bytes = (self.volume * samples).tobytes()
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=self.sampleRate,
                    output=True)
    start_time = time.time()
    stream.write(output_bytes)
    stream.stop_stream()
    stream.close()

    images.wavePlot(samples)

#functions that are called upon pressing buttons in the GUI

def changeVolume(change):
    attributesDict["volume"] = float(change) * 0.01
    updateOsc()


def hitNote(f):
    attributesDict["frequency"] = noteDict[f]
    updateOsc()
    for i in oscillators:
        Wave.calcWave(i)

def updateOsc():
    osc1 = Wave(**attributesDict)
    oscillators[0] = osc1

def menuHit(type):
    attributesDict["type"] = str(type)
    updateOsc()

'''
def menuTwoHit(type):
    attributesDict["type"] = str(type)
    osc2 = Wave(**attributesDict)
    oscillators.append(osc2)

def menuThreeHit(type):
    attributesDict["type"] = str(type)
    osc3 = Wave(**attributesDict)
    oscillators.append(osc3)
   '''


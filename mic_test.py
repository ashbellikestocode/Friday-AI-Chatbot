# My working audio recorder

import sounddevice as sd
a=sd.rec(220500, samplerate=44100, channels=1,device=1)
sd.wait()
print("Recording finished. Playing back...")
sd.play(a, samplerate=44100)
sd.wait()
print(sd.query_devices())
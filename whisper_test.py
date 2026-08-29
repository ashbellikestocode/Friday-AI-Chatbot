from faster_whisper import WhisperModel
import sounddevice as sd
from command_processor import process_command
from speech import speak 

#Lets choose a whisper model
model = WhisperModel("small", device="cpu", compute_type="int8")

while True:
    print("Recording Audio....")
    audio=sd.rec(80000,samplerate=16000,channels=1,dtype="float32",device=1)
    sd.wait()
    audio=audio.squeeze()
    segments,info=model.transcribe(audio,language="en")
    recognized_text=""
    for segment in segments:
            recognized_text+=segment.text.lower()

    if "hey friday" in recognized_text:
        speak("Hello sir")
        speak("Recording instructions...")
        command=sd.rec(80000,samplerate=16000,channels=1,dtype="float32",device=1)
        sd.wait()
        command=command.squeeze()
        segments,info=model.transcribe(command,language="en")
        recognized_command="" 
        for segment in segments:
            recognized_command+=segment.text.lower()
        print(recognized_command)   
        process_command(recognized_command)


             

            
                 


                 
                



            
                            

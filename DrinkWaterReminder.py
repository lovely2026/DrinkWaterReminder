import pyttsx3
import time

def reminder(interval_seconds=2,voice_id=1, rate=150):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)  # Set the voice
    engine.setProperty('rate', rate) # Set the rate of voice
    try:
        while True:
            engine.say("Hey! It's time to drink water!")
            engine.runAndWait() 
            time.sleep(interval_seconds)  
            
    except KeyboardInterrupt:
        print("Reminder stopped.")

if __name__ == "__main__":
    reminder()

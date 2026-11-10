import pyttsx3
import pythoncom

def text_to_speech(text):
    try:
        # Authorize the background thread to use Windows Speech
        pythoncom.CoInitialize()
        
        # Initialize the engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        
        print(f"AI: {text}")
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"Speech error: {e}")
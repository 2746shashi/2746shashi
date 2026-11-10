import pyttsx3
import pythoncom  # This library manages Windows background threads

def text_to_speech(text):
    try:
        # 1. Authorize this thread to use Windows Speech COM objects
        pythoncom.CoInitialize()
        
        # 2. Initialize the engine on the current active thread
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        
        print(f"AI: {text}")
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        print(f"Speech error: {e}")
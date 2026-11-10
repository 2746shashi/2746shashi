import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            # 5-second timeout prevents infinite freezing
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            
        voice_data = r.recognize_google(audio)
        print(f"User said: {voice_data}")
        return voice_data
        
    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        return ""
    except Exception as e:
        print(f"Microphone error: {e}")
        return ""
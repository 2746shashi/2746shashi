import speech_to_text
import text_to_speech
import datetime
import webbrowser
import weather
import os
import pyjokes
import pyautogui
import ollama
import subprocess

ollama_client = ollama.Client()

def Action(data_input=""):
    if data_input != "":
        user_data = data_input.lower()
    else:
        user_data = speech_to_text.speech_to_text().lower()

    if not user_data:
        return ""

    # 1. System Operations
    if "open notepad" in user_data:
        os.system("notepad")
        return text_to_speech.text_to_speech("Opening Notepad.")
    
    elif "close notepad" in user_data:
        subprocess.run(["taskkill", "/f", "/im", "notepad.exe"], capture_output=True)
        return text_to_speech.text_to_speech("Closed Notepad.")

    elif "open calculator" in user_data:
        os.system("calc")
        return text_to_speech.text_to_speech("Opening Calculator.")

    elif "close calculator" in user_data:
        subprocess.run(["taskkill", "/f", "/im", "calc.exe"], capture_output=True)
        return text_to_speech.text_to_speech("Closed Calculator.")

    # 2. Utilities
    elif "screenshot" in user_data:
        try:
            pyautogui.screenshot().save("screenshot.png")
            return text_to_speech.text_to_speech("Screenshot saved.")
        except Exception:
            return text_to_speech.text_to_speech("Failed to take screenshot.")

    elif "joke" in user_data:
        return text_to_speech.text_to_speech(pyjokes.get_joke())

    elif "time" in user_data:
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        return text_to_speech.text_to_speech(f"The time is {time_str}.")

    elif "weather" in user_data:
        words = user_data.split()
        city = words[words.index("in") + 1] if "in" in words else "Patna"
        return text_to_speech.text_to_speech(weather.weather(city))

    # 3. Web Navigation
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        return text_to_speech.text_to_speech("Opening YouTube.")

    elif "google" in user_data or "search" in user_data:
        webbrowser.open("https://google.com/")
        return text_to_speech.text_to_speech("Opening Google.")

    elif "shutdown" in user_data or "exit" in user_data or "close" in user_data:
        text_to_speech.text_to_speech("Goodbye!")
        return "EXIT"

    # 4. Local LLM Fallback
    else:
        try:
            system_prompt = "You are a concise voice assistant."
            response = ollama_client.chat(model='llama3.2', messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_data}
            ])
            reply = response['message']['content']
            text_to_speech.text_to_speech(reply)
            return reply
        except Exception:
            error_msg = "Local AI is offline."
            text_to_speech.text_to_speech(error_msg)
            return error_msg
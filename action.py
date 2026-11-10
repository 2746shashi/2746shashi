import speech_to_text
import text_to_speech
import datetime
import webbrowser
import weather
import os
import pyjokes
import pyautogui
import ollama

def Action(data_input=""):
    # Normalize input from GUI or Microphone
    if data_input != "":
        user_data = data_input.lower()
    else:
        user_data = speech_to_text.speech_to_text()
        if user_data:
            user_data = user_data.lower()
        else:
            return "I didn't catch that."

    # 1. Quick Utilities & Commands
    if "what is your name" in user_data or "who are you" in user_data:
        response = "I am your offline AI assistant."
        text_to_speech.text_to_speech(response)
        return response

    elif "hello" in user_data or "hey" in user_data or "hi" in user_data:
        response = "Hello! I am ready and listening. How can I help you today?"
        text_to_speech.text_to_speech(response)
        return response

    elif "joke" in user_data:
        joke = pyjokes.get_joke()
        text_to_speech.text_to_speech(joke)
        return joke

    elif "open notepad" in user_data:
        os.system("notepad")
        response = "Opening Notepad."
        text_to_speech.text_to_speech(response)
        return response

    elif "open calculator" in user_data:
        os.system("calc")
        response = "Opening Calculator."
        text_to_speech.text_to_speech(response)
        return response

    elif "screenshot" in user_data:
        try:
            img = pyautogui.screenshot()
            img.save("screenshot.png")
            response = "Screenshot taken and saved."
        except Exception as e:
            response = "Failed to take screenshot."
        text_to_speech.text_to_speech(response)
        return response

    # 2. Dynamic Information Retrievers
    elif "time" in user_data:
        current_time = datetime.datetime.now()
        time_str = current_time.strftime("%I:%M %p")
        response = f"The current time is {time_str}."
        text_to_speech.text_to_speech(response)
        return response

    elif "weather" in user_data:
        words = user_data.split()
        city = "Patna"
        if "in" in words:
            try:
                city = words[words.index("in") + 1]
            except IndexError:
                pass
        response = weather.weather(city)
        text_to_speech.text_to_speech(response)
        return response

    # 3. Web Navigation
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        response = "Opening YouTube."
        text_to_speech.text_to_speech(response)
        return response

    elif "google" in user_data or "search" in user_data:
        webbrowser.open("https://google.com/")
        response = "Opening Google."
        text_to_speech.text_to_speech(response)
        return response

    elif "shutdown" in user_data or "exit" in user_data or "close" in user_data:
        response = "Goodbye!"
        text_to_speech.text_to_speech(response)
        return "EXIT"

    # 4. Local AI Brain (Ollama Fallback)
    else:
        try:
            system_prompt = "You are a concise voice assistant. Answer in 1 to 3 short sentences."
            ai_response = ollama.chat(model='llama3.2', messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_data}
            ])
            result = ai_response['message']['content']
            text_to_speech.text_to_speech(result)
            return result
        except Exception:
            error_msg = "My local brain is offline. Please ensure Ollama is running."
            text_to_speech.text_to_speech(error_msg)
            return error_msg
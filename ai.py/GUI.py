from tkinter import *
from PIL import Image, ImageTk
import action
import threading
import os
import weather

# Create window
root = Tk()
root.title("AI Assistant")
root.geometry("550x750")
root.resizable(False, False)
root.config(bg="#6F8FAF")

def process_response(user_val):
    if user_val == "EXIT":
        root.quit()
    else:
        text.insert(END, f"AI: {user_val}\n\n")
        text.see(END)

def ask_thread():
    text.insert(END, "Listening (Speak now)...\n")
    text.see(END)
    response = action.Action("")
    process_response(response)

def send_thread(user_val):
    response = action.Action(user_val)
    process_response(response)

def ask():
    threading.Thread(target=ask_thread, daemon=True).start()

def send():
    user_val = entry.get().strip()
    if user_val:
        text.insert(END, f"You: {user_val}\n")
        entry.delete(0, END)
        threading.Thread(target=send_thread, args=(user_val,), daemon=True).start()

def del_text():
    text.delete("1.0", END)

# Image Frame
frame = Frame(root, bg="#6F8FAF")
frame.pack(pady=15)

# Load the assistant image
if os.path.exists("assistant.png"):
    try:
        img = Image.open("assistant.png")
        img = img.resize((150, 150), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        img_label = Label(frame, image=img_tk, bg="#6F8FAF")
        img_label.image = img_tk  # Keep reference so it doesn't disappear
        img_label.pack()
    except Exception as e:
        print(f"Error loading image: {e}")

text_label = Label(
    frame,
    text="AI Assistant",
    font=("Comic Sans MS", 16, "bold"),
    bg="#6F8FAF",
    fg="white"
)
text_label.pack(pady=5)

# Text Box
text = Text(
    root,
    font=("Courier", 10, "bold"),
    bg="#356696",
    fg="white",
    wrap=WORD,
    padx=10,
    pady=10
)
text.pack(padx=20, pady=10, fill=BOTH, expand=True)

# Entry Box
entry = Entry(root, justify=CENTER, font=("Arial", 12))
entry.pack(padx=20, pady=10, fill=X, ipady=5)

# Buttons
btn_frame = Frame(root, bg="#6F8FAF")
btn_frame.pack(pady=10)

Button(btn_frame, text="ASK (VOICE)", bg="#356696", fg="white", pady=10, padx=20, borderwidth=3, relief=SOLID, command=ask).grid(row=0, column=0, padx=10)
Button(btn_frame, text="SEND (TEXT)", bg="#356696", fg="white", pady=10, padx=20, borderwidth=3, relief=SOLID, command=send).grid(row=0, column=1, padx=10)
Button(btn_frame, text="CLEAR CHAT", bg="#356696", fg="white", pady=10, padx=20, borderwidth=3, relief=SOLID, command=del_text).grid(row=0, column=2, padx=10)

# Start the application
root.mainloop()
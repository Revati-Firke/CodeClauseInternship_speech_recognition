import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox
from tkinter.font import Font

# Initialize the recognizer
recognizer = sr.Recognizer()

def recognize_speech():
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... Please speak to search..")
        
        # Listen for the first phrase and extract it into audio data
        audio_data = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio_data)
            print("Your search :", text)
            messagebox.showinfo("Recognized Speech", f"You said: {text}")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Could not request results from Google Web Speech API; {e}")

# Set up the GUI
def GUI_display():
    window = tk.Tk()
    window.title("Speech Recognition")
    window.geometry("550x330")
    font=Font(family="Times New Roman",size=18)
    label = tk.Label(window,foreground="black",bg="pink", text="Press the button below and speak into the microphone",font=font)
    label.pack(pady=10)
    
    recognize_btn = tk.Button(window,fg="white",bg="blue", text="Click to Speak!!",font=font, command=recognize_speech)
    recognize_btn.pack(pady=30)
    image=tk.PhotoImage(file="microphone.gif")
    label=tk.Label(window,image=image)
    label.pack()
    window.mainloop()

# Run the GUI setup
GUI_display()

import tkinter as tk
import subprocess
from tkinter import * 

program = Tk() 
p1 = PhotoImage(file = 'logo.png')   
# Icon set for program window
program.iconphoto(False, p1)   

def start_function():
    user_vs_user_button.pack(pady=10)  # Show the "User Vs User" button
    user_vs_ai_button.pack(pady=10)  # Show the "User Vs AI" button
    analyzer_button.pack(pady=10)  # Show the "Analyzer" button

def user_vs_user_function():
    subprocess.Popen(['python', 'chessh/ChessMain.py'])

def user_vs_ai_function():
    subprocess.Popen(['python', 'chessai/ChessMain.py'])

def analyzer_function():
    subprocess.Popen(['python', 'checkgame.py'])

window = tk.Tk()
window.title("ChessWizard")
window.geometry("300x300")


user_vs_user_button = tk.Button(window, text="User Vs User", command=user_vs_user_function)
user_vs_user_button.pack(pady=10)

user_vs_ai_button = tk.Button(window, text="User Vs AI", command=user_vs_ai_function)
user_vs_ai_button.pack(pady=10)

analyzer_button = tk.Button(window, text="Analyzer", command=analyzer_function)
analyzer_button.pack(pady=10)

window.mainloop()
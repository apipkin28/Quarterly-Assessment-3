import tkinter as tk
from tkinter import ttk
import sqlite3

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")

        self.conn = sqlite3.connect('QuizBowl.db')
        self.cr = self.conn.cursor()

        self.createMain()
    
    # first window
    def createMain(self):
        self.mainFrame = ttk.Frame(self.root, padding="20")
        self.mainFrame.grid(row=0, column=0)

        self.label = ttk.Label(self.mainFrame, text="Select a category:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.categoryVar = tk.StringVar()
        self.categoryDropdown = ttk.Combobox(self.mainFrame, textvariable=self.categoryVar, width=30, state="readonly")
        self.categoryDropdown['values'] = ["Business_Applications_Development", 
                                            "Behavioral_Economics", 
                                            "Economics_Workshop", 
                                            "Risk_Management_And_Insurance", 
                                            "Calculus_II"]
        self.categoryDropdown.grid(row=0, column=1, padx=5, pady=5)

        self.submitBtn = ttk.Button(self.mainFrame, text="Start Quiz", command=self.startQuiz)
        self.submitBtn.grid(row=0, column=2, padx=5, pady=5)
    

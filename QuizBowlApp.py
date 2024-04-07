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
    
    # second window
    def startQuiz(self):
        selectedCategory = self.categoryVar.get()
        questions = self.getQs(selectedCategory)

        self.mainFrame.destroy()

        self.quizFrame = ttk.Frame(self.root, padding="20")
        self.quizFrame.grid(row=0, column=0)

        self.questionLabels = []
        self.selectedAnswers = {}
        for i, (question, answer) in enumerate(questions, start=1):
            ttk.Label(self.quizFrame, text=f"{i}. {question}").grid(row=i, column=0, sticky="w", padx=5, pady=5)
            self.selectedAnswers[i] = tk.StringVar()
            ttk.Radiobutton(self.quizFrame, text="A", variable=self.selectedAnswers[i], value="A").grid(row=i, column=1, sticky="w", padx=5, pady=5)
            ttk.Radiobutton(self.quizFrame, text="B", variable=self.selectedAnswers[i], value="B").grid(row=i, column=2, sticky="w", padx=5, pady=5)
            ttk.Radiobutton(self.quizFrame, text="C", variable=self.selectedAnswers[i], value="C").grid(row=i, column=3, sticky="w", padx=5, pady=5)

        ttk.Button(self.quizFrame, text="Submit Answers", command=lambda: self.submitAnswers(selectedCategory, questions)).grid(row=len(questions) + 1, column=0, columnspan=4, padx=5, pady=10)
    
    # retrieving questions from db table
    def getQs(self, category):
        self.cr.execute(f"SELECT question, answer FROM {category}")
        return self.cr.fetchall()
    
    # scoring
    def submitAnswers(self, category, questions):
        correctAnswers = 0
        totalQs = len(questions)

        for i, (question, answer) in enumerate(questions, start=1):
            selected_answer = self.selectedAnswers[i].get()
            if selected_answer == answer:
                correctAnswers += 1
                feedback = "Correct!"
            else:
                feedback = f"Incorrect. Correct answer: {answer}"

            ttk.Label(self.quizFrame, text=feedback).grid(row=i, column=4, sticky="w", padx=5, pady=5)

        ttk.Label(self.quizFrame, text=f"You scored {correctAnswers}/{totalQs}").grid(row=totalQs + 2, column=0, columnspan=5, padx=5, pady=5)


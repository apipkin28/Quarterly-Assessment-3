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
    

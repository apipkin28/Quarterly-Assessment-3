import sqlite3

# defining function to create tables
def tableCreation():
    # connecting to db
    conn = sqlite3.connect('QuizBowl.db')
    cr = conn.cursor()

    # creating tables for db
    cr.execute(f'''CREATE TABLE IF NOT EXISTS Business_Applications_Development (
                                id INTEGER PRIMARY KEY,
                                question TEXT,
                                answer TEXT)
                                ''')
    cr.execute(f'''CREATE TABLE IF NOT EXISTS Behavioral_Economics (
                                id INTEGER PRIMARY KEY,
                                question TEXT,
                                answer TEXT)
                                ''')
    cr.execute(f'''CREATE TABLE IF NOT EXISTS Economics_Workshop (
                                id INTEGER PRIMARY KEY,
                                question TEXT,
                                answer TEXT)
                                ''')
    cr.execute(f'''CREATE TABLE IF NOT EXISTS Risk_Management_And_Insurance (
                                id INTEGER PRIMARY KEY,
                                question TEXT,
                                answer TEXT)
                                ''')
    cr.execute(f'''CREATE TABLE IF NOT EXISTS Calculus_II (
                                id INTEGER PRIMARY KEY,
                                question TEXT,
                                answer TEXT)
                                ''')
    # commit changes and close connection
    conn.commit()
    conn.close()

# call the function to create tables
tableCreation()
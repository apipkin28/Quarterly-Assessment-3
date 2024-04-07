# Quarterly-Assessment-3
This project is a continuation of the QuizBowl application with the combination of a database and GUI. The database file is used to store the quiz categories and corresponding questions, while the GUI provides a way for the user to take their quiz of choice.

## Files
### Database files
1. `createtablesdb.py`: This file was used to create tables within the QuizBowl database. Each table stands for each of the subjects the user can choose to be quizzed on.
2. `populatedb.py`: This file was used to populate the tables with ten multiple choice questions each.
3. `readdb.py`: This file was used to confirm that the database had connected and received the data properly.
4. `QuizBowl.db`: This is the actual database file.

### Quiz Bowl GUI
`QuizBowlApp.py`: This file holds the code for running the Quiz Bowl GUI windows. Once the database files have been run and the database has been properly populated, then the QuizBowl App code can run after. Once ran, the first GUI window will appear, providing a user with the option of 5 quiz categories. Once chosen, the user can click "Start Quiz" and will be brought over to the second window. The second window displays the actual quiz, and the user can choose between answers A, B, or C for each of the ten questions before submitting. Once submitted, the user will receive a score at the bottom of the window, as well as feedback on whether their answers were correct or not.
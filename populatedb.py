import sqlite3

class DBQuestions:
# inserting questions and answers into table
    def insertQA():
    # defining the questions and answers -- used GAI for questions
        quizData = {
            "Business_Applications_Development": [
                ("What does the 'print()' function do in Python? A) Displays output B) Reads input C) Converts data types","A"),
                ("Which of the following is used to define a function in Python? A) for B) def C) if","B"),
                ("What is the correct syntax for a list comprehension in Python? A) [x for x in range(10)] B) (x for x in range(10)) C) [x*2 for x in range(10)]","C"),
                ("Which of the following is NOT a valid data type in Python? A) int B) float C) char","C"),
                ("What does the 'len()' function return in Python? A) Length of an object B) Largest element C) Smallest element","A"),
                ("Which of the following is used for comments in Python? A) // B) # C) <!-- -->","B"),
                ("What is the output of '2 + 2' in Python? A) 4 B) '4' C) '22'","A"),
                ("What is the output of '3 * 'hello' in Python? A) 'hellohellohello' B) Error C) 'hellohellohellohellohello'","C"),
                ("What does the 'import' keyword do in Python? A) Imports a module B) Declares a variable C) Defines a function","A"),
                ("Which of the following is used to exit a loop in Python? A) continue B) break C) exit","C")
            ],
            "Behavioral_Economics": [
                ("What is the Endowment Effect? A) Describes market supply and demand B) Tendency to value owned items higher C) Theory of consumer behavior","B"),
                ("What is Prospect Theory? A) Predicts future economic trends B) Theory of inflation C) Describes decision making under risk","C"),
                ("What is Loss Aversion? A) Tendency to avoid losses B) Desire to maximize profit C) Willingness to take risks","A"),
                ("What is Anchoring? A) Economic theory B) Desire to maximize utility C) Cognitive bias towards initial information","C"),
                ("What is Confirmation Bias? A) Economic model B) Tendency to favor preexisting beliefs C) Theory of demand","B"),
                ("What is the Halo Effect? A) Cognitive bias in judgment B) Economic indicator C) Behavioral economics principle","A"),
                ("What is the Availability Heuristic? A) Investment strategy B) Mental shortcut for decision making C) Economic theory of production","B"),
                ("What is Framing Effect? A) Bias in decision making based on presentation B) Economic pricing strategy C) Theory of inflation","A"),
                ("What is the Overconfidence Effect? A) Economic market phenomenon B) Investment strategy C) Tendency to overestimate abilities","C"),
                ("What is the Status Quo Bias? A) Economic theory of trade B) Tendency to prefer current state C) Consumer spending behavior","B")  
            ],
            "Economics_Workshop": [
                ("What is Microeconomics? A) Study of individual economic units B) Study of aggregate economy C) Analysis of global markets","A"),
                ("What is Macroeconomics? A) Analysis of consumer behavior B) Study of overall economy C) Study of individual firms","B"),
                ("What is Opportunity Cost? A) Cost of next best alternative B) Total cost of production C) Cost of raw materials","A"),
                ("What is Supply and Demand? A) Economic theory of production B) Market equilibrium C) Relationship between buyers and sellers","C"),
                ("What is Elasticity? A) Economic growth measure B) Responsiveness of quantity demanded to price changes C) Rate of inflation","B"),
                ("What is Monopoly? A) Market structure with single seller B) Market structure with multiple sellers C) Market structure with no sellers","A"),
                ("What is Oligopoly? A) Market structure with single seller B) Market structure with few sellers C) Market structure with many sellers","B"),
                ("What is Perfect Competition? A) Market structure with no sellers B) Market structure with single seller C) Market structure with many sellers","C"),
                ("What is Gross Domestic Product (GDP)? A) Total value of goods and services produced B) Total consumer spending C) Total government spending","A"),
                ("What is Inflation? A) Total value of goods and services produced B) Rate of increase in price level C) Rate of decrease in price level","B") 
            ],
            "Risk_Management_And_Insurance": [
                ("What is Risk Management? A) Identifying, assessing, and controlling threats B) Assessing market demand C) Investing in high-risk assets","A"),
                ("What is Insurance? A) Method of saving money B) Contract transferring financial risk C) Government welfare program","B"),
                ("What is Risk Assessment? A) Process of selecting investments B) Analysis of market trends C) Identifying hazards and their potential impact","C"),
                ("What is Risk Mitigation? A) Reducing adverse effects of threats B) Accepting all risks C) Ignoring potential threats","A"),
                ("What is Underwriting? A) Evaluating investment opportunities B) Assessing risk for insurance C) Calculating future profits","B"),
                ("What is Actuarial Science? A) Applying mathematical methods to assess risk B) Studying consumer behavior C) Analyzing market trends","A"),
                ("What is Reinsurance? A) Insuring individual policies B) Transferring risk to another insurer C) Refusing to insure high-risk clients","B"),
                ("What is Catastrophe Bond? A) Insurance policy for everyday events B) Life insurance policy C) Bond issued to cover catastrophic events","C"),
                ("What is Risk Financing? A) Determining how to pay for losses B) Investing in high-risk assets C) Borrowing money to cover expenses","A"),
                ("What is Enterprise Risk Management (ERM)? A) Managing risks for individuals B) Investing in new businesses C) Identifying risks across an organization","C")
            ],
            "Calculus_II": [
                ("What is Integration? A) Finding area under curve B) Finding slope of a curve C) Finding limit of a sequence","A"),
                ("What is the Fundamental Theorem of Calculus? A) Describes properties of functions B) Relates differentiation and integration C) Describes properties of limits","B"),
                ("What is Differentiation? A) Finding area under curve B) Finding limit of a sequenc C) Finding rate of change","C"),
                ("What is the Chain Rule? A) Rule for solving exponential equations B) Rule for differentiating composite functions C) Rule for finding limits","B"),
                ("What is Partial Derivative? A) Derivative with respect to one variable B) Derivative with respect to all variables C) Derivative of a constant","A"),
                ("What is Integration by Parts? A) Finding slope of a curve B) Finding area under curve C) Method for integration of products","C"),
                ("What is Taylor Series? A) Series for finding limits B) Series expansion of a function C) Series for solving differential equations","B"),
                ("What is Maclaurin Series? A) Series for finding limits B) Series for solving differential equations C) Taylor series expansion around 0","C"),
                ("What is Power Series? A) Infinite series involving powers of a variable B) Infinite series for finding limits C) Series for solving differential equations","A"),
                ("What is Taylor's Theorem? A) Describes properties of functions B) Describes properties of limits C) Theorem for approximating functions","C")
            ]
        }

        # connect to db
        conn = sqlite3.connect('QuizBowl.db')
        cr = conn.cursor()

        # iterate through quiz data
        for table, pairsQA in quizData.items():
            for question, answer in pairsQA:
                cr.execute(f"INSERT INTO {table} (question, answer) VALUES (?, ?)", (question, answer))

        # commit changes and close
        conn.commit()
        conn.close()

    # call function to insert
    insertQA()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Welcome to Keleni's Bible Quizz!")
print("============================================")
#Welcome
name =input ("What is your name: ")
print("Welcome {}, Thank you for taking my Bible Quiz. " .format(name))

#Introductions
#these are the instructions for the quiz and how it will work. This is used to notify the user about the quiz and inform with things they need to know.
print("============================================")
print("Intructions")
print("1. You will be answering a total of 10 bible quiz questions. ")
print("2. In each question you are required to pick on of the multichoice suggestions\n as the answer for the question. ")
print("3. If your answer isnt one of the options or you spelt the answer in correctly, \nthe question is repeated. Make sure your answer is one of the options given\n and correctly spelt. ")
print("4. You are allowed to just type in the letter that has the answer that you \nbelieve is correct.")
print(":)Now let us test your general Bible knowledege!!(:")
print("====================================================================================")


#question One
#In the while loop, the user is asked a multichoice question. If the user picks one of the correct forms of the answer, then the user will be told their answer is correct. But if they choose the wrong answer or any of its form, they will be told their answer is wrong. And if they answer correctly or wrong, the quiz will continue. If the user does not choose any of the given options (or any of his forms) the question will be repeated and the user will be asked to choose the given options. 
print("Question 1")
while True:
  question_one = input("Who betrayed Jesus?\n (a) john the baptist\n (b) peter\n (c) judas\n (d) paul\n >>  ")

  correct_q1 = ["judas", "c", "(c)","Judas"]
  incorrect_q1 = [" john the baptist","john","John", "(a)", "a","Peter", "peter", "(b)", "b", "paul", "Paul", "(d)", "d"]

  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")
print("====================================================================================")





#Question Two
print("Question 2")
while True:
  question_one = input("How many years did the Israelites spend in the Wilderness in the OT? \n (a) 56 years \n (b) 100 years \n (c) 60 years \n (d) 40 years\n >>  ")
  
  correct_q1 = ["40 years", "d", "(d)","40"]
  incorrect_q1 = ["56 years", "(a)", "a","56", "100 years","100", "(b)", "b","60", "60 years", "(c)", "c"]

  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")
print("====================================================================================")




#Question Three
print("Question 3")
while True:
  question_one = input("How old was the oldest person (Methuselah) in the Bible? \n (a) 969 years \n (b) 150 years \n (c) 500 years \n (d) 249 years\n >>  ")
  
  correct_q1 = ["969 years", "a", "(a)","969"]
  incorrect_q1 = ["150 years","150", "(a)", "a", "500 years","500", "(c)", "c", "249 years", "249", "(d)", "d"]

  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")
print("====================================================================================")




#Question Four
print("Question 4")
while True:
  question_one = input("What was the last plague of the 10 plagues in Egypt? \n (a) water into blood \n (b) death of first borns \n (c) lice\n (d) boils\n >>  ")
  
  correct_q1 = ["death of first borns", "b", "(b)",]
  incorrect_q1 = ["water into blood", "(a)", "a", "lice", "(c)", "c", "boils", "(d)", "d"]

  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")
print("====================================================================================")



#Question Five
print("Question 5")
while True:
  question_one = input("How many brothers did Joseph (Jacob’s son) have?  \n (a) 5 \n (b) 15 \n (c) 11\n (d) 12 \n>>  ")
  
  correct_q1 = ["11", "c", "(c)","eleven"]
  incorrect_q1 = ["5","five", "(a)", "a", "15","fifteen", "(b)", "b", "12", "(d)", "d","twelve"]

  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")
print("====================================================================================")



#Question Six
print("Question 6")
while True:
  question_one = input("Who was the first eyewitness to Jesus after his resurrection?  \n (a) Mary Magdelene \n (b) Simon Peter \n (c) Paul \n (d) Thomas \n>>  ")
  
  correct_q1 = ["Mary Magdelene", "a", "(a)", "mary magdelene"]
  incorrect_q1 = ["Simon Peter","simon peter", "(b)", "b","paul", "Paul", "(c)", "c", "Thomas", "(d)", "d","thomas"]

  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")
print("====================================================================================")


#Question Seven
print("Question 7")
while True:
  question_one = input("Who was a Christian persecutor but became a Christian on the roads to Damascus? \n (a) James \n (b) John \n (c) Paul \n (d) Bartholomew \n>>  ")
  
  correct_q1 = ["Paul", "c", "(c)", "paul"]
  incorrect_q1 = ["Bartholomew", "(b)", "b", "bartholomew","James", "james" "(a)", "a", "John", "james", "(d)", "d"]

  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")
print("====================================================================================")



#Question Eight
print("Question 8")
while True:
  question_one = input("How many chapters in the longest book of the Bible?    \n (a) 150 \n (b) 89 \n (c) 105 \n (d) 76 \n>>  ")
  
  correct_q1 = ["150", "a", "(a)","150 chapters",]
  incorrect_q1 = ["89", "(d)", "d", "105", "(c)", "c", "76", "(b)", "b"]
  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")
print("====================================================================================")



#Question Nine
print("Question 9")
while True:
  question_one = input('"The Father, Son, and Holy Spirit". What is this called?    \n (a) Trinity \n (b) Cheribum \n (c) Ark of the Covenant \n (d) Alter  \n>>  ')
  
  correct_q1 = ["Trinity", "a", "(a)", "trinity"]
  incorrect_q1 = ["Alter", "(d)", "alter","d", "Ark of the Covenent","ark of the covenant", "(c)", "c", "Cheribum", "cheribum", "(b)", "b"]

  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")


#question Ten
print("Question 10")
while True:
  question_one = input("How many parts was the Tabernacle (in the OT) divided into? \n (a) 6 \n (b) 4 \n (c) 3 \n (d) 2 \n >> ")
  
  correct_q1 = ["3", "c", "(c)", ]
  incorrect_q1 = ["2", "(d)", "4","d", "2", "(a)", "a", "6", "(b)", "b"]

  if question_one.lower() in correct_q1:
    print (">>>>>>>>>>THAT IS CORRECT<<<<<<<<<<<<")
    break
  elif question_one.lower() in incorrect_q1:
    print("***********THAT IS INCORRECT*************")
    break
  else: 
    print("----------------------------------------")
    print("you did not choose any of the options")
    print("----------------------------------------")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("THE END")
print("Thank you, for participating.")
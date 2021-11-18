print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Welcome to Keleni's Bible Quizz!")
print("============================================")
#Welcome
name =input ("What is your name: ")
print("Welcome {}, Thank you for taking my Bible Quiz. " .format(name))

#Introductions
print("============================================")
print("Intructions")
print("1. You will be answering a total of 10 bible quiz questions. ")
print("2. In each question you are required to pick on of the multichoice suggestions\n as the answer for the question. ")
print("3. If your answer isnt one of the options or you spelt the answer in correctly, \nthe question is repeated. Make sure your answer is one of the options given\n and correctly spelt. ")
print("4. You are allowed to just type in the letter that has the answer that you \nbelieve is correct.")
print(":)Now let us test your general Bible knowledege!!(:")




#question One
print("====================================================================================")
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
while True:
  question_one = input("How old was the oldest person (Methuselah) in the Bible? \n (a) 150 years \n (b) 969 years \n (c) 500 years \n (d) 249 years\n >>  ")
  
  correct_q1 = ["969 years", "b", "(b)","969"]
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
while True:
  question_one = input("How many brothers did Joseph (Jacob’s son) have?  \n (a) 5 \n (b) 11 \n (c) 15\n (d) 12 \n>>  ")
  
  correct_q1 = ["11", "b", "(b)","eleven"]
  incorrect_q1 = ["5","five", "(a)", "a", "15","fifteen", "(c)", "c", "12", "(d)", "d","twelve"]

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
print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("THE END")
print("Thank you, for participating.")
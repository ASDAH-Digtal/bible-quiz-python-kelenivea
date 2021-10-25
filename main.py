print("============================================")
print("Welcome to Keleni's Bible Quizz!")
print("============================================")

while True:
  question_one = input("Who betrayed Jesus?\n (a)john the baptist\n (b) peter\n (c) judas\n (d) paul\n >>")

  correct_q1 = ["judas", "c", "(c)",]
  incorrect_q1 = ["john the baptist", "(a)", "a", "peter", "(b)", "b", "paul", "(c)", "c"]

  if question_one.lower() in correct_q1:
  print("that is correct")
  break
  elif question_one.lower() in incorrect_q1:
  print("that is incorrect")
  break
  else: 
  print("you did not choose any of the options")

  
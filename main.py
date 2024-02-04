import random as ran
com = ran.randint(1,3)
user=int(input("Enter What You Want Rock,Paper,Scissors For This Enter 1,2,3: "))

if (com==1 and user==1):
  print("Computer And You Choose The Same Option That Is Rock")
  print("Game Draw")
elif (com==1 and user==2):
  print("Computer Chose Rock And You Chose Paper")
  print("You Win This Game")
elif (com==1 and user==3):
  print("Computer Chose Rock And You Chose Scissors")
  print("You Lose This Game")
  
elif (com==2 and user==1):
  print("Computer Chose Paper And You Chose Rock")
  print("You Lose This Game")
elif (com==2 and user==2):
  print("Computer And You Choose The Same Option That Is Paper")
  print("Game Draw")
elif (com==2 and user==3):
  print("Computer Chose Paper And You Chose Scissors")
  print("You Lose This Game")
  
elif (com==3 and user==1):
  print("Computer Chose Scissors And You Chose Rock")
  print("You Win This Game")
elif (com==3 and user==2):
  print("Computer Chose Scissors And You Chose Paper")
  print("You Lose This Game")
elif (com==3 and user==3):
  print("Computer And You Choose The Same Option That Is Scissors")
  print("Game Draw")
else:
  print("Quit The Game")

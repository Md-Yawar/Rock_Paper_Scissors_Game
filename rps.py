rock = '''
     ___
    ¦   ¦
 /------------------
/            \     ¦
¦       ------------
¦       ------------
¦            \     ¦
¦       ------------
¦       ------------
¦            \     ¦
¦       ------------
\       ------------
 \           \     /
  \---------------/   '''


paper = '''

        ____   ____   ____   ____
       |    | |    | |    | |    |
       |    | |    | |    | |    |
       |    | |    | |    | |    |
       |    | |    | |    | |    |
       |    | |    | |    | |    |
 ____  |    | |    | |    | |    |
|    | |    | |    | |    | |    |
|    | |    | |    | |    | |    |
|    | |    | |    | |    | |    |
|    | |    | |    | |    | |    |
|    | |    | |    | |    | |    |
\                                /
 \                              /
  \                            /
   \                          /
    \                        /
     \                      /     '''



scissors='''
                              _____
                             /     \
                            /      /
                           /      /
                          /      /
                         /      /
                        /      /
                       /      /
                      /      /
     _______________ /      /
   /               /       /
  /                       / -----------------------\
                                                    |
                                                    |
                           ------------------------/
                          |
                          |
                          |
  \                       |
   \_____________________/



'''
life=5
complife=5
print("Your lives:",life)
print("Computer lives:",complife)
while 'true' :
   rps = input("Choose Rock, Paper or Scissors")
   import random
   computer = ("rock", "paper", "scissors")
   computer = random.choice(computer)
#rock if statments
   if rps == "rock" and computer == "paper":
      print("you chose Rock ", rock)
      print("The computer choose paper")
      print(paper)
      print('')
      print('')
      print("YOU LOSE!!")
      print("")
      print("")
      life=life-1
      print("Lives left :", life)
      print("Computer Lives left :", complife)
   if rps == "rock" and computer == "scissors":
      print("you chose Rock ", rock)
      print("The computer choose scissors")
      print(scissors)
      print('')
      print('')
      print("YOU WIN!!")
      print("")
      print("")
      complife=complife-1
      print("Lives left :", life)
      print("Computer lives left:", complife )
   if rps == "rock" and computer == "rock":
      print("you chose Rock ", rock)
      print("The computer choose rock")
      print(rock)
      print('')
      print('')
      print("DRAW!!")
      print("")
      print("")
      print("Lives left :", life)
      print("Computer lives left:", complife )
#paper statements
   if rps == "paper" and computer == "scissors":
      print("your chose paper ",paper)
      print("The computer choose scissors",)
      print(scissors)
      print('')
      print('')
      print("YOU LOSE!!")
      print("")
      print("")
      life=life-1
      print("Lives left :", life)
      print("computer Lives left:", complife)
   if rps == "paper" and computer == "rock":
      print("you chose Paper ", paper)
      print("The computer choose rock")
      print(rock)
      print('')
      print('')
      print("YOU WIN!!")
      print("")
      print("")
      complife=complife-1
      print("Lives left :", life)
      print("Computer lives left:", complife )
   if rps == "paper" and computer == "paper":
      print("you chose paper ", paper)
      print("The computer choose paper")
      print('')
      print('')
      print(paper)
      print('')
      print('')
      print("DRAW!!")
      print("")
      print("")
      print("Lives left :", life)
      print("Computer lives left:", complife )
#scissors statements
   if rps == "scissors" and computer == "rock":
      print("you chose scissors ",scissors)
      print("The computer choose",computer)
      print(rock)
      print('')
      print('')
      print("YOU LOSE!!")
      print("")
      print("")
      life=life-1
      print("Lives left :", life)
      print("computer Lives left:", complife)
   if rps == "scissors" and computer == "paper":
      print("you chose scissors ", scissors)
      print("The computer choose paper")
      print(paper)
      print('')
      print('')
      print("YOU WIN!!")
      print("")
      print("")
      complife=complife-1
      print("Lives left :", life)
      print("Computer lives left:", complife )
   if rps == "scissors" and computer == "scissors":
      print("you chose scissors ", scissors)
      print("The computer choose scissors")
      print('')
      print('')
      print(scissors)
      print('')
      print('')
      print("DRAW!!")
      print("")
      print("")
      print("Lives left :", life)
      print("Computer lives left:", complife )
   if life == 0 :
      print("YOU ARE LOST")
      print("THANKS FOR PLAYING")
      exit()

   if complife == 0:
      print("YOU ARE THE WINNER")
      print("THANKS FOR PLAYING")
      exit()

import random
print("Enter (q)uit to quit \n \n \n")
while True:
    comp_turn = random.randint(1,3) #Generates random value between 1 and 3(both included). Refer readme file for more details
    # 1 - rock
    # 2 - paper
    # 3 - scissor
 
    user_turn = input("Enter (r)ock, (p)aper or (s)cissor: ")
    
    if user_turn.lower() == "r" or user_turn.lower() == "rock":
        if comp_turn == 1:
            print("Computer entered rock. It's a draw! \n")
        elif comp_turn == 2:
            print("Computer entered paper. You loose \n")
        else:
            print("Computer entered scissor. You win! \n")
            
            
    elif user_turn.lower() == "p" or user_turn.lower() == "paper":
        if comp_turn == 1:
            print("Computer entered rock. You win! \n")
        elif comp_turn == 2:
            print("Computer entered paper. It's a draw! \n")
        else:
            print("Computer entered scissor. You loose \n")
            
            
    elif user_turn.lower() == "s" or user_turn.lower() == "scissor":
        if comp_turn == 1:
            print("Computer entered rock. You loose \n")
        elif comp_turn == 2:
            print("Computer entered paper. You win! \n")
        else:
            print("Computer entered scissor. It's a draw! \n")
            
    elif user_turn.lower() == "q" or user_turn.lower() == "quit":
        print("it was a pleasure playing with you. See ya!")
        break
    
    





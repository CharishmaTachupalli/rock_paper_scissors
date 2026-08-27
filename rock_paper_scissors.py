import random

user_choice=int(input("your turn...(0,1,2)\n"))
computer_choice=random.randint(0,2)
print(f"Computer choice is {computer_choice}")
print("Your choice is",user_choice)
if user_choice > 2 or user_choice < 0:
    print("enter valid Input(0,1,2).")
else:
    if computer_choice == user_choice:
        print("Its a Tie")
    elif user_choice==2 and computer_choice==0:
        print("You Lose...")
    elif computer_choice==2 and user_choice==0:
        print("You Win....")
    elif computer_choice > user_choice:
        print("You Lose...")
    else:
        print("You Win...")

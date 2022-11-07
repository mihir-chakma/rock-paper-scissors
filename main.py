import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

choice_list = [rock, paper, scissor]

print("Welcome to Rock Paper Scissor Game.")
print('Choose Rock - 0, Paper - 1, Scissor - 2.\n') 

# user choice 
user_choice = int(input("Enter your choce: "))
print("\nYour choice: ")
print(choice_list[user_choice])

# computer choice 
computer_choice = random.randint(0, 2)

print("Computer choice: ")
print(choice_list[computer_choice])

if user_choice > 2 or user_choice < 0:
    print('You lose !! (Because your choice wrong input.')
elif user_choice == 0 and computer_choice == 2:
    print('You win !')
elif computer_choice == 0 and user_choice == 2:
    print('You lose !')
elif computer_choice > user_choice:
    print('You lose !')
elif user_choice > computer_choice:
    print('You win !')
elif user_choice == computer_choice:
    print('It\'s draw !')


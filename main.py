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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]

user_choice = int(input('please enter 0 for rock, 1 for paper or 2 for scissors\n'))
if user_choice < 3 and user_choice >= 0:
    print(game_images[user_choice])
else:
    print('You entered a number out of the range of 0 - 2 Try Again Later Bye!')

computer_choice = random.randint(0, 2)
print('The Computer Choose:')
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print('You typed an incorrect input, You Lose!')
elif user_choice == 0 and computer_choice == 2:
    print('You Win!')
elif computer_choice > user_choice:
    print('You Lose!')
elif user_choice == computer_choice:
    print('Draw!')
elif computer_choice == 0 and user_choice == 2:
    print('You Lose!')
elif user_choice > computer_choice:
    print('You Win!')

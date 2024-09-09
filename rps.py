import random
rock= '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
     '''
paper='''
    _______
---'   __)__
           ______)
          _______)
          _______)
---.)
'''
scissors='''
   ________
---'   __)__
           ______)
      ___________)
    ()
---.(_)
'''
game_images=[rock,paper,scissors]
#take input from user
user_choice=int(input('enter your choice:type 0 for rock,1 for paper,2 for scissors.'))
#printing invalid if entered another choices
if user_choice>=3 or user_choice<0:
    print("you entered invalid number,you lose")
#determining the winning or loosing position
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choice:")
    print(game_images[computer_choice])
    if computer_choice==user_choice:
        print("its a draw")
    elif computer_choice==2 and user_choice==0:
        print("you win")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif computer_choice>user_choice:
        print("you lose")
    elif computer_choice<user_choice:
        print("you win")
#exit from the loop
print("thanks for playing!!")

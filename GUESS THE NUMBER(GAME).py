import random
import sys

def startup():
    a = "-"
    a1 = a.center(24, "-")
    game_name = "!GUESS THE NUMBER!  |"
    game_name1 = game_name.center(25)
    print(a1+"\n|"+game_name1+"\n"+a1)

range_num = random.randrange(1,100)
ans_num = random.randrange(1,range_num)
counting_tries = 0
chances = 5

startup()
print()
y_name = input("What's your name: ")
print(f"\n--->Hello, {y_name}! ***(You've 5 Chances!)***\n\n->Let's Start!! I'm guessing a number between 1-{range_num}")
print("\n->You think the number is:-  ")


while 1:
    y_choice = int(input())
    counting_tries += 1
    chances = chances - 1
    game_over = "GAME OVER !!!"
    game_over1 = game_over.center(21,"-")
    if chances == 0:
        print(f"{game_over1}\n\n->The number was {ans_num}")
        sys.exit()
    if y_choice > range_num:
        print("Your guess is out of range! Try Again...")
        continue

# WARNING FOR THE LAST CHANCE
    
    if chances == 1:
        print("\nYou'Ve Only 1 Chance Left!!")

# CONDITIONS THAT ARE APPLIED UPON USER'S GUESSES

    if y_choice < (ans_num-3):
        print("\nYour guess is too LOW!")
        continue
    
    elif y_choice > (ans_num-3) and y_choice < ans_num :
        print("\nYou're almost there but still a little LOW!")
        continue
    
    elif y_choice > (ans_num+3):
        print("\nYour guess is too HIGH!")
        continue
        
    elif y_choice < (ans_num+3) and y_choice > ans_num :
        print("\nYou're almost there but still a little HIGH")
        continue
    
    if y_choice == ans_num:
        print("\nEUREKA!!! YOU'VE GOT THE NUMBER...")
        print(f"You tried only {counting_tries} time(s)")
        break
        
   
        
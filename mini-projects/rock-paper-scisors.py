import random

def play():
    user = input("Choose: 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    
    if user not in ['r', 'p', 's']:
        return "Invalid input!"
    
    computer = random.choice(['r', 'p', 's'])
    
    print(f"You: {user}, Computer: {computer}")
    
    if user == computer:
        return 'Tie!'
    
    # Check all win conditions
    if (user == 's' and computer == 'p') or \
       (user == 'p' and computer == 'r') or \
       (user == 'r' and computer == 's'):
        return 'You win!'
    else:
        return 'Computer wins!'

# Play the game
print(play())

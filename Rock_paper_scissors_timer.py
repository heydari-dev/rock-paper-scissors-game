from Rock_paper_scissors_game_data import ACTION, WIN, score, save_score
from random import choice
from Rock_paper_scissors_decorators import game_decorator

def user_choice():
    """Get and validate player input."""
    while True:
        user_input = input('Please enter your choice (s, p, r): ').lower()
        if user_input in ACTION:
            return user_input
        print("Invalid choice. Please enter 's', 'p', or 'r'.")

def system_choice():
    """Randomly select a choice for the system."""
    return choice(list(ACTION.keys()))

def win_action(user, system):
    """Determine the winning action based on user and system choices."""
    return WIN.get((user, system), WIN.get((system, user), 'Equal'))

def find_winner(user, system, win_act, result):
    """Determine the winner and update the score."""
    if user == win_act:
        result['user_score'] += 1
        print('..........You Win..........')
    elif system == win_act:
        result['system_score'] += 1
        print('..........System Wins..........')
    return result

def check_winner(result):
    """Check if either the user or system has reached the winning score of 3."""
    return result['user_score'] < 3 and result['system_score'] < 3

def scoreboard(result):
    """Display the final scoreboard and ask for a replay."""
    if result['user_score'] == 3:
        score['total_user'] += 1
    else:
        score['total_system'] += 1
    
    save_score()  # Save updated scores
    
    print('#' * 80)
    print(f'Total score - User: {score["total_user"]}, System: {score["total_system"]}')
    print('#' * 80)
    print('_' * 80)
    
    while True:
        user_result = input('Do you want to continue? (y/n): ').lower()
        if user_result in ('y', 'n'):
            break
    
    if user_result == 'y':
        play_game()
    else:
        print('Thank you for playing! :)')

def play_game():
    """Main game loop."""
    result = {'user_score': 0, 'system_score': 0}
    while check_winner(result):
        user = user_choice()
        system = system_choice()
        win_act = win_action(user, system)
        
        if win_act == 'Equal':
            print("..........It's a Tie..........")
        else:
            find_winner(user, system, win_act, result)
        
        print(f'Your Choice: {ACTION[user]}   System Choice: {ACTION[system]}')
        print(f'Score - User: {result["user_score"]} | System: {result["system_score"]}')
        print('_' * 80)
    
    scoreboard(result)

@game_decorator
def play():
    """Start the game with timing enabled."""
    play_game()

if __name__ == '__main__':
    play()


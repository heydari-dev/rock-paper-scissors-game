import json
import os

# Available actions: Scissors (s), Paper (p), Rock (r)
ACTION = {'s': 'Scissors', 'p': 'Paper', 'r': 'Rock'}

# Winning combinations
WIN = {
    ('r', 's'): 'r',  # Rock beats Scissors
    ('s', 'p'): 's',  # Scissors beat Paper
    ('p', 'r'): 'p'   # Paper beats Rock
}

# Score storage file
SCORE_FILE = "score.json"

# Load previous scores if available, otherwise initialize new scores
if os.path.exists(SCORE_FILE):
    with open(SCORE_FILE, "r") as f:
        score = json.load(f)
else:
    score = {'total_user': 0, 'total_system': 0}
    
# Function to save scores to file
def save_score():
    """Save the updated score to a JSON file."""
    with open(SCORE_FILE, "w") as f:
        json.dump(score, f)

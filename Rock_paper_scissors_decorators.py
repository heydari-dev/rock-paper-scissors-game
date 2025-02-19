from datetime import datetime

def game_decorator(func):
    """Decorator to measure and display the duration of the game."""
    def wrap_func(*args, **kwargs):
        start_time = datetime.now()  # Capture start time
        result_game = func(*args, **kwargs)  # Execute the game function
        finish_time = datetime.now()  # Capture finish time

        # Calculate total elapsed time in seconds
        total_seconds = (finish_time - start_time).total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)

        # Display formatted game duration
        print(f'Game Duration: {hours:02}:{minutes:02}:{seconds:02}')
        return result_game
    
    return wrap_func


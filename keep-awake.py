import pyautogui
import time
import random
from datetime import datetime

def keep_awake():
    while True:
        # Generate random distances for mouse movement
        x_move = random.randint(-3, 3)
        y_move = random.randint(-3, 3)

        # Move the mouse
        pyautogui.move(x_move, y_move)

        # Simulate a keyboard press (e.g., shift key)
        pyautogui.press('shift')

        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Determine direction for logging
        x_direction = 'right' if x_move > 0 else 'left'
        y_direction = 'down' if y_move > 0 else 'up'

        # Print detailed information about the action
        print(f"Cursor moved {abs(x_move)}px to the {x_direction} and {abs(y_move)}px to the {y_direction} at {current_time}")

        # Wait for a minute or adjust the sleep time if necessary
        time.sleep(60)

if __name__ == "__main__":
    keep_awake()

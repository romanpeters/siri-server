import time
import keyboard

def hey_siri(query) -> None:
    """
    Simulate key presses to interact with Siri
    """
    keyboard.press('command+space')
    time.sleep(0.3)
    keyboard.release('command+space')
    time.sleep(0.2)
    keyboard.write(query)
    keyboard.send('enter')
    print(query)

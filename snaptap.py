import keyboard

def on_direction(direction):
    current_direction = None
    
    if current_direction == direction or keyboard.is_pressed('space'):
        return    
    if (current_direction == current_direction and current_direction != direction):
        if current_direction!=None: 
            keyboard.release(current_direction)

    current_direction = direction
    keyboard.press(current_direction)

def main():
    keyboard.on_press_key('a', lambda _: on_direction('a'))
    keyboard.on_press_key('d', lambda _: on_direction('d'))
    keyboard.on_press_key('w', lambda _: on_direction('w'))
    keyboard.on_press_key('s', lambda _: on_direction('s'))

    keyboard.wait("f6")

if __name__ == "__main__":
    main()
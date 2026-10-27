from vex import *

# Initialize brain and touch LED
brain = Brain()
touch_led = Touchled(Ports.PORT1)

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Touch LED Diagnostic")
    
    while True:
        brain.screen.set_cursor(3, 1)
        if touch_led.pressing():
            brain.screen.print("Touch: TOUCHED ")
            # Change color to green when pressed
            touch_led.set_color(Color.GREEN)
        else:
            brain.screen.print("Touch: OPEN    ")
            # Keep color red when idle
            touch_led.set_color(Color.RED)
        wait(20, MSEC)

if __name__ == "__main__":
    main()

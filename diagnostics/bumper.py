from vex import *

# Initialize brain and bumper switch
brain = Brain()
bumper = Bumper(Ports.PORT1)

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Bumper Diagnostic")
    
    while True:
        brain.screen.set_cursor(3, 1)
        if bumper.pressing():
            brain.screen.print("Status: PRESSED    ")
        else:
            brain.screen.print("Status: RELEASED   ")
        wait(20, MSEC)

if __name__ == "__main__":
    main()

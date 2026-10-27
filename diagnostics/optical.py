from vex import *

# Initialize brain and optical sensor
brain = Brain()
optical_sensor = Optical(Ports.PORT4)

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Optical Diagnostic")
    
    optical_sensor.set_light(LedStateType.ON) 
    
    while True:
        hue = optical_sensor.hue()
        brightness = optical_sensor.brightness()
        
        brain.screen.set_cursor(3, 1)
        brain.screen.print("Hue: {:.1f}      ".format(hue))
        brain.screen.set_cursor(4, 1)
        brain.screen.print("Brightness: {:.1f}% ".format(brightness))
        wait(50, MSEC)

if __name__ == "__main__":
    main()

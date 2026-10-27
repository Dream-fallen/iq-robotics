from vex import *

# Initialize brain and inertial sensor
brain = Brain()
inertial_sensor = Inertial(Ports.PORT1)

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Inertial Diagnostic")
    
    # Calibrate before reading
    brain.screen.set_cursor(2, 1)
    brain.screen.print("Calibrating...")
    inertial_sensor.calibrate()
    
    # FIX: Changed lowercase msec to uppercase MSEC
    while inertial_sensor.is_calibrating():
        wait(10, MSEC)
        
    brain.screen.clear_line(2)
    
    while True:
        # Read heading and pitch angles
        heading = inertial_sensor.heading(DEGREES)
        pitch = inertial_sensor.orientation(OrientationType.PITCH)
        
        brain.screen.set_cursor(3, 1)
        brain.screen.print("Heading: {:.1f} deg   ".format(heading))
        brain.screen.set_cursor(4, 1)
        brain.screen.print("Pitch: {:.1f} deg     ".format(pitch))
        
        # FIX: Fixed spelling typo from MESC to MSEC
        wait(50, MSEC)

if __name__ == "__main__":
    main()

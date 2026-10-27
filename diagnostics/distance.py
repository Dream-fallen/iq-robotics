from vex import *

# Initialize brain and distance sensor
brain = Brain()
# Use the Distance class and assign to Port 1
distance_sensor = Distance(Ports.PORT1)

def main():
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Distance Diagnostic")
    
    while True:
        brain.screen.set_cursor(3, 1)
        
        dist_mm = distance_sensor.object_distance(MM)
        
        # Printing extra spaces ensures older digits are completely erased
        brain.screen.print("Distance: {} mm      ".format(dist_mm))
        
        # Brief delay to allow the hardware screen to refresh smoothly
        wait(50, MSEC)

if __name__ == "__main__":
    main()

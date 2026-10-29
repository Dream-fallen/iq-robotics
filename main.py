from vex import *

# Initialize brain 
brain = Brain()

# Initialize the Controller
con = Controller()

# Initialize your drive motors 
left_motor = Motor(Ports.PORT7)
right_motor = Motor(Ports.PORT12, True) # True reverses this side
back_shared_motor = Motor(Ports.PORT9)  # <--- Your new third motor 

# Initialize your Touch LEDs
left_status_led = Touchled(Ports.PORT1)
right_status_led = Touchled(Ports.PORT6)

def main():
    # --- DEFINE YOUR UNIQUE CUSTOM RGB COLORS HERE ---
    # format: Color(Red, Green, Blue) from 0 to 255
    color_ready = Color(100, 255, 100)     # Pastel Green
    color_moving = Color(100, 100, 255)    # Pastel Blue
    color_flash = Color(255, 100, 100)     # Pastel Red
    
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Drive Mode: TANK")
    
    # LEDs turn to your unique ready color immediately
    left_status_led.set_color(color_ready) 
    right_status_led.set_color(color_ready) 
    
    # Deadband threshold to prevent motor humming/drifting when joysticks are centered
    deadband = 10 
    
    # Drive Mode State: True for Tank, False for Arcade
    is_tank_drive = True
    toggle_was_pressed = False  # For button debouncing
    
    # LED indicator flash tracking (in milliseconds)
    flash_duration = 300  
    flash_timer = 0             
    
    while True:
        # --- TOGGLE LOGIC WITH DEBOUNCING ---
        if con.buttonLUp.pressing(): 
            if not toggle_was_pressed:
                is_tank_drive = not is_tank_drive  
                toggle_was_pressed = True          
                
                flash_timer = flash_duration
                
                brain.screen.clear_screen()
                brain.screen.set_cursor(1, 1)
                
                if is_tank_drive:
                    brain.screen.print("Drive Mode: TANK")
                    brain.play_note(4, 0, 200)
                else:
                    brain.screen.print("Drive Mode: ARCADE")
                    brain.play_note(6, 0, 200)
        else:
            toggle_was_pressed = False 

        # --- DRIVE LOGIC DEPENDING ON MODE ---
        if is_tank_drive:
            # --- TANK DRIVE ---
            left_power = con.axisA.position()   
            right_power = con.axisD.position()  
        else:
            # --- ARCADE DRIVE ---
            speed = con.axisA.position()        
            turn = con.axisC.position()         
            
            left_power = speed + turn           
            right_power = speed - turn          

        # Calculate shared power for the center/back motor (average of both sides)
        shared_power = (left_power + right_power) / 2

        # Track if motors are actively moving past the deadband threshold
        left_moving = abs(left_power) > deadband
        right_moving = abs(right_power) > deadband
        back_moving = abs(shared_power) > deadband
        
        # --- MOTOR OUTPUT CONTROLS ---
        if left_moving:
            left_motor.spin(FORWARD, left_power, PERCENT)
        else:
            left_motor.stop()
            
        if right_moving:
            right_motor.spin(FORWARD, right_power, PERCENT)
        else:
            right_motor.stop()

        # Apply power to the new shared third motor
        if back_moving:
            # Note: Change FORWARD to REVERSE below if your center wheel spins backward!
            back_shared_motor.spin(FORWARD, shared_power, PERCENT)
        else:
            back_shared_motor.stop()
            

        # --- LED COLOR LOGIC WITH FLASH PRIORITIZATION ---
        if flash_timer > 0:
            left_status_led.set_color(color_flash)
            right_status_led.set_color(color_flash)
            flash_timer -= 20
        else:
            if left_moving:
                left_status_led.set_color(color_moving)
            else:
                left_status_led.set_color(color_ready)
                
            if right_moving:
                right_status_led.set_color(color_moving)
            else:
                right_status_led.set_color(color_ready)
            
        wait(20, MSEC)

if __name__ == "__main__":
    main()

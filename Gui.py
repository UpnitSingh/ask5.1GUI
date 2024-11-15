from tkinter import *
from gpiozero import LED
import RPi.GPIO as GPIO
from functools import partial

# GPIO setup (BCM mode)
GPIO.setmode(GPIO.BCM)

# Initialize LEDs with correct GPIO pins (BCM numbering)
white_led = LED(17)  # Using GPIO 17 (Pin 11 on the Pi)
green_led = LED(27)  # Using GPIO 27 (Pin 13 on the Pi)
yellow_led = LED(22) # Using GPIO 22 (Pin 15 on the Pi)

# Create the main window for the GUI
main_window = Tk()
main_window.title("LED Controller")

# Center the GUI window
def center_window(window, width=400, height=200):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

center_window(main_window)

# Set background color for the main window
main_window.configure(bg="#D4E6F1")  # Light blue background

# Function to turn on the selected LED and turn off others
def toggle_led(selected_led):
    # Turn off all LEDs first
    white_led.off()
    green_led.off()
    yellow_led.off()
    
    # Reset button texts to indicate LEDs are off
    white_button.config(text="WHITE LED ON", bg="white")
    green_button.config(text="GREEN LED ON", bg="white")
    yellow_button.config(text="YELLOW LED ON", bg="white")
    
    # Turn on the selected LED and change the button text
    if selected_led == 'white':
        white_led.on()
        white_button.config(text="WHITE LED OFF", bg="#D5DBDB")  # Light gray
    elif selected_led == 'green':
        green_led.on()
        green_button.config(text="GREEN LED OFF", bg="#82E0AA")  # Light green
    elif selected_led == 'yellow':
        yellow_led.on()
        yellow_button.config(text="YELLOW LED OFF", bg="#F7DC6F")  # Light yellow

# Function to close the window and clean up GPIO resources
def exit_program():
    GPIO.cleanup()  # Clean up GPIO settings
    main_window.destroy()  # Close the GUI window

# Using functools.partial to pass arguments to toggle_led
white_button = Button(main_window, text="WHITE LED ON", command=partial(toggle_led, 'white'), fg='black', bg="white", height=2, width=15)
white_button.grid(row=0, column=0, padx=10, pady=10)

green_button = Button(main_window, text="GREEN LED ON", command=partial(toggle_led, 'green'), fg='green', bg="white", height=2, width=15)
green_button.grid(row=0, column=1, padx=10, pady=10)

yellow_button = Button(main_window, text="YELLOW LED ON", command=partial(toggle_led, 'yellow'), fg='orange', bg="white", height=2, width=15)
yellow_button.grid(row=0, column=2, padx=10, pady=10)

# Create the exit button to close the program
exit_button = Button(main_window, text="EXIT", command=exit_program, fg='black', bg="#F7DC6F", height=2, width=15)
exit_button.grid(row=1, column=1, padx=10, pady=20)

# Set up window close protocol to clean up GPIO 
main_window.protocol("WM_DELETE_WINDOW", exit_program)

# Run the Tkinter main loop to display the GUI
main_window.mainloop()

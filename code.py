# gimme-that-grub-cpb.py
import board, time, pwmio
from simpleio import map_range
from analogio import AnalogIn
from adafruit_motor import servo

# Create a pwm object
pwm = pwmio.PWMOut(board.A2, frequency=50) # My object / the servo / is on A2
# Create and calibrate a Servo object
servo_1 = servo.Servo(pwm, min_pulse = 550, max_pulse = 2350)

# Create a potentiometer object
potentiometer = AnalogIn(board.A3)
output_range = 180
max_reading = 65535

print("Gimme That Grub Running")
last_servo_reading = 0
while True:
        pot_reading = potentiometer.value
        angle = map_range(pot_reading, 0, max_reading, 0, output_range) # with map_range
        # angle = int( pot_reading * (output_range/max_reading) ) # with calculation
        angle = output_range-angle # flip angle on 180° access to mimic pot turn
        print(f"pot value {pot_reading}, angle {angle}")
        servo_1.angle = angle
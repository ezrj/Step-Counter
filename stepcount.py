import board
import busio
import adafruit_mpu6050 as adafruit
import time
import math
import matplotlib.pyplot as plt
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit.MPU6050(i2c)

x_ref, y_ref, z_ref = [], [], []

check = False

print("Calibrating...")


for i in range(100):
    data = mpu.acceleration 
    x_ref.append(data[0])
    y_ref.append(data[1])
    z_ref.append(data[2])
    

x_avg = np.sum(x_ref)/100
y_avg = np.sum(y_ref)/100
z_avg = np.sum(z_ref)/100

print(x_avg, " ", y_avg, " ", z_avg, " ")
print("Calibration Complete")



x_data, y_data, z_data = [], [], []
step_count = 0

    
def detect_step(acceleration, threshold=4):
    #calculate the magnitude of the acceleration vector
    global check
    magnitude = np.sqrt(sum(a**2 for a in acceleration))
    
    #detect step if magnitude exceeds a threshold
    if magnitude > threshold:
        if check == False:
            check = True
            return True
    else:
        check = False
        return False
        
    #time.sleep(.6)


#collect data
while (True):
    data = mpu.acceleration  #assuming this gets your acceleration data
    x_data.append(data[0])
    y_data.append(data[1])
    z_data.append(data[2])
    
#read acceleration
    
        
    # Step detection
    data_new = ((data[0] - x_avg), (data[1] - y_avg), (data[2] - z_avg))
    if detect_step(data_new):
        step_count += 1
        print(f"Step detected! Total steps: {step_count}")
    time.sleep(.1)
        
    
    
    

#plotting
plt.figure(figsize=(14, 6))
plt.plot(x_data, label='X', color="blue")
plt.plot(y_data, label='Y', color="red")
plt.plot(z_data, label='Z', color="yellow")
plt.legend(loc="upper left")
plt.show()

# 1. Setting up Robot
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

        
# 2. Adding Robot Logic
def control_bot(self, new_speed, new_direction):
    self.motor_speed = new_speed
    self.direction = new_direction
 
def adjust_sensor(self, new_sensor_range):
    self.sensor_range = new_sensor_range


# 3. Enhanced Constructor
def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range


# 4. Controlling them All
class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999


# 5. Identifying Robots
class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
 
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
 
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
 
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
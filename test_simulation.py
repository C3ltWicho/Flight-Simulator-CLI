class FlightSimulator:
    def __init__(self, altitude=10000, speed=300, temperature=20):
        
        self.altitude = altitude
        self.speed = speed
        self.temperature = temperature

    #Methods
    def increase_altitude(self,amount):
            self.altitude += amount
        
    def increase_speed(self,speed):
            self.speed += speed
        
    def increase_temperature(self,temperature):
            self.temperature += temperature

    def decrease_altitude(self,amount):
            self.altitude = max(0, self.altitude - amount)
        
    def decrease_speed(self,amount):
            try:
                   amount = int(amount)
                   self.speed = max(0, self.speed - amount)
            except ValueError:
                   raise ValueError("Invalid amount for speed decrease.")
                   

    def get_state(self):
            return f"Altitude: {self.altitude}, Speed: {self.speed}, Temperature:{self.temperature}"
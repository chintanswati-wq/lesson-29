# create class 
class vehicle:

    # create init method
    def __init__(self , max_speed, mileage):

        #bind the arguments
        self.max_speed = max_speed 
        self.mileage = mileage

# obeject creation
modelX = vehicle(240, 18)

print("Model Max Speed :", modelX.max_speed)
print("model mileage :", modelX.mileage)
# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.

class  Vehicle:
    def __init__(self):
        pass

    # This is the base class that is the top of the Hierarchy

class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()

    # Vehicle Attributes is passed into here

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
    # Vehicle and GroundVehicle Attributes are inherited here
    # MotorCycle Attributes are not shared

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
    # Vehicle and GroundVehicle Attributes are inherited here
    # Car Attributes are not Shared


class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()

    # Vehicle Attributes is inherited into here
    # Ground Vehicle Attributes are not shared


class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
    # Vehicle & Flight Vehicle Attributes are inherited into here
    # Not shared with Startship

class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
    # Vehicle & Flight Vehicle Attributes are inherited into here
    # Not shared with Airplane

# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

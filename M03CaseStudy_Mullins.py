"""
Author:  Emily Mullins
Date written: 11/19/2023
File: M03CaseStudy_Mullins.py
Short Desc: This program will create a class for Vehicle and a subclass of Vehicle Automobile.
A user will be able to enter in information about a vehicle and receive output of the information.
            
"""

#Creating class Vehicle 
class Vehicle():
    def __init__(self, vehicle_type) -> None:
        self.vehicle_type = vehicle_type
                 
#Creating subclass Automobile
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof) -> None:
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#Function to get door numbers, 2 or 4, and return. Must be int, must be 2 or 4.
def get_doors():
    try:
        doors = int(input("Enter the number of doors (2 or 4): "))
    except:
        print("Invalid input. Please enter a valid number of doors.")
        return get_doors()
    if doors not in [2, 4]:
       print("Please enter a valid number of doors (2 or 4).") 
       return get_doors()
    else:
        return doors
        
# Function to get year input and return. Must be int.
def get_year():
    try:
       year = int(input('Enter the vehicle year: ')) 
       return year 
    except:    
        print('Invalid year.')
        return get_year()
        
    
# function to get roof type (solid or sunroof) and return
def get_roof():
    roof = input('Enter the vehicle roof type (Solid or Sunroof): ').strip().lower()
    if roof not in ['solid', 'sunroof']:
        print('Not a valid rooftype.')
        return get_roof()
    else:
        return roof

# Get input, store values
vehicle_type = input('Enter the vehicle type: ')
year = get_year()
make = input('Enter the vehicle make: ')
model = input('Enter the vehicle model: ')
doors = get_doors()
roof = get_roof()

#create Automobile object.
car1 = Automobile(vehicle_type, year, make, model, doors, roof)

#Print automobile object info
print()
print(f'Vehicle Type: {car1.vehicle_type} \n'
f'Vehicle Year: {car1.year} \n'
f'Vehicle Type: {car1.make} \n'
f'Vehicle Type: {car1.model} \n'
f'Vehicle Type: {car1.doors} \n'
f'Vehicle Type: {car1.roof}')



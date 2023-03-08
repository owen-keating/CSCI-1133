import math

def nickels_to_cents(nickels):
    '''
    Purpose: converts number of nickels to how many cents we have
    Input Parameter(s):
        nickels: the number of nickels we have
    Return Value: the amount of cents we have
    '''
    total = nickels * 5
    return total

def fahrenheit_to_celsius(fahrenheit):
    '''
    Purpose: converts the temperature from degrees fahrenheit to degrees celsius
    Input Parameter(s):
        fahrenheit: the current temperature in degrees fahrenheit
    Return Value: the current temperature in degrees celsius
    '''
    tmp = fahrenheit - 32
    cels = tmp * 5.0 / 9.0
    return cels

def volume_sphere(radius):
    '''
    Purpose: finds the volume of a sphere with a known radius
    Input Parameter(s):
        radius: the radius of the sphere we are trying to find the volume of
    Return Value: the volume of the sphere
    '''
    pi = 3.14159
    rcubed = radius * radius * radius
    volume = pi * 4.0 * rcubed / 3.0
    return volume

def pounds_to_kilograms(pounds):
    '''
    Purpose: converts the weight of something from pounds into kilograms
    Input Parameter(s):
        pounds: the weight in pounds
    Return Value: the weight in kilograms
    '''
    kilos = 0.45359 * pounds
    return kilos

def area_circle(radius):
    '''
    Purpose: finds the area of a circle with a known radius
    Input Parameter(s):
        radius: the radius of the circle we are trying to find the area of
    Return Value: the area of the circle
    '''
    pi = 3.14159
    rsquared = radius * radius
    area = pi * rsquared
    return area

def surface_area_sphere(radius):
    '''
    Purpose: finds the surface area of a sphere with a known radius
    Input Parameter(s):
        radius: the radius of the sphere we are trying to find the surface area of
    Return Value: the surface area of the sphere
    '''
    pi = 3.14159
    rsquared = radius * radius
    sa = 4.0 * rsquared * pi
    return sa

def miles_per_gallon(start, end, gas):
    '''
    Purpose: compute a car's miles per gallon using the change in mileage and gallons of gas used during a road trip
    Input Parameter(s):
        start: the mileage on the car at the start of the trip
        end: the mileage on the car at the end of the trip
        gas: the amount of gas used during the trip
    Return Value: the miles per gallon that the given car has
    '''
    diff = end - start
    mpg = diff / gas
    return mpg

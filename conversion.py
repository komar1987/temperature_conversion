def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius/5*9 + 32
    return fahrenheit

def celsius_to_kelvin(celcius):
    return celsius + 273.15
    
def kelvin_to_fahrenheit(kelvin):
    celcius = kelvin - 273.15
    return celcius_to_fahrenheit(celcius)
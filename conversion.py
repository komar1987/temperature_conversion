def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius/5*9 + 32
    return fahrenheit

def celsius_to_kelvin(celcius):
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin- 273.15
    return celsius_to_fahrenheit(celsius)
    

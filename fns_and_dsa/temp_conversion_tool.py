CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
FAHRENHEIT_OFFSET = CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{fahrenheit}°F is {celsius}°C"

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return f"{celsius}°C is {fahrenheit}°F"

temperature = float(input("Enter the temperature to convert: "))
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

match temp_unit:
    case "F":
        result = convert_to_celsius(temperature)
        print(result)
    case "C":
        result = convert_to_fahrenheit(temperature)
        print(result)
    case _ :
        print(f"Invalid input: {temperature}, {temp_unit}")

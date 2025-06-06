FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return f"{fahrenheit}°F is {fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR}°C"

def convert_to_fahrenheit(celsius):
    return f"{celsius}°C is {celsius * CELSIUS_TO_FAHRENHEIT_FACTOR}°F"


temperature = float(input("Enter the temperature to convert: "))
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

match temp_unit:
    case "F":
        result = convert_to_celsius(temperature)
        print(result)
    case "C":
        result = convert_to_fahrenheit(temparature)
        print(result)
    case _ :
        print(f"Invalid input: {temparature}, {temp_unit}")

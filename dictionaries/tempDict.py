temperature_values = [
    "Cº (Celsius)",
    "Fº (Fahrenheit)",
    "K (Kelvin)",
    "Rº (Rankine)"
]

temperature_conversions = {
    "Cº (Celsius)": {
        "Cº (Celsius)": 1,
        "Fº (Fahrenheit)": 0.555555556+32,
        "K (Kelvin)": 1+273.15,
        "Rº (Rankine)": 1.8 + 491.67
    },
    "Fº (Fahrenheit)": {
        "Cº (Celsius)": 1-32*0.5556,
        "Fº (Fahrenheit)": 1,
        "K (Kelvin)": 1+459.67*0.555555556,
        "Rº (Rankine)": 1+459.67
    },
    "K (Kelvin)": {
        "Cº (Celsius)": 1+273.15,
        "Fº (Fahrenheit)": 1-273.15*1.8+32,
        "K (Kelvin)": 1,
        "Rº (Rankine)": 1.8
    },
    "Rº (Rankine)": {
        "Cº (Celsius)": 1-491.67*0.555555556,
        "Fº (Fahrenheit)": 1-459.67,
        "K (Kelvin)": 0.555555556,
        "Rº (Rankine)": 1
    }
}
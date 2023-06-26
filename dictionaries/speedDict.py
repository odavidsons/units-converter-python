"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Dictionary for speed conversions
"""
speed_values = [
    "Kilometers per hour (kph)",
    "Miles per hour (mph)",
    "Meters per second (m/s)",
    "Feet per second (fps)",
    "Knots (kt)"
]

speed_conversions = {
    "Kilometers per hour (kph)": {
        "Kilometers per hour (kph)": 1,
        "Miles per hour (mph)": 0.621371192,
        "Meters per second (m/s)": 0.277777778,
        "Feet per second (fps)": 0.911344,
        "Knots (kt)": 0.539956803
    },
    "Miles per hour (mph)": {
        "Kilometers per hour (kph)": 1.609344,
        "Miles per hour (mph)": 1,
        "Meters per second (m/s)": 0.44704,
        "Feet per second (fps)": 1.46666667,
        "Knots (kt)": 0.868976242
    },
    "Meters per second (m/s)" : {
        "Kilometers per hour (kph)": 3.6,
        "Miles per hour (mph)": 2.23693629,
        "Meters per second (m/s)": 1,
        "Feet per second (fps)": 3.2808399,
        "Knots (kt)": 1.94384449
    },
    "Feet per second (fps)": {
        "Kilometers per hour (kph)": 1.09728,
        "Miles per hour (mph)": 0.681818182,
        "Meters per second (m/s)": 0.3048,
        "Feet per second (fps)": 1,
        "Knots (kt)": 0.592483801
    },
    "Knots (kt)": {
        "Kilometers per hour (kph)": 1.85200,
        "Miles per hour (mph)": 1.15077945,
        "Meters per second (m/s)": 0.514444444,
        "Feet per second (fps)": 1.68780986,
        "Knots (kt)": 1
    },
}
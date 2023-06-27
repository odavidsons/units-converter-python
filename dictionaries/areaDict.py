"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Dictionary for are conversions
"""
area_values = [
    "km² (Square Kilometer)",
    "m² (Square Meter)",
    "mm² (Square Centimeter)",
    "m² (Square Milimeter)",
    "ha (Hectare)",
    "ac (Acre)",
    "mile² (Square mile)",
    "ft² (Square feet)",
    "in² (Square inches)",
    "y² (Square yard)"
]

area_conversions = {
    "km² (Square Kilometer)": {
        "km² (Square Kilometer)": 1,
        "m² (Square Meter)": 1000000,
        "mm² (Square Centimeter)": 10000000000,
        "m² (Square Milimeter)": 1000000000000,
        "ha (Hectare)": 100,
        "ac (Acre)": 247.105381,
        "mile² (Square mile)": 0.386102,
        "ft² (Square feet)": 10763910.42,
        "in² (Square inches)": 1550003100.01,
        "y² (Square yard)": 1195990.05
    },
    "m² (Square Meter)": {
        "km² (Square Kilometer)": 0.000001,
        "m² (Square Meter)": 1,
        "mm² (Square Centimeter)": 10000,
        "m² (Square Milimeter)": 1000000,
        "ha (Hectare)": 0.0001,
        "ac (Acre)": 0.000247,
        "mile² (Square mile)": 0.0000003861,
        "ft² (Square feet)": 10.763910417,
        "in² (Square inches)": 1550.0031,
        "y² (Square yard)": 1.1959900463
    },
    "mm² (Square Centimeter)": {
        "km² (Square Kilometer)": 0.0000000001,
        "m² (Square Meter)": 0.0001,
        "mm² (Square Centimeter)": 1,
        "m² (Square Milimeter)": 100,
        "ha (Hectare)": 00000000.1,
        "ac (Acre)": 0.00002471,
        "mile² (Square mile)": 0.00000003861,
        "ft² (Square feet)": 0.001076,
        "in² (Square inches)": 0.155,
        "y² (Square yard)": 0.0001196
    },
    "m² (Square Milimeter)": {
        "km² (Square Kilometer)": 0.000000000001,
        "m² (Square Meter)": 0.000001,
        "mm² (Square Centimeter)": 0.01,
        "m² (Square Milimeter)": 1,
        "ha (Hectare)": 0.00000000009999999999,
        "ac (Acre)": 0.0000000002471053814,
        "mile² (Square mile)": 0.0000000000003861018768,
        "ft² (Square feet)": 0.0000107639,
        "in² (Square inches)": 0.0015500031,
        "y² (Square yard)": 0.000001196
    },
    "ha (Hectare)": {
        "km² (Square Kilometer)": 0.01,
        "m² (Square Meter)": 10000,
        "mm² (Square Centimeter)": 100000000,
        "m² (Square Milimeter)": 10000000000,
        "ha (Hectare)": 1,
        "ac (Acre)": 2.4710538147,
        "mile² (Square mile)": 0.0038610188,
        "ft² (Square feet)": 107639.10417,
        "in² (Square inches)": 15500031,
        "y² (Square yard)": 11959.900463
    },
    "ac (Acre)": {
        "km² (Square Kilometer)": 0.0040468564,
        "m² (Square Meter)": 4046.8564224,
        "mm² (Square Centimeter)": 40468564.224,
        "m² (Square Milimeter)": 4046856422.4,
        "ha (Hectare)": 0.4046856422,
        "ac (Acre)": 1,
        "mile² (Square mile)": 0.0015624989,
        "ft² (Square feet)": 43560,
        "in² (Square inches)": 6272640,
        "y² (Square yard)": 4840
    },
    "mile² (Square mile)": {
        "km² (Square Kilometer)": 2.58999,
        "m² (Square Meter)": 2589990,
        "mm² (Square Centimeter)": 25899900000,
        "m² (Square Milimeter)": 2589990000000,
        "ha (Hectare)": 258.999,
        "ac (Acre)": 640.00046695,
        "mile² (Square mile)": 1,
        "ft² (Square feet)": 27878420.34,
        "in² (Square inches)": 4014492529,
        "y² (Square yard)": 3097602.26
    },
    "ft² (Square feet)": {
        "km² (Square Kilometer)": 0.00000009290304,
        "m² (Square Meter)": 0.09290304,
        "mm² (Square Centimeter)": 929.0304,
        "m² (Square Milimeter)": 92903.04,
        "ha (Hectare)": 0.0000092903,
        "ac (Acre)": 0.0000229568,
        "mile² (Square mile)": 0.0000000358700381,
        "ft² (Square feet)": 1,
        "in² (Square inches)": 144,
        "y² (Square yard)": 0.1111111111
    },
    "in² (Square inches)": {
        "km² (Square Kilometer)": 0.00000000064516,
        "m² (Square Meter)": 0.00064516,
        "mm² (Square Centimeter)": 6.4516,
        "m² (Square Milimeter)": 645.16,
        "ha (Hectare)": 0.000000064516,
        "ac (Acre)": 0.0000001594225079,
        "mile² (Square mile)": 0.0000000002490974868,
        "ft² (Square feet)": 0.0069444444,
        "in² (Square inches)": 1,
        "y² (Square yard)": 0.0007716049
    },
    "y² (Square yard)": {
        "km² (Square Kilometer)": 0.00000083612736,
        "m² (Square Meter)": 0.83612736,
        "mm² (Square Centimeter)": 8361.2736,
        "m² (Square Milimeter)": 836127.36,
        "ha (Hectare)": 0.0000836127,
        "ac (Acre)": 0.0002066116,
        "mile² (Square mile)": 0.0000003228303429,
        "ft² (Square feet)": 9,
        "in² (Square inches)": 1296,
        "y² (Square yard)": 1
    }
}
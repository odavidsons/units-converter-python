"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Dictionary for volume conversions
"""
power_values = [
    "km³ (Cubic kilometers)",
    "m³ (Cubic meters)",
    "cm³ (Cubic centimeters)",
    "mm³ (Cubic milimeters)",
    "l (Liters)",
    "dl (Deciliters)",
    "cd (Centiliters)",
    "ml (Mililiter)",
    "gl (Galons)",
    "miles³ (Cubic miles)",
    "ft³ (Cubic feets)",
    "in³ (Cubid inches)",
    "y³ (Cubic yards)"

]

power_conversions = {
    "km³ (Cubic kilometers)": {
        "km³ (Cubic kilometers)": 1,
        "m³ (Cubic meters)": 1000000000,
        "cm³ (Cubic centimeters)": 1000000000000000,
        "mm³ (Cubic milimeters)": 1000000000000000000,
        "l (Liters)": 1000000000000,
        "dl (Deciliters)": 1,
        "cd (Centiliters)": 100000000000000,
        "ml (Mililiter)": 1000000000000000,
        "gl (Galons)": 264172176858,
        "miles³ (Cubic miles)": 0.2399128636,
        "ft³ (Cubic feets)": 35314666721,
        "in³ (Cubid inches)": 61023744094732,
        "y³ (Cubic yards)": 1307950619.3
    },
    "m³ (Cubic meters)": {
        "km³ (Cubic kilometers)": 0.000000001,
        "m³ (Cubic meters)": 1,
        "cm³ (Cubic centimeters)": 1000000,
        "mm³ (Cubic milimeters)": 1000000000,
        "l (Liters)": 1000,
        "dl (Deciliters)": 1,
        "cd (Centiliters)": 1,
        "ml (Mililiter)": 1000000,
        "gl (Galons)": 264.17217686,
        "miles³ (Cubic miles)": 0.0000000002399128636,
        "ft³ (Cubic feets)": 35.314666721,
        "in³ (Cubid inches)": 61023.744095,
        "y³ (Cubic yards)": 1.3079506193
    },
    "cm³ (Cubic centimeters)": {
        "km³ (Cubic kilometers)": 0.0000000000000001,
        "m³ (Cubic meters)": 0.000001,
        "cm³ (Cubic centimeters)": 1,
        "mm³ (Cubic milimeters)": 1000,
        "l (Liters)": 0.001,
        "dl (Deciliters)": 1,
        "cd (Centiliters)": 1,
        "ml (Mililiter)": 1,
        "gl (Galons)": 0.0002641722,
        "miles³ (Cubic miles)": 0.0000000000000002399128636,
        "ft³ (Cubic feets)": 0.0000353147,
        "in³ (Cubid inches)": 0.0610237441,
        "y³ (Cubic yards)": 0.000001308
    },
    "mm³ (Cubic milimeters)": {
        "km³ (Cubic kilometers)": 0.000000000000000001,
        "m³ (Cubic meters)": 0.000000001,
        "cm³ (Cubic centimeters)": 0.001,
        "mm³ (Cubic milimeters)": 1,
        "l (Liters)": 0.000001,
        "dl (Deciliters)": 1,
        "cd (Centiliters)": 1,
        "ml (Mililiter)": 0.001,
        "gl (Galons)": 0.0000002641721768,
        "miles³ (Cubic miles)": 0.0000000000000000002399128636,
        "ft³ (Cubic feets)": 0.00000003531466672,
        "in³ (Cubid inches)": 0.0000610237,
        "y³ (Cubic yards)": 0.000000001307950619
    },
    "l (Liters)": {
        "km³ (Cubic kilometers)": 0.000000000001,
        "m³ (Cubic meters)": 0.001,
        "cm³ (Cubic centimeters)": 1000,
        "mm³ (Cubic milimeters)": 1000000,
        "l (Liters)": 1,
        "dl (Deciliters)": 1,
        "cd (Centiliters)": 1,
        "ml (Mililiter)": 1000,
        "gl (Galons)": 0.2641721769,
        "miles³ (Cubic miles)": 0.0000000000002399128636,
        "ft³ (Cubic feets)": 0.0353146667,
        "in³ (Cubid inches)": 61.023744095,
        "y³ (Cubic yards)": 0.0013079506
    },
    "dl (Deciliters)": {
        "km³ (Cubic kilometers)": 1,
        "m³ (Cubic meters)": 1,
        "cm³ (Cubic centimeters)": 1,
        "mm³ (Cubic milimeters)": 1,
        "l (Liters)": 1,
        "dl (Deciliters)": 1,
        "cd (Centiliters)": 1,
        "ml (Mililiter)": 1,
        "gl (Galons)": 1,
        "miles³ (Cubic miles)": 1,
        "ft³ (Cubic feets)": 1,
        "in³ (Cubid inches)": 1,
        "y³ (Cubic yards)": 1
    },
    "cd (Centiliters)": {
        "km³ (Cubic kilometers)": 1,
        "m³ (Cubic meters)": 1,
        "cm³ (Cubic centimeters)": 1,
        "mm³ (Cubic milimeters)": 1,
        "l (Liters)": 1,
        "dl (Deciliters)": 1,
        "cd (Centiliters)": 1,
        "ml (Mililiter)": 1,
        "gl (Galons)": 1,
        "miles³ (Cubic miles)": 1,
        "ft³ (Cubic feets)": 1,
        "in³ (Cubid inches)": 1,
        "y³ (Cubic yards)": 1
    },
    "ml (Mililiter)": {
        "km³ (Cubic kilometers)": 0.0000000000000001,
        "m³ (Cubic meters)": 0.000001,
        "cm³ (Cubic centimeters)": 1,
        "mm³ (Cubic milimeters)": 1000,
        "l (Liters)": 0.001,
        "dl (Deciliters)": 1,
        "cd (Centiliters)": 1,
        "ml (Mililiter)": 1,
        "gl (Galons)": 0.0002641722,
        "miles³ (Cubic miles)": 0.0000000000000002399128636,
        "ft³ (Cubic feets)": 0.0000353147,
        "in³ (Cubid inches)": 0.0610237441,
        "y³ (Cubic yards)": 0.000001308
    },
    "gl (Galons)": {
        "km³ (Cubic kilometers)": 1,
        "m³ (Cubic meters)": 1,
        "cm³ (Cubic centimeters)": 1,
        "mm³ (Cubic milimeters)": 1,
        "l (Liters)": 1,
        "dl (Deciliters)": 1,
        "cd (Centiliters)": 1,
        "ml (Mililiter)": 1,
        "gl (Galons)": 1,
        "miles³ (Cubic miles)": 1,
        "ft³ (Cubic feets)": 1,
        "in³ (Cubid inches)": 1,
        "y³ (Cubic yards)": 1
    }
}
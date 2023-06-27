"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Dictionary for length conversions
"""
length_values = [
    "Tm (Terameter)",
    "Gm (Gigameter)",
    "Mm (Megameter)",
    "km (Kilometer)",
    "hm (Hectometer)",
    "dam (Dekameter)",
    "m (Meter)",
    "dm (Decimeter)",
    "cm (Centimeter)",
    "mm (Milimeter)",
    "um (Micrometer)",
    "nm (Nanometer)"
]

length_conversions = {
    "Tm (Terameter)": {
        "Tm (Terameter)": 1,
        "Gm (Gigameter)": 100,
        "Mm (Megameter)": 100000,
        "km (Kilometer)": 100000000,
        "hm (Hectometer)": 1000000000,
        "dam (Dekameter)": 10000000000,
        "m (Meter)": 100000000000,
        "dm (Decimeter)": 1000000000000,
        "cm (Centimeter)": 10000000000000,
        "mm (Milimeter)": 100000000000000,
        "um (Micrometer)": 100000000000000000,
        "nm (Nanometer)": 100000000000000000000
    },
    "Gm (Gigameter)": {
        "Tm (Terameter)": 0.001,
        "Gm (Gigameter)": 1,
        "Mm (Megameter)": 100,
        "km (Kilometer)": 100000,
        "hm (Hectometer)": 1000000,
        "dam (Dekameter)": 10000000,
        "m (Meter)": 100000000,
        "dm (Decimeter)": 1000000000,
        "cm (Centimeter)": 10000000000,
        "mm (Milimeter)": 100000000000,
        "um (Micrometer)": 100000000000000,
        "nm (Nanometer)": 100000000000000
    },
    "Mm (Megameter)": {
        "Tm (Terameter)": 0.000001,
        "Gm (Gigameter)": 0.001,
        "Mm (Megameter)": 1,
        "km (Kilometer)": 100,
        "hm (Hectometer)": 1000,
        "dam (Dekameter)": 10000,
        "m (Meter)": 100000,
        "dm (Decimeter)": 1000000,
        "cm (Centimeter)": 10000000,
        "mm (Milimeter)": 100000000,
        "um (Micrometer)": 100000000000,
        "nm (Nanometer)": 100000000000000
    },
    "km (Kilometer)": {
        "Tm (Terameter)": 0.000000001,
        "Gm (Gigameter)": 0.000001,
        "Mm (Megameter)": 0.001,
        "km (Kilometer)": 1,
        "hm (Hectometer)": 10,
        "dam (Dekameter)": 100,
        "m (Meter)": 1000,
        "dm (Decimeter)":10000,
        "cm (Centimeter)":100000,
        "mm (Milimeter)": 1000000,
        "um (Micrometer)":1000000000,
        "nm (Nanometer)": 1000000000000
    },
    "hm (Hectometer)": {
        "Tm (Terameter)": 0.0000000001,
        "Gm (Gigameter)": 0.0000001,
        "Mm (Megameter)": 0.0001,
        "km (Kilometer)": 0.1,
        "hm (Hectometer)": 1,
        "dam (Dekameter)": 10,
        "m (Meter)": 100,
        "dm (Decimeter)": 1000,
        "cm (Centimeter)": 10000,
        "mm (Milimeter)": 100000,
        "um (Micrometer)": 100000000,
        "nm (Nanometer)": 100000000
    },
    "dam (Dekameter)": {
        "Tm (Terameter)": 0.00000000001,
        "Gm (Gigameter)": 0.00000001,
        "Mm (Megameter)": 0.00001,
        "km (Kilometer)": 0.01,
        "hm (Hectometer)": 0.1,
        "dam (Dekameter)": 1,
        "m (Meter)": 10,
        "dm (Decimeter)":100,
        "cm (Centimeter)":1000,
        "mm (Milimeter)":10000,
        "um (Micrometer)":10000000,
        "nm (Nanometer)": 10000000000
    },
    "m (Meter)": {
        "Tm (Terameter)": 0.000000001,
        "Gm (Gigameter)": 0.000000001,
        "Mm (Megameter)": 0.000001,
        "km (Kilometer)": 0.001,
        "hm (Hectometer)": 0.01,
        "dam (Dekameter)": 0.1,
        "m (Meter)": 1,
        "dm (Decimeter)":10,
        "cm (Centimeter)":100,
        "mm (Milimeter)":1000,
        "um (Micrometer)":1000000,
        "nm (Nanometer)": 1000000000
    },
    "dm (Decimeter)": {
        "Tm (Terameter)": 0.0000000000001,
        "Gm (Gigameter)": 0.0000000001,
        "Mm (Megameter)": 0.0000001,
        "km (Kilometer)": 0.0001,
        "hm (Hectometer)": 0.001,
        "dam (Dekameter)": 0.01,
        "m (Meter)": 0.1,
        "dm (Decimeter)":1,
        "cm (Centimeter)":10,
        "mm (Milimeter)":100,
        "um (Micrometer)":100000,
        "nm (Nanometer)": 100000000
    },
    "cm (Centimeter)": {
        "Tm (Terameter)": 0.00000000000001,
        "Gm (Gigameter)": 0.00000000001,
        "Mm (Megameter)": 0.00000001,
        "km (Kilometer)": 0.00001,
        "hm (Hectometer)": 0.0001,
        "dam (Dekameter)": 0.001,
        "m (Meter)": 0.01,
        "dm (Decimeter)": 0.1,
        "cm (Centimeter)": 1,
        "mm (Milimeter)": 10,
        "um (Micrometer)": 10000,
        "nm (Nanometer)": 10000000
    },
    "mm (Milimeter)": {
        "Tm (Terameter)": 0.000000000000001,
        "Gm (Gigameter)": 0.000000000001,
        "Mm (Megameter)": 0.000000001,
        "km (Kilometer)": 0.000001,
        "hm (Hectometer)": 0.00001,
        "dam (Dekameter)": 0.0001,
        "m (Meter)": 0.001,
        "dm (Decimeter)": 0.01,
        "cm (Centimeter)": 0.1,
        "mm (Milimeter)": 1,
        "um (Micrometer)": 1000,
        "nm (Nanometer)": 1000000
    },
    "um (Micrometer)": {
        "Tm (Terameter)": 0.000000000000000001,
        "Gm (Gigameter)": 0.000000000000001,
        "Mm (Megameter)": 0.000000000001,
        "km (Kilometer)": 0.000000001,
        "hm (Hectometer)": 0.00000001,
        "dam (Dekameter)": 0.0000001,
        "m (Meter)": 0.000001,
        "dm (Decimeter)": 0.00001,
        "cm (Centimeter)": 0.0001,
        "mm (Milimeter)": 0.001,
        "um (Micrometer)": 1,
        "nm (Nanometer)": 1000
    },
    "nm (Nanometer)": {
        "Tm (Terameter)": 0.000000000000000000001,
        "Gm (Gigameter)": 0.000000000000000001,
        "Mm (Megameter)": 0.000000000000001,
        "km (Kilometer)": 0.000000000001,
        "hm (Hectometer)": 0.00000000001,
        "dam (Dekameter)": 0.0000000001,
        "m (Meter)": 0.000000001,
        "dm (Decimeter)": 0.00000001,
        "cm (Centimeter)": 0.0000001,
        "mm (Milimeter)": 0.000001,
        "um (Micrometer)": 0.001,
        "nm (Nanometer)": 1
    }
}
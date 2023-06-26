power_values = [
    "Megawatts (MW)",
    "Kilowatts (kW)",
    "Watts (W)",
    "Miliwatts (mW)",
    "Microwatts (µW)"
]

power_conversions = {
    "Megawatts (MW)": {
        "Megawatts (MW)": 1,
        "Kilowatts (kW)": 1000,
        "Watts (W)": 1000000,
        "Miliwatts (mW)": 1000000000,
        "Microwatts (µW)": 1000000000000
    },
    "Kilowatts (kW)": {
        "Megawatts (MW)": 0.001,
        "Kilowatts (kW)": 1,
        "Watts (W)": 1000,
        "Miliwatts (mW)": 1000000,
        "Microwatts (µW)": 1000000000
    },
    "Watts (W)": {
        "Megawatts (MW)": 0.000001,
        "Kilowatts (kW)": 0.001,
        "Watts (W)": 1,
        "Miliwatts (mW)": 1000,
        "Microwatts (µW)": 1000000
    },
    "Miliwatts (mW)": {
        "Megawatts (MW)": 0.000000001,
        "Kilowatts (kW)": 0.000001,
        "Watts (W)": 0.001,
        "Miliwatts (mW)": 1,
        "Microwatts (µW)": 1000
    },
    "Microwatts (µW)": {
        "Megawatts (MW)": 0.000000000001,
        "Kilowatts (kW)": 0.000000001,
        "Watts (W)": 0.000001,
        "Miliwatts (mW)": 0.001,
        "Microwatts (µW)": 1
    },
}
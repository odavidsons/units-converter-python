"""
Author: David Santos
Repository: https://github.com/odavidsons/units-converter-python
Year: 2023

Dictionary for mass conversions
"""
mass_values = [
    "Kt (Kilotonne)",
    "t (Tonne)",
    "kg (Kilogram)",
    "hg (Hectogram)",
    "dag (Dekagram)",
    "g (Gram)",
    "dg (Decigram)",
    "cg (Centigram)",
    "mg (Miligram)",
    "?g (Microgram)",
    "ng (Nanogram)"
]

mass_conversions = {
    "Kt (Kilotonne)": {
        "Kt (Kilotonne)": 1,
        "t (Tonne)": 100,
        "kg (Kilogram)": 100000,
        "hg (Hectogram)": 1000000,
        "dag (Dekagram)": 10000000,
        "g (Gram)": 100000000,
        "dg (Decigram)": 1000000000,
        "cg (Centigram)": 10000000000,
        "mg (Miligram)": 100000000000,
        "?g (Microgram)": 100000000000000,
        "ng (Nanogram)": 100000000000000000
    },
    "t (Tonne)": {
        "Kt (Kilotonne)": 0.100,
        "t (Tonne)": 1,
        "kg (Kilogram)": 1000,
        "hg (Hectogram)": 10000,
        "dag (Dekagram)": 100000,
        "g (Gram)": 1000000,
        "dg (Decigram)": 10000000,
        "cg (Centigram)": 100000000,
        "mg (Miligram)": 1000000000,
        "?g (Microgram)": 1000000000000,
        "ng (Nanogram)": 1000000000000000
    },
    "kg (Kilogram)": {
        "Kt (Kilotonne)": 0.100000,
        "t (Tonne)": 0.100,
        "kg (Kilogram)": 1,
        "hg (Hectogram)": 10,
        "dag (Dekagram)": 100,
        "g (Gram)": 1000,
        "dg (Decigram)": 10000,
        "cg (Centigram)": 100000,
        "mg (Miligram)": 1000000,
        "?g (Microgram)": 1000000000,
        "ng (Nanogram)": 1000000000000
    },
    "hg (Hectogram)": {
        "Kt (Kilotonne)": 0.1000000,
        "t (Tonne)": 0.1000,
        "kg (Kilogram)": 0.1,
        "hg (Hectogram)": 1,
        "dag (Dekagram)": 10,
        "g (Gram)": 100,
        "dg (Decigram)": 1000,
        "cg (Centigram)": 10000,
        "mg (Miligram)": 100000,
        "?g (Microgram)": 100000000,
        "ng (Nanogram)": 100000000000
    },
    "dag (Dekagram)": {
        "Kt (Kilotonne)": 0.10000000,
        "t (Tonne)": 0.10000,
        "kg (Kilogram)": 0.10,
        "hg (Hectogram)": 0.1,
        "dag (Dekagram)": 1,
        "g (Gram)": 10,
        "dg (Decigram)": 100,
        "cg (Centigram)": 1000,
        "mg (Miligram)": 10000,
        "?g (Microgram)": 10000000,
        "ng (Nanogram)": 10000000000
    },
    "g (Gram)": {
        "Kt (Kilotonne)": 0.100000000,
        "t (Tonne)": 0.100000,
        "kg (Kilogram)": 0.100,
        "hg (Hectogram)": 0.10,
        "dag (Dekagram)": 0.1,
        "g (Gram)": 1,
        "dg (Decigram)": 10,
        "cg (Centigram)": 100,
        "mg (Miligram)": 1000,
        "?g (Microgram)": 1000000,
        "ng (Nanogram)": 1000000000
    },
    "dg (Decigram)": {
        "Kt (Kilotonne)": 0.1000000000,
        "t (Tonne)": 0.1000000,
        "kg (Kilogram)": 0.1000,
        "hg (Hectogram)": 0.100,
        "dag (Dekagram)": 0.10,
        "g (Gram)": 0.1,
        "dg (Decigram)": 1,
        "cg (Centigram)": 10,
        "mg (Miligram)": 100,
        "?g (Microgram)": 100000,
        "ng (Nanogram)": 100000000
    },
    "cg (Centigram)": {
        "Kt (Kilotonne)": 0.10000000000,
        "t (Tonne)": 0.10000000,
        "kg (Kilogram)": 0.10000,
        "hg (Hectogram)": 0.1000,
        "dag (Dekagram)": 0.100,
        "g (Gram)": 0.10,
        "dg (Decigram)": 0.1,
        "cg (Centigram)": 1,
        "mg (Miligram)": 10,
        "?g (Microgram)": 10000,
        "ng (Nanogram)": 10000000
    },
    "mg (Miligram)": {
        "Kt (Kilotonne)": 0.100000000000,
        "t (Tonne)": 0.100000000,
        "kg (Kilogram)": 0.100000,
        "hg (Hectogram)": 0.10000,
        "dag (Dekagram)": 0.1000,
        "g (Gram)": 0.100,
        "dg (Decigram)": 0.10,
        "cg (Centigram)": 0.1,
        "mg (Miligram)": 1,
        "?g (Microgram)": 1000,
        "ng (Nanogram)": 1000000
    },
    "?g (Microgram)": {
        "Kt (Kilotonne)": 0.10000000000000,
        "t (Tonne)": 0.10000000000,
        "kg (Kilogram)": 0.10000000,
        "hg (Hectogram)": 0.1000000,
        "dag (Dekagram)": 0.100000,
        "g (Gram)": 0.10000,
        "dg (Decigram)": 0.1000,
        "cg (Centigram)": 0.100,
        "mg (Miligram)": 0.10,
        "?g (Microgram)": 1,
        "ng (Nanogram)": 1000
    },
    "ng (Nanogram)": {
        "Kt (Kilotonne)": 0.10000000000000000,
        "t (Tonne)": 0.10000000000000,
        "kg (Kilogram)": 0.10000000000,
        "hg (Hectogram)": 0.1000000000,
        "dag (Dekagram)": 0.100000000,
        "g (Gram)": 0.10000000,
        "dg (Decigram)": 0.1000000,
        "cg (Centigram)": 0.100000,
        "mg (Miligram)": 0.10000,
        "?g (Microgram)": 0.10,
        "ng (Nanogram)": 1
    }
}
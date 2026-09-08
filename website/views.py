from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@views.route('/main', methods=['GET', 'POST'])
def main():
    element_data = None

    if request.method == 'POST':
        period_number_input = request.form.get('period_number')
        group_number_input = request.form.get('group_number')

        period_number = None
        group_number = None

        # Validate Period Number
        try:
            period_number = int(period_number_input)
            if not (1 <= period_number <= 7):
                flash('Please enter a number between 1 and 7 in the period number.', category='error')
                period_number = None
        except (ValueError, TypeError):
            flash('Inputted period must be a valid number.', category='error')

        # Validate Group Number
        try:
            group_number = int(group_number_input)
            if not (1 <= group_number <= 6):
                flash('Please enter a number between 1 and 6 in the group number.', category='error')
                group_number = None
        except (ValueError, TypeError):
            flash('Inputted group must be a valid number.', category='error')

        # Perform lookup only if both inputs are valid
        if period_number is not None and group_number is not None:
            element_symbol = element_positions.get((period_number, group_number))

            if element_symbol is None:
                flash(
                    'There is no element in that period and group combination within Groups 1–6.',
                    category='error'
                )
            else:
                element_data = elements.get(element_symbol)

    return render_template("main.html", element_data=element_data)

# ELEMENT DATA STRUCTURES
# ============================================================
# ELEMENT LOOKUP TABLE
# Key = (period, group)
# Value = element symbol
# ============================================================

element_positions = {
    # Group 1
    (1, 1): "H",
    (2, 1): "Li",
    (3, 1): "Na",
    (4, 1): "K",
    (5, 1): "Rb",
    (6, 1): "Cs",
    (7, 1): "Fr",

    # Group 2
    (2, 2): "Be",
    (3, 2): "Mg",
    (4, 2): "Ca",
    (5, 2): "Sr",
    (6, 2): "Ba",
    (7, 2): "Ra",

    # Group 3
    (4, 3): "Sc",
    (5, 3): "Y",
    (6, 3): "La",
    (7, 3): "Ac",

    # Group 4
    (4, 4): "Ti",
    (5, 4): "Zr",
    (6, 4): "Hf",
    (7, 4): "Rf",

    # Group 5
    (4, 5): "V",
    (5, 5): "Nb",
    (6, 5): "Ta",
    (7, 5): "Db",

    # Group 6
    (4, 6): "Cr",
    (5, 6): "Mo",
    (6, 6): "W",
    (7, 6): "Sg",
}

elements = {
    "H": {
        "name": "Hydrogen",
        "symbol": "H",
        "atomic_number": 1,
        "atomic_mass": 1.008,
        "common_uses": "The common uses for Hydrogen are Fuel Cells, Rocket Fuel, Ammonia Production, Hydrogenation of Fats and Oils, Metal Production and Refining",
        "electron_configuration": "1s1",
        "ionization_energy": 1312,
        "electron_affinity": 72.8,
        "atomic_radius": 53
    },
    "Li": {
        "name": "Lithium",
        "symbol": "Li",
        "atomic_number": 3,
        "atomic_mass": 6.94,
        "common_uses": "The common uses for Lithium are Batteries, Ceramics and Glass, Lubricating Greases, Air Treatment, Pharmaceuticals",
        "electron_configuration": "[He] 2s1",
        "ionization_energy": 520,
        "electron_affinity": 59.6,
        "atomic_radius": 167
    },
    "Na": {
        "name": "Sodium",
        "symbol": "Na",
        "atomic_number": 11,
        "atomic_mass": 22.990,
        "common_uses": "The common uses for Sodium are Food Additive, Chemical Manufacturing, Water Treatment, and Pharmaceuticals",
        "electron_configuration": "[Ne] 3s1",
        "ionization_energy": 496,
        "electron_affinity": 52.9,
        "atomic_radius": 190
    },
    "K": {
        "name": "Potassium",
        "symbol": "K",
        "atomic_number": 19,
        "atomic_mass": 39.098,
        "common_uses": "The common uses for Potassium are Fertilizers, Food Additive, and Pharmaceuticals",
        "electron_configuration": "[Ar] 4s1",
        "ionization_energy": 419,
        "electron_affinity": 48.4,
        "atomic_radius": 243
    },
    "Rb": {
        "name": "Rubidium",
        "symbol": "Rb",
        "atomic_number": 37,
        "atomic_mass": 85.468,
        "common_uses": "The common uses for Rubidium are Atomic Clocks, Research, and Medical Applications",
        "electron_configuration": "[Kr] 5s1",
        "ionization_energy": 403,
        "electron_affinity": 46.9,
        "atomic_radius": 265
    },
    "Cs": {
        "name": "Cesium",
        "symbol": "Cs",
        "atomic_number": 55,
        "atomic_mass": 132.905,
        "common_uses": "The common uses for Cesium are Atomic Clocks, Photoelectric Cells, and Medical Applications",
        "electron_configuration": "[Xe] 6s1",
        "ionization_energy": 376,
        "electron_affinity": 45.5,
        "atomic_radius": 298
    },
    "Fr": {
        "name": "Francium",
        "symbol": "Fr",
        "atomic_number": 87,
        "atomic_mass": 223,
        "common_uses": "The common uses for Francium are primarily in research and medical applications",
        "electron_configuration": "[Rn] 7s1",
        "ionization_energy": 380,
        "electron_affinity": 44,
        "atomic_radius": 348
    },

    "Be": {
        "name": "Beryllium",
        "symbol": "Be",
        "atomic_number": 4,
        "atomic_mass": 9.012,
        "common_uses": "The common uses for Beryllium are Aerospace Applications, Nuclear Reactors, and Electronics",
        "electron_configuration": "[He] 2s2",
        "ionization_energy": 900,
        "electron_affinity": 0,
        "atomic_radius": 112
    },
    "Mg": {
        "name": "Magnesium",
        "symbol": "Mg",
        "atomic_number": 12,
        "atomic_mass": 24.305,
        "common_uses": "The common uses for Magnesium are Aerospace Applications, Fireworks, and Pharmaceuticals",
        "electron_configuration": "[Ne] 3s2",
        "ionization_energy": 738,
        "electron_affinity": 0,
        "atomic_radius": 160
    },
    "Ca": {
        "name": "Calcium",
        "symbol": "Ca",
        "atomic_number": 20,
        "atomic_mass": 40.078,
        "common_uses": "The common uses for Calcium are Bone Health, Food Additive, and Construction Materials",
        "electron_configuration": "[Ar] 4s2",
        "ionization_energy": 590,
        "electron_affinity": 2.37,
        "atomic_radius": 197
    },
    "Sr": {
        "name": "Strontium",
        "symbol": "Sr",
        "atomic_number": 38,
        "atomic_mass": 87.62,
        "common_uses": "The common uses for Strontium are Fireworks, Incandescent Lamps, and Medical Applications",
        "electron_configuration": "[Kr] 5s2",
        "ionization_energy": 550,
        "electron_affinity": 5.03,
        "atomic_radius": 215
    },
    "Ba": {
        "name": "Barium",
        "symbol": "Ba",
        "atomic_number": 56,
        "atomic_mass": 137.327,
        "common_uses": "The common uses for Barium are Medical Imaging, Electronics, and Chemical Manufacturing",
        "electron_configuration": "[Xe] 6s2",
        "ionization_energy": 503,
        "electron_affinity": 13.95,
        "atomic_radius": 222
    },
    "Ra": {
        "name": "Radium",
        "symbol": "Ra",
        "atomic_number": 88,
        "atomic_mass": 226,
        "common_uses": "The common uses for Radium are primarily in research and medical applications",
        "electron_configuration": "[Rn] 7s2",
        "ionization_energy": 509,
        "electron_affinity": 9.65,
        "atomic_radius": 283
    },
    "Sc": {
        "name": "Scandium",
        "symbol": "Sc",
        "atomic_number": 21,
        "atomic_mass": 44.956,
        "common_uses": "The common uses for Scandium are 3D Printing With Scalmalloy, Solid Oxide Fuel Cells, Nuclear Medicine and Cancer Imaging, Sporting Goods, Semiconductors and Electronics",
        "electron_configuration": "[Ar] 3d1 4s2",
        "ionization_energy": 633,
        "electron_affinity": 18.1,
        "atomic_radius": 162
    },
    "Y": {
        "name": "Yttrium",
        "symbol": "Y",
        "atomic_number": 39,
        "atomic_mass": 88.906,
        "common_uses": "The common uses for Yttrium are LED Phosphors, Cancer Radiotherapy, Solid Oxide Fuel Cells, Nd:YAG Lasers, Microwave and Radar, Water Purification",
        "electron_configuration": "[Kr] 4d1 5s2",
        "ionization_energy": 600,
        "electron_affinity": 29.6,
        "atomic_radius": 180
    },
    "La": {
        "name": "Lanthanum",
        "symbol": "La",
        "atomic_number": 57,
        "atomic_mass": 138.905,
        "common_uses": "The common uses for Lanthanum are Batteries and Fuel Cells, Optical Glass, Catalysts, Carbon Arc Lamps",
        "electron_configuration": "[Xe] 5d1 6s2",
        "ionization_energy": 538,
        "electron_affinity": 48,
        "atomic_radius": 187
    },
    "Ac": {
        "name": "Actinium",
        "symbol": "Ac",
        "atomic_number": 89,
        "atomic_mass": 227,
        "common_uses": "The common uses for Actinium are (Prostate) Cancer Treatment, Thermoelectric generators, Radio Immunotherapy, Nuclear Medicine (Used to remove tumors)",
        "electron_configuration": "[Rn] 6d1 7s2",
        "ionization_energy": 499,
        "electron_affinity": 33.8,
        "atomic_radius": 195
    },

    "Ti": {
        "name": "Titanium",
        "symbol": "Ti",
        "atomic_number": 22,
        "atomic_mass": 47.867,
        "common_uses": "The common uses for Titanium are Engine parts, Heat exchangers, Reactors, Storage tanks, Jewelry, Sports Equipment",
        "electron_configuration": "[Ar] 3d2 4s2",
        "ionization_energy": 659,
        "electron_affinity": 7.6,
        "atomic_radius": 147
    },
    "Zr": {
        "name": "Zirconium",
        "symbol": "Zr",
        "atomic_number": 40,
        "atomic_mass": 91.224,
        "common_uses": "The common uses for Zirconium are Plastic and Polymer Production, Dental Implants, Nuclear Reactors, Ceramics and Refractories (Ceramic Knives), Surgical Instruments",
        "electron_configuration": "[Kr] 4d2 5s2",
        "ionization_energy": 640,
        "electron_affinity": 41.1,
        "atomic_radius": 160
    },
    "Hf": {
        "name": "Hafnium",
        "symbol": "Hf",
        "atomic_number": 72,
        "atomic_mass": 178.49,
        "common_uses": "The common uses for Hafnium are Computer Chips and Transistors, Nuclear Reactor Control Rods, Jet Engines and Superalloys, Plasma Cutting Torches, Optical Coatings, Plastic and Polymer Production",
        "electron_configuration": "[Xe] 4f14 5d2 6s2",
        "ionization_energy": 659,
        "electron_affinity": 17,
        "atomic_radius": 159
    },
    "Rf": {
        "name": "Rutherfordium",
        "symbol": "Rf",
        "atomic_number": 104,
        "atomic_mass": 267,
        "common_uses": "The common uses for Rutherfordium are mostly in studies like; (Nuclear Physics, heavier Metals, Behaviour of oter metals)",
        "electron_configuration": "[Rn] 5f14 6d2 7s2",
        "ionization_energy": 579,
        "electron_affinity": 0,
        "atomic_radius": 150
    },
    "V": {
        "name": "Vanadium",
        "symbol": "V",
        "atomic_number": 23,
        "atomic_mass": 50.942,
        "common_uses": "The common uses for Vanadium are strengthens steel, adds color to glass/ceramics/tiles, helps store wind and solar energy for electrical power grid, heat-resistant parts for jet engines and spacecraft.",
        "electron_configuration": "[Ar] 3d3 4s2",
        "ionization_energy": 651,
        "electron_affinity": 50.6,
        "atomic_radius": 134
    },
    "Nb": {
        "name": "Niobium",
        "symbol": "Nb",
        "atomic_number": 41,
        "atomic_mass": 92.906,
        "common_uses": "The common uses for Niobium are oil and gas pipelines, bridges, and structural girders. used in automotive industry,  used in rocket nozzles and hypersonic systems.",
        "electron_configuration": "[Kr] 4d4 5s1",
        "ionization_energy": 652,
        "electron_affinity": 86.1,
        "atomic_radius": 146
    },
    "Ta": {
        "name": "Tantalum",
        "symbol": "Ta",
        "atomic_number": 73,
        "atomic_mass": 180.948,
        "common_uses": "The common uses for Tantalum are smartphones, laptops, automotive systems, and digital cameras. is also used in hip replacements, cranial plates, pacemakers, and surgical mesh.",
        "electron_configuration": "[Xe] 4f14 5d3 6s2",
        "ionization_energy": 761,
        "electron_affinity": 31,
        "atomic_radius": 146
    },
    "Db": {
        "name": "Dubnium",
        "symbol": "Db",
        "atomic_number": 105,
        "atomic_mass": 268,
        "common_uses": "Dubnium is used in scientific research.",
        "electron_configuration": "[Rn] 5f14 6d3 7s2",
        "ionization_energy": 665,
        "electron_affinity": 0,
        "atomic_radius": 139
    },
    "Cr": {
    "name": "Chromium",
    "symbol": "Cr",
    "atomic_number": 24,
    "atomic_mass": 51.996,
    "common_uses": "Chromium is used for shiny/chrome coatings on car parts, gives objects a shiny, protective surface, used to produce various industrial chemicals.",
    "electron_configuration": "[Ar] 3d5 4s1",
    "ionization_energy": 653,
    "electron_affinity": 64.3,
    "atomic_radius": 128
    },
    "Mo": {
        "name": "Molybdenum",
        "symbol": "Mo",
        "atomic_number": 42,
        "atomic_mass": 95.95,
        "common_uses": "Molybdenum is used in some electrical components, used where materials need to withstand very high heat, used as a catalyst in some chemical processes.",
        "electron_configuration": "[Kr] 4d5 5s1",
        "ionization_energy": 684,
        "electron_affinity": 72.1,
        "atomic_radius": 139
    },
    "W": {
        "name": "Tungsten",
        "symbol": "W",
        "atomic_number": 74,
        "atomic_mass": 183.84,
        "common_uses": "Tungsten withstands very high temperatures, used to make very hard tools, used for heavy equipment where high strength and heat resistance are needed.",
        "electron_configuration": "[Xe] 4f14 5d4 6s2",
        "ionization_energy": 770,
        "electron_affinity": 78.6,
        "atomic_radius": 139
    },
    "Sg": {
        "name": "Seaborgium",
        "symbol": "Sg",
        "atomic_number": 106,
        "atomic_mass": 269,
        "common_uses": "Seaborgium is mainly used to study superheavy elements, used in very small amounts because it is highly radioactive and short-lived.",
        "electron_configuration": "[Rn] 5f14 6d4 7s2",
        "ionization_energy": 757,
        "electron_affinity": 0,
        "atomic_radius": 132
    },
}

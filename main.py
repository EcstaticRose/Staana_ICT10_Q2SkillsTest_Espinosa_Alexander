from pyscript import display, document

# Non-metal elements: "Symbol": ("Name", Atomic Number, Atomic Mass)
placeholder = {
    "H":  ("Hydrogen",   1,   1.008),
    "He": ("Helium",     2,   4.0026),
    "C":  ("Carbon",     6,   12.011),
    "N":  ("Nitrogen",   7,   14.007),
    "O":  ("Oxygen",     8,   15.999),
    "F":  ("Fluorine",   9,   18.998),
    "Ne": ("Neon",       10,  20.180),
    "P":  ("Phosphorus", 15,  30.974),
    "S":  ("Sulfur",     16,  32.06),
    "Cl": ("Chlorine",   17,  35.45),
    "Ar": ("Argon",      18,  39.948),
    "Se": ("Selenium",   34,  78.971),
    "Br": ("Bromine",    35,  79.904),
    "Kr": ("Krypton",    36,  83.798),
    "I":  ("Iodine",     53,  126.90),
    "Xe": ("Xenon",      54,  131.29),
    "Rn": ("Radon",      86,  222.0),
    "At": ("Astatine",   85,  210.0),
}

def element_checker(e):
    result_div = document.getElementById('result')
    result_div.innerHTML = ""

    element = document.getElementById('element_name').value.strip().title()

    if not element:
        result_div.innerHTML = '<p class="text-danger fw-bold">Please enter an element symbol.</p>'
        return

    result = placeholder.get(element, ("Element not found", "-", "-"))

    if result[0] == "Element not found":
        result_div.innerHTML = f'<p class="text-danger fw-bold">"{element}" is not found in the non-metals list.</p>'
    else:
        result_div.innerHTML = f"""
        <b>Symbol:</b> {element}<br>
        <b>Element:</b> {result[0]}<br>
        <b>Atomic Number:</b> {result[1]}<br>
        <b>Atomic Mass:</b> {result[2]}<br>
        """
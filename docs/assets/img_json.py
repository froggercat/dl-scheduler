import os
import json
from itertools import compress
from collections import ChainMap

current_path = os.path.dirname(os.path.abspath(__file__))
imgs = [i for i in os.listdir(current_path) if not ".py" in i]
elements = {
    "fire": ["blazing", "scalding", "agni", "volcanic", "steel"],
    "water": ["poseidon", "frost", "greedy"],
    "wind": ["zephyr", "gust", "catoblepas", "phantom"],
    "light": ["amber", "lambent", "proud", "jeanne", "wandering"],
    "shadow": ["ebon", "obsidian", "violet", "nidhogg", "raging", "twilight"]
}

outputs = []
for img in imgs:
    key = "dragon" if "void" in img else img.split("_")[-1].split(".png")[0]
    title = " ".join([i.split(".png")[0].title() for i in img.split("_") if not any(c.isdigit() for c in i)])
    double_drop_path = f"../assets/{img}" if "2x" in img else None
    single_drop_path = f"../assets/{img}" if not "2x" in img else None
    element = list(compress(
        elements.keys(), 
        [True if any(True for b in elements[i] if b in img) else False for i in elements.keys()]))[0]
    
    existing_outputs = [i for i in outputs if i["key"] == key]
    if not existing_outputs:
        outputs.append({"key": key, "data":[]})
    
    output = [i for i in outputs if i["key"] == key][0]["data"]

    print(output)

    existing_element = [i for i in output if "element" in i.keys() and i["element"] == element] if output else None
    if not existing_element:
        elt = {}
        elt["title"] = title
        elt["element"] = element
        elt["images"] = {}
        output.append(elt)

    elt = [i for i in output if "element" in i.keys() and i["element"] == element][0]

    print(elt)

    if double_drop_path:
        elt["images"]["2x"] = double_drop_path
    if single_drop_path:
        elt["images"]["path"] = single_drop_path

with open("junk", "w") as f:
    f.writelines(json.dumps(outputs, indent=4, sort_keys=True))
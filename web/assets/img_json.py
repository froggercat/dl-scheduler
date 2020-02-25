import os
import pprint
import json

current_path = os.path.dirname(os.path.abspath(__file__))
imgs = [i for i in os.listdir(current_path) if not ".py" in i]
outputs = []
for img in imgs:
    output = {}
    output["2x"] = True if "2x" in img else False
    output["title"] = " ".join([i.split(".png")[0].title() for i in img.split("_") if not any(c.isdigit() for c in i)])
    output["path"] = f"../assets/{img}"
    outputs.append(output)

with open("junk", "w") as f:
    f.writelines(json.dumps(outputs))
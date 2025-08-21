import json
from openpharmacophore.io import pharmacophore_reader

# Load .ph4 file
ph4_file = "pharmacophore.ph4"
pharmacophore = pharmacophore_reader.read_ph4(ph4_file)

# Mapping MOE feature names to OpenPharmacophore feature types
feature_map = {
    "PiN": "positive charge",
    "Aro|Hyd": "aromatic ring",
    "Acc": "hb acceptor",
    "Acc2": "hb acceptor",
    "Don": "hb donor",
    "Don2": "hb donor",
    "Hyd": "hydrophobicity",
    "Aromatic": "aromatic ring",
    # add more if needed
}

points_data = []

for point in pharmacophore._points:
    # Get original feature name, fallback to name attribute
    orig_name = getattr(point, "feature_name", None) or getattr(point, "name", None)
    feat_type = feature_map.get(orig_name, orig_name).lower()

    # Extract center coordinates as plain floats
    center_coords = [point.center[i].magnitude for i in range(3)]

    # Extract radius as float
    radius_val = point.radius.magnitude

    # Try to get svector, else set default pointing along +z axis
    svector = getattr(point, "svector", None)
    if svector is None:
        svector = [1.0, 0.0, 0.0]  # <-- Default vector, e.g., along x axis, or change to [0,0,1]

    # If svector has magnitude attribute (quantity), convert to float, else keep as is
    def to_float(val):
        return val.magnitude if hasattr(val, "magnitude") else float(val)

    svector_dict = {
        "x": to_float(svector[0]),
        "y": to_float(svector[1]),
        "z": to_float(svector[2]),
    }

    point_dict = {
        "feat_type": feat_type,
        "center": center_coords,
        "radius": radius_val,
        "svector": svector_dict
    }

    points_data.append(point_dict)

output_json = {
    "points": points_data,
    "origin": [0.0, 0.0, 0.0]
}

with open("pharmacophore.json", "w") as f:
    json.dump(output_json, f, indent=4)



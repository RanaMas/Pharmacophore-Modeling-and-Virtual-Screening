import json
from rdkit import Chem
from rdkit.Chem import SDWriter
import openpharmacophore as oph
from openpharmacophore import puw

# Load your custom JSON
with open("pharmacophore.json") as f:
    data = json.load(f)

# Build PharmacophoricPoints manually from your format
points = []
for pt in data["points"]:
    center = puw.quantity(pt["center"], "angstroms")
    radius = puw.quantity(pt["radius"], "angstroms")

    sv = pt.get("svector", {"x": 0.0, "y": 0.0, "z": 1.0})

    # Create PharmacophoricPoint
    point = oph.PharmacophoricPoint(
        feat_type=pt["feat_type"],
        center=center,
        radius=radius,
    )

    # Add svector attribute to the point
    point.svector = puw.quantity([sv["x"], sv["y"], sv["z"]], "dimensionless")

    points.append(point)

# Create the pharmacophore object
pharmacophore = oph.Pharmacophore(points)

# Load molecules from SDF containing ZINC or ChHEMBL 3D molecules
supplier = Chem.SDMolSupplier("./3D_library.sdf", removeHs=False)
mols = [m for m in supplier if m is not None]

# Screening setup
hits = []
for mol in mols:
    ligand = oph.Ligand(mol)
    if pharmacophore.matches(ligand, max_dist=1.5):  # Adjust max_dist as needed
        hits.append(mol)

# Write hits to output SDF
with SDWriter("pharmacophore-hits.sdf") as writer:
    for hit in hits:
        writer.write(hit)

print("Screening complete. Hits saved to pharmacophore-hits.sdf")


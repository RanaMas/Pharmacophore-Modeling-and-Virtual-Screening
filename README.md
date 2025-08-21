# Pharmacophore-Modeling-and-Virtual-Screening

Huge drug 3D databases can be hard to store/screen on a local machine. In this repo, it's assumed that the work is done on an HPC terminal with OpenPharmacophore installed.

This is a pipeline that helps change the formatting pf a pharmacophore file from .ph4 to json and screen drug libraries like **ZINC**_lead_like and **CHEMBL**_2.5million databases.

File.ph4 is the pharamcophore file used by the Molecular Operating Environment software (MOE) while File.json is the format used by most softwares/modules like **OpenPharmacophore**.

In this repo, a code that changes the format from .ph4 to json is provided; in addition to a Python code for screening the libraries.

In addition, a script in bash is provided that allows you screen 3D libraries using several pharmacophores at once once submmitted as: **sbatch sreen.job**

**This repo assumes that you have already installed and compiled opharm_env where OpenPharmacophore is functional** and that you have downloaded the 3d libraries from ZINC20/22 or CHEMBL.

If you only have acces to a 2D library, 3D structures can be generated using the **Wash** algorithm in MOE.


**Post Pharmacophore Search**

In th effort of prioritizing your hits after the pharmacophore search, a code (stoplight.py) is provided that prioritizes the pharmacophore hits based on MW, logP, HBD, HBA, Rotatable bonds and TPSA according to Lipinski's Druglike Score (parameters are adjustable).

The stoplight analysis categorizes the molecules as Green/Yellow/Red. Each parameter is flagged and given a score of 2 (green), 1 (yellow) or 0 (red). Upon scanning, each feature in the molecule is indexed and the total score goes from 0 to 12 (6 features).


**N.B.** Molecules of highest priority score 12 if all 6 features were considered.

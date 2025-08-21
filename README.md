# Pharmacophore-Modeling-and-Virtual-Screening

Huge drug 3D databases can be hard to store/screen on a local machine. In this repo, it's assumed that the work is done on an HPC terminal with OpenPharmacophore installed.

This is a pipeline that helps change the formatting pf a pharmacophore file from .ph4 to json and screen drug libraries like **ZINC**_lead_like and **CHEMBL**_2.5million databases.

File.ph4 is the pharamcophore file used by the Molecular Operating Environment software (MOE) while File.json is the format used by most softwares/modules like **OpenPharmacophore**.

In this repo, a code that changes the format from .ph4 to json is provided; in addition to a Python code for screening the libraries.

In addition, a script in bash is provided that allows you screen 3D libraries using several pharmacophores at once once submmitted as: **sbatch sreen.job**

**This repo assumes that you have already installed and compiled opharm_env where OpenPharmacophore is functional** and that you have downloaded the 3d libraries from ZINC20/22 or CHEMBL.

If you only have acces to a 2D library, 3D structures can be generated using the **Wash** algorithm in MOE.

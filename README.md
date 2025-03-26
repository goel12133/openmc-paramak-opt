# OpenMC Tokamak Neutronics Simulation

This repository contains a full neutron transport simulation of a submersion-style tokamak fusion reactor using OpenMC. The geometry is generated with Paramak and the simulation includes custom materials, neutron source definition, and Tritium Breeding Ratio (TBR) calculation.

## Requirements
- Python 3.6+
- OpenMC
- Paramak
- openmc-data-downloader
- CAD-to-OpenMC converter
- Nuclear cross section data 

## Installation
```bash
git clone https://github.com/goel12133/openmc-paramak-opt.git
cd openmc-paramak-opt
pip install openmc paramak openmc-data-downloader

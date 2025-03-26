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
```

## Geometry Explanation

The simulation uses a **Submersion Tokamak** reactor geometry, created using the Paramak library. The reactor is defined by various radial thicknesses, coil placements, and other key parameters.

### Tokamak Geometry Parameters

| Parameter                            | Description                                      | Value  |
|--------------------------------------|--------------------------------------------------|--------|
| `inner_bore_radial_thickness`       | Radial thickness of the central bore            | 30 mm  |
| `inboard_tf_leg_radial_thickness`   | Thickness of the inboard toroidal field coil leg | 30 mm  |
| `center_column_shield_radial_thickness` | Thickness of the shielding around the center column | 30 mm  |
| `divertor_radial_thickness`         | Radial thickness of the divertor                | 80 mm  |
| `inner_plasma_gap_radial_thickness` | Gap between the plasma and center column        | 50 mm  |
| `plasma_radial_thickness`           | Radial thickness of the plasma                  | 200 mm |
| `outer_plasma_gap_radial_thickness` | Gap between the plasma and first wall           | 50 mm  |
| `firstwall_radial_thickness`        | Thickness of the first wall                     | 30 mm  |
| `blanket_rear_wall_radial_thickness` | Thickness of the blanket rear wall              | 30 mm  |
| `number_of_tf_coils`                | Number of toroidal field coils                  | 16     |
| `rotation_angle`                     | Rotation angle of the reactor geometry          | 360°   |
| `support_radial_thickness`          | Radial thickness of structural supports         | 90 mm  |

The toroidal and poloidal field coils are positioned strategically to ensure optimal plasma confinement. The reactor includes a vacuum boundary at a radius of **10 m**.

---

## Neutron Source Explanation

A **fixed neutron source** is defined using a Muir energy distribution to simulate **fusion-generated neutrons**. The source has the following properties:

### Neutron Source Parameters

| Parameter       | Description                                         | Value        |
|----------------|-----------------------------------------------------|-------------|
| `radius`       | Radial position of neutron emission                 | 293 mm      |
| `z_values`     | Vertical position of neutron emission               | 0 mm        |
| `angle`        | Angular distribution of emitted neutrons            | 0° to 90°   |
| `energy`       | Muir distribution peak energy                       | 14.1 MeV    |
| `m_rat`        | Mass ratio for energy distribution                   | 5.0         |
| `kt`          | Thermal spread of neutron energy distribution        | 20 keV      |

The neutron source is **isotropic** and **cylindrically distributed**, ensuring an even spread of fusion neutrons. These neutrons interact with the reactor components, and their behavior is analyzed using OpenMC tallies.

## Customizing

### Breeder Material Change

The breeder material in a fusion reactor is critical for neutron absorption and the production of tritium. In this model, the breeder material is initially set to **Li17Pb83**, a common lithium-lead alloy that is used for its ability to absorb neutrons and breed tritium. 

To customize the breeder material in this model, you can modify the material properties 



```python
mat_blanket = openmc.Material(name="blanket")
mat_blanket.add_elements_from_formula("Li4SiO4")  # New breeder material formula
mat_blanket.set_density("g/cm3", 2.0)  # Adjusted density for Li4SiO4
```

## Outputs

| Output               | Description                                                   |
|----------------------|---------------------------------------------------------------|
| `TBR tally`         | Tritium Breeding Ratio tally from neutron interactions        |
| `Neutron transport` | Simulation of neutron behavior and interactions in the tokamak |
| `Particle tracks`   | Monte Carlo tracking of neutron paths                         |
| `Energy deposition` | Heat deposition from neutron interactions                     |
| `Material reactions`| Nuclear reactions within materials (e.g., (n,Xt) reactions)  |


## License
[MIT License](https://opensource.org/licenses/MIT) © 2024 goel12133

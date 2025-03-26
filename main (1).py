
import math
import openmc
import openmc_data_downloader

import paramak
my_reactor = paramak.SubmersionTokamak(
   inner_bore_radial_thickness=30,
   inboard_tf_leg_radial_thickness=30,
   center_column_shield_radial_thickness=30,
   divertor_radial_thickness=80,
   inner_plasma_gap_radial_thickness=50,
   plasma_radial_thickness=200,
   outer_plasma_gap_radial_thickness=50,
   firstwall_radial_thickness=30,
   blanket_rear_wall_radial_thickness=30,
   number_of_tf_coils=16,
   rotation_angle=360,
   support_radial_thickness=90,
   inboard_blanket_radial_thickness=30,
   outboard_blanket_radial_thickness=30,
   elongation=2.00,
   triangularity=0.50,
   pf_coil_case_thicknesses=[10, 10, 10, 10],
   pf_coil_radial_thicknesses=[20, 50, 50, 20],
   pf_coil_vertical_thicknesses=[20, 50, 50, 20],
   pf_coil_radial_position=[500, 550, 550, 500],
   pf_coil_vertical_position=[270, 100, -100, -270],
   rear_blanket_to_tf_gap=50,
   outboard_tf_coil_radial_thickness=30,
   outboard_tf_coil_poloidal_thickness=30,
)
cadquery_object = my_reactor.solid

mat_blanket = openmc.Material(name="blanket")
mat_blanket.add_elements_from_formula("Li17Pb83")
mat_blanket.set_density("g/cm3", 15)


mat_plasma = openmc.Material(name="plasma")
mat_plasma.add_element("H", 1, "ao")
mat_plasma.add_nuclide("H3", 0.05, "ao")
mat_plasma.add_nuclide("H2", 0.95, "ao")
mat_plasma.set_density("g/cm3", 0.00001)

mat_pf_coil_1 = openmc.Material(name="pf_coil_1")
mat_pf_coil_1.add_elements_from_formula("NbTi")
mat_pf_coil_1.set_density("g/cm3", 8.94)


mat_pf_coil_2 = openmc.Material(name="pf_coil_2")
mat_pf_coil_2.add_elements_from_formula("NbTi")
mat_pf_coil_2.set_density("g/cm3", 8.94)


mat_pf_coil_3 = openmc.Material(name="pf_coil_3")
mat_pf_coil_3.add_elements_from_formula("NbTi")
mat_pf_coil_3.set_density("g/cm3", 8.94)


mat_pf_coil_4 = openmc.Material(name="pf_coil_4")
mat_pf_coil_4.add_elements_from_formula("NbTi")
mat_pf_coil_4.set_density("g/cm3", 8.94)


mat_pf_coil_case_1 = openmc.Material(name="pf_coil_case_1")
mat_pf_coil_case_1.add_element('Fe', 0.68)  # Iron
mat_pf_coil_case_1.add_element('Cr', 0.16)  # Chromium
mat_pf_coil_case_1.add_element('Ni', 0.10)  # Nickel
mat_pf_coil_case_1.add_element('Mo', 0.03)  # Molybdenum
mat_pf_coil_case_1.add_element('Mn', 0.02)  # Manganese
mat_pf_coil_case_1.add_element('Si', 0.01)  # Silicon
mat_pf_coil_case_1.set_density("g/cm3", 8.94)


mat_pf_coil_case_2 = openmc.Material(name="pf_coil_case_2")
mat_pf_coil_case_2.add_element('Fe', 0.68)  # Iron
mat_pf_coil_case_2.add_element('Cr', 0.16)  # Chromium
mat_pf_coil_case_2.add_element('Ni', 0.10)  # Nickel
mat_pf_coil_case_2.add_element('Mo', 0.03)  # Molybdenum
mat_pf_coil_case_2.add_element('Mn', 0.02)  # Manganese
mat_pf_coil_case_2.add_element('Si', 0.01)  # Silicon
mat_pf_coil_case_2.set_density("g/cm3", 8.94)


mat_pf_coil_case_3 = openmc.Material(name="pf_coil_case_3")
mat_pf_coil_case_3.add_element('Fe', 0.68)  # Iron
mat_pf_coil_case_3.add_element('Cr', 0.16)  # Chromium
mat_pf_coil_case_3.add_element('Ni', 0.10)  # Nickel
mat_pf_coil_case_3.add_element('Mo', 0.03)  # Molybdenum
mat_pf_coil_case_3.add_element('Mn', 0.02)  # Manganese
mat_pf_coil_case_3.add_element('Si', 0.01)  # Silicon
mat_pf_coil_case_3.set_density("g/cm3", 8.94)


mat_pf_coil_case_4 = openmc.Material(name="pf_coil_case_4")
mat_pf_coil_case_4.add_element('Fe', 0.68)  # Iron
mat_pf_coil_case_4.add_element('Cr', 0.16)  # Chromium
mat_pf_coil_case_4.add_element('Ni', 0.10)  # Nickel
mat_pf_coil_case_4.add_element('Mo', 0.03)  # Molybdenum
mat_pf_coil_case_4.add_element('Mn', 0.02)  # Manganese
mat_pf_coil_case_4.add_element('Si', 0.01)  # Silicon
mat_pf_coil_case_4.set_density("g/cm3", 8.94)

mat_outboard_firstwall = openmc.Material(name="outboard_firstwall")
mat_outboard_firstwall.add_element("W", 1, "ao")
mat_outboard_firstwall.set_density("g/cm3", 7.5)

mat_center_column_shield = openmc.Material(name="center_column_shield")
mat_center_column_shield.add_element("W", 1, "ao")
mat_center_column_shield.set_density("g/cm3", 19.3)

mat_divertor_upper = openmc.Material(name="divertor_upper")
mat_divertor_upper.add_element("W", 1, "ao")
mat_divertor_upper.set_density("g/cm3", 19.3)

mat_divertor_lower = openmc.Material(name="divertor_lower")
mat_divertor_lower.add_element("W", 1, "ao")
mat_divertor_lower.set_density("g/cm3", 19.3)

mat_supports = openmc.Material(name="supports")
mat_supports.add_element("Ti", 1, "ao")
mat_supports.set_density("g/cm3", 7.5)

mat_outboard_rear_blanket_wall = openmc.Material(name="outboard_rear_blanket_wall")
mat_outboard_rear_blanket_wall.add_element("Be", 1)
mat_outboard_rear_blanket_wall.set_density("g/cm3", 7.5)

mat_inboard_tf_coils = openmc.Material(name="inboard_tf_coils")
mat_inboard_tf_coils.add_elements_from_formula("Nb3Sn")
mat_inboard_tf_coils.set_density("g/cm3", 8)


mat_tf_coils = openmc.Material(name="tf_coils")
mat_tf_coils.add_elements_from_formula("Nb3Sn")
mat_tf_coils.set_density("g/cm3", 8)



all_my_mat = openmc.Materials(
    [
        mat_pf_coil_1,
        mat_pf_coil_2,
        mat_pf_coil_3,
        mat_pf_coil_4,
        mat_pf_coil_case_1,
        mat_pf_coil_case_2,
        mat_pf_coil_case_3,
        mat_pf_coil_case_4,
        mat_plasma,
        mat_center_column_shield,
        mat_outboard_firstwall,
        mat_blanket,
        mat_divertor_upper,
        mat_divertor_lower,
        mat_supports,
        mat_outboard_rear_blanket_wall,
        mat_inboard_tf_coils,
        mat_tf_coils,
    ]
)

print(all_my_mat)



all_my_mat.download_cross_section_data(
        libraries=["ENDFB-8.0-NNDC"],
        set_OPENMC_CROSS_SECTIONS=True,
        particles=["neutron"],
    )


dag_univ = openmc.DAGMCUniverse("dagmc12133.h5m")


vac_surf = openmc.Sphere(r=10000, surface_id=9999, boundary_type="vacuum")
region = -vac_surf
containing_cell = openmc.Cell(cell_id=9999, region=region, fill=dag_univ)
geometry = openmc.Geometry(root=[containing_cell])

my_source = openmc.Source()

radius = openmc.stats.Discrete([293.], [1])

z_values = openmc.stats.Discrete([0], [1])

angle = openmc.stats.Uniform(a=0., b=math.radians(90))

my_source.space = openmc.stats.CylindricalIndependent(r=radius, phi=angle, z=z_values, origin=(0.0, 0.0, 0.0))

my_source.angle = openmc.stats.Isotropic()

my_source.energy = openmc.stats.muir(e0=14100000, m_rat=5.0, kt=20000.0)


settings = openmc.Settings()
settings.batches = 10
settings.particles = 5000
settings.inactive = 0
settings.run_mode = "fixed source"
settings.source = my_source

tbr_cell_tally = openmc.Tally(name="tbr")
tbr_cell_tally.scores = ["(n,Xt)"]


tallies = openmc.Tallies([tbr_cell_tally])

my_model = openmc.Model(
    materials=all_my_mat, geometry=geometry, settings=settings, tallies=tallies
)

my_model.run()





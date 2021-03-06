# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='CO2_root',
    task_id='CO2',
    output_dir='out',
)
model.msh.read_file('CO2.msh')
model.gli.read_file('CO2.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TEMPERATURE_UNIT='KELVIN',
)
model.rfd.read_file('CO2.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 20000000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 318.15],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='CARBON1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 100000.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 318.15],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    PRIMARY_VARIABLE='CARBON1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 1.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.35],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 2.7e-11],
    MASS_DISPERSION=[1, 1, 0.1],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2650],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 750],
        ['CONDUCTIVITY:'],
        [1, 3.5],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    COMPONENTS=[1, 'CARBON1'],
    EOS_TYPE='VTPR',
    COMPRESSIBILITY=[
        [15],
        [1, 0],
        [1, 0],
    ],
    JTC='OFF',
    DENSITY=15,
    VISCOSITY=15,
    SPECIFIC_HEAT_CAPACITY=15,
    HEAT_CONDUCTIVITY=15,
    ISOTHERM=[1, 0, 0],
    DECAY=[1, 0, 0],
    DIFFUSION=[1, 1e-06],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    ELE_MASS_LUMPING=1,
    LINEAR_SOLVER=[2, 1, 1e-15, 2000, 1, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 50, 1],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    TIME_STEPS=[10, 6],
    TIME_END=60,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='MULTI_COMPONENTIAL_FLOW',
    NOD_VALUES='PRESSURE1',
    MFP_VALUES=[
        ['DENSITY1'],
        ['VISCOSITY1'],
        ['SPESIFIC_HEAT_CAPACITY1'],
        ['HEAT_CONDUCTIVITY1'],
    ],
    GEO_TYPE=['POLYLINE', 'OUT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()

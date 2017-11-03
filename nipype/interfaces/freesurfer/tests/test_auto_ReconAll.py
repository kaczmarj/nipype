# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import ReconAll


def test_ReconAll_inputs():
    input_map = dict(T1_files=dict(argstr='-i %s...',
    ),
    T2_file=dict(argstr='-T2 %s',
    min_ver='5.3.0',
    ),
    args=dict(argstr='%s',
    ),
    big_ventricles=dict(argstr='-bigventricles',
    ),
    brainstem=dict(argstr='-brainstem-structures',
    ),
    directive=dict(argstr='-%s',
    position=0,
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    expert=dict(argstr='-expert %s',
    ),
    flags=dict(argstr='%s',
    ),
    hemi=dict(argstr='-hemi %s',
    ),
    hippocampal_subfields_T1=dict(argstr='-hippocampal-subfields-T1',
    min_ver='6.0.0',
    ),
    hippocampal_subfields_T2=dict(argstr='-hippocampal-subfields-T2 %s %s',
    min_ver='6.0.0',
    ),
    hires=dict(argstr='-hires',
    min_ver='6.0.0',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    mprage=dict(argstr='-mprage',
    ),
    mri_aparc2aseg=dict(xor=['expert'],
    ),
    mri_ca_label=dict(xor=['expert'],
    ),
    mri_ca_normalize=dict(xor=['expert'],
    ),
    mri_ca_register=dict(xor=['expert'],
    ),
    mri_edit_wm_with_aseg=dict(xor=['expert'],
    ),
    mri_em_register=dict(xor=['expert'],
    ),
    mri_fill=dict(xor=['expert'],
    ),
    mri_mask=dict(xor=['expert'],
    ),
    mri_normalize=dict(xor=['expert'],
    ),
    mri_pretess=dict(xor=['expert'],
    ),
    mri_remove_neck=dict(xor=['expert'],
    ),
    mri_segment=dict(xor=['expert'],
    ),
    mri_segstats=dict(xor=['expert'],
    ),
    mri_tessellate=dict(xor=['expert'],
    ),
    mri_watershed=dict(xor=['expert'],
    ),
    mris_anatomical_stats=dict(xor=['expert'],
    ),
    mris_ca_label=dict(xor=['expert'],
    ),
    mris_fix_topology=dict(xor=['expert'],
    ),
    mris_inflate=dict(xor=['expert'],
    ),
    mris_make_surfaces=dict(xor=['expert'],
    ),
    mris_register=dict(xor=['expert'],
    ),
    mris_smooth=dict(xor=['expert'],
    ),
    mris_sphere=dict(xor=['expert'],
    ),
    mris_surf2vol=dict(xor=['expert'],
    ),
    mrisp_paint=dict(xor=['expert'],
    ),
    openmp=dict(argstr='-openmp %d',
    ),
    parallel=dict(argstr='-parallel',
    ),
    subject_id=dict(argstr='-subjid %s',
    usedefault=True,
    ),
    subjects_dir=dict(argstr='-sd %s',
    genfile=True,
    hash_files=False,
    ),
    talairach=dict(xor=['expert'],
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    use_T2=dict(argstr='-T2pial',
    min_ver='5.3.0',
    ),
    xopts=dict(argstr='-xopts-%s',
    ),
    )
    inputs = ReconAll.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ReconAll_outputs():
    output_map = dict(BA_stats=dict(altkey='BA',
    loc='stats',
    ),
    T1=dict(loc='mri',
    ),
    annot=dict(altkey='*annot',
    loc='label',
    ),
    aparc_a2009s_stats=dict(altkey='aparc.a2009s',
    loc='stats',
    ),
    aparc_aseg=dict(altkey='aparc*aseg',
    loc='mri',
    ),
    aparc_stats=dict(altkey='aparc',
    loc='stats',
    ),
    area_pial=dict(altkey='area.pial',
    loc='surf',
    ),
    aseg=dict(loc='mri',
    ),
    aseg_stats=dict(altkey='aseg',
    loc='stats',
    ),
    avg_curv=dict(loc='surf',
    ),
    brain=dict(loc='mri',
    ),
    brainmask=dict(loc='mri',
    ),
    curv=dict(loc='surf',
    ),
    curv_pial=dict(altkey='curv.pial',
    loc='surf',
    ),
    curv_stats=dict(altkey='curv',
    loc='stats',
    ),
    entorhinal_exvivo_stats=dict(altkey='entorhinal_exvivo',
    loc='stats',
    ),
    filled=dict(loc='mri',
    ),
    graymid=dict(altkey=['graymid', 'midthickness'],
    loc='surf',
    ),
    inflated=dict(loc='surf',
    ),
    jacobian_white=dict(loc='surf',
    ),
    label=dict(altkey='*label',
    loc='label',
    ),
    norm=dict(loc='mri',
    ),
    nu=dict(loc='mri',
    ),
    orig=dict(loc='mri',
    ),
    pial=dict(loc='surf',
    ),
    rawavg=dict(loc='mri',
    ),
    ribbon=dict(altkey='*ribbon',
    loc='mri',
    ),
    smoothwm=dict(loc='surf',
    ),
    sphere=dict(loc='surf',
    ),
    sphere_reg=dict(altkey='sphere.reg',
    loc='surf',
    ),
    subject_id=dict(),
    subjects_dir=dict(),
    sulc=dict(loc='surf',
    ),
    thickness=dict(loc='surf',
    ),
    volume=dict(loc='surf',
    ),
    white=dict(loc='surf',
    ),
    wm=dict(loc='mri',
    ),
    wmparc=dict(loc='mri',
    ),
    wmparc_stats=dict(altkey='wmparc',
    loc='stats',
    ),
    )
    outputs = ReconAll.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

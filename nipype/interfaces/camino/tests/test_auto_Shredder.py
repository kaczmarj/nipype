# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..convert import Shredder


def test_Shredder_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    chunksize=dict(argstr='%d',
    position=2,
    units='NA',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='< %s',
    mandatory=True,
    position=-2,
    ),
    offset=dict(argstr='%d',
    position=1,
    units='NA',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    space=dict(argstr='%d',
    position=3,
    units='NA',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = Shredder.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Shredder_outputs():
    output_map = dict(shredded=dict(),
    )
    outputs = Shredder.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

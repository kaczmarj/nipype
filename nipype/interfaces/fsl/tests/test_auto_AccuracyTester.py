# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..fix import AccuracyTester


def test_AccuracyTester_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    mel_icas=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=3,
    ),
    output_directory=dict(argstr='%s',
    mandatory=True,
    position=2,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    trained_wts_file=dict(argstr='%s',
    mandatory=True,
    position=1,
    ),
    )
    inputs = AccuracyTester.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_AccuracyTester_outputs():
    output_map = dict(output_directory=dict(argstr='%s',
    position=1,
    ),
    )
    outputs = AccuracyTester.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

#!/usr/bin/env python3


def test1():
    from count_matched_spectra import main

    result = main(
        argv=[
            "-s",
            "data/XLpeplib_Beveridge_QEx-HFX_DSS_R1.mgf",
            "-m",
            "data/masses.txt",
        ]
    )
    assert len(result) == 7
    assert 215 in result.values()
    assert 741 in result.values()
    assert 137 in result.values()
    assert 1295 in result.values()
    assert 364 in result.values()
    assert 133 in result.values()
    assert 189 in result.values()

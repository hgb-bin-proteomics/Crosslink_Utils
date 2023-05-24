#!/usr/bin/env python3

# CROSSLINK UTILS - TESTS
# 2022 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

##### tests for find_shortest.py #####

def test_find_shortest1():

    from find_shortest import find_shortest

    shortest = find_shortest("pyXlinkViewer_export.csv", [["C", "D"]])
    shorest["ConstraintSatisfied"] = shortest["CA distance"].apply(lambda x: float(x) <= 27.0)

    assert shortest.shape[0] == 17 and shortest[shortest["ConstraintSatisfied"]].shape[0] == 9

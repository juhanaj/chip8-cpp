#!/usr/bin/env python


# // 4xkk SNE Vx, byte
# // Skip next instruction if Vx != kk

import re
import os
import json

from util import run_asm

def test_se_byte():
    asm = """
        LD V0, #1
        SNE V0, #0
        LD V0, #2
        EXIT
    """
    emulator_debug = run_asm(asm)
    assert emulator_debug.get("V0") == 1


def test_sne_register():
    asm = """
        LD V0, #1
        LD V1, #1
        LD V3, #1
        SE V0, V1
        LD V3, #2
        EXIT
    """
    emulator_debug = run_asm(asm)
    assert emulator_debug.get("V3") == 1

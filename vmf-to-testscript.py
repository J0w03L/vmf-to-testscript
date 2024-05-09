"""
    VMF to TestScript for Xbox 360
    -------------------------------------------
    https://github.com/J0w03L/vmf-to-testscript
    https://j0w03l.me
    -------------------------------------------
"""

VERSION = "v0.0.0"

import sys

sys.path.insert(0, "./src/PyVMF/src")
sys.path.insert(0, "./src/")

from vmfconvert import *

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog        = "vmf-to-testscript.py",
        description = "Tool to convert a VMF into a TestScript for modding on the Xbox 360.",
        epilog      = f"Version {VERSION}"
    )
    parser.add_argument(
        "-i", "--input",
        help     = "Path of the .vmf file to convert.",
        required = True
    )
    parser.add_argument(
        "-s", "--start-id",
        help    = "hammerid to begin at (default: 703100).",
        default = 703100
    )
    parser.add_argument(
        "-o", "--output",
        help    = "Path to write the .vtest to.",
        required = True
    )
    args = parser.parse_args()
    
    TestScript(args.input, args.output, int(args.start_id))

# VMF to TestScript
A simple Python script that parses a .vmf file and generates a .vtest file from it's entities.
This tool is intended to help speed up the process of creating testscripts for The Orange Box on the Xbox 360.

## How to use
1. `git clone https://github.com/J0w03L/vmf-to-testscript.git --recursive`
2. `cd vmf-to-testscript`
3. `python3 vmf-to-testscript -h` (this will show you a help page)

**Note that the intended way to use this tool is to set everything up in the map you're running the script on's decompiled VMF, and then copy all of the entities you created into a new VMF, making sure to use "Paste Special" so that entity positions are preserved. You should then use the new VMF as the input file with this tool.**

## Notes
This is currently not a very optimized way to create a testscript. This tool will blindly copy all entity properties into the testscript, regardless of if they're valid on the 360 or not!
Additionally, this tool does not make any attempts to save space.
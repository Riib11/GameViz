import sys
from subprocess import call
from gameviz.parsing.parser import parse
from gameviz.compiling.compiler import compile

for filename in sys.argv[1:]:
    with open(filename,"r+") as file:
        filename_root = filename[:filename.index(".gdot")]
        lines = [line for line in file]
        # parse
        graph = parse(lines)
        # compile
        compiled = compile(graph)
        # write
        filename_new = filename_root + ".dot"
        with open(filename_new, "w+") as file_new:
            file_new.write(compiled)
        # dot image
        call(["dot","-Tpng", "-o"+filename_root+".png", filename_new])


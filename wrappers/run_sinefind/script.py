######################################
# wrapper for rule: run_sinefind
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_sinefind \n##\n")
f.write("## Run SINE Finder\n")
f.close()

OUTPUT = os.path.splitext(os.path.basename(snakemake.input.seq))[0] + "-matches.fasta"

command = "cd " + os.path.join("annotation_TE",snakemake.params.genome) + " ; " +\
          "sine_finder -V " + os.path.basename(snakemake.input.seq)

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

command = "cd " + os.path.join("annotation_TE",snakemake.params.genome) + " ; " +\
          "mv " + OUTPUT + " " + snakemake.params.folder + "/"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

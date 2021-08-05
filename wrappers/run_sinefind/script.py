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

FASTA = "../" + os.path.basename(snakemake.input.seq)

command = "cd " + os.path.join("annotation_TE" + snakemake.params.genome + snakemake.params.folder) + " ; " +\
          "sine_finder -V " + FASTA

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

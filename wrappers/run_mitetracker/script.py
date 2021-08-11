######################################
# wrapper for rule: run_mitetracker
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_mitetracker \n##\n")
f.write("## Run MiteTracker\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)

command = "cd annotation_TE/" + snakemake.params.genome + "/mitetracker ; " +\
          "mkdir -p results ; " + \
          "mitetracker -g " + FASTA + " " +\
          "-j job -w 3"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

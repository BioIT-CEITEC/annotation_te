######################################
# wrapper for rule: run_mitetracker_rc
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_mitetracker_rc \n##\n")
f.write("## Run MiteTracker\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq_rc)

command = "cd annotation_TE" + snakemake.params.genome + "/mitetracker_rc ; " +\
          "mkdir -p results ; " + \
          "mitetracker -g " + FASTA + " " +\
          "-j job -w 3"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

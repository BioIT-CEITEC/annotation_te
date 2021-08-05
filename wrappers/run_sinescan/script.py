######################################
# wrapper for rule: run_sinescan
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_sinescan \n##\n")
f.write("## Run SINE Scan\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)

command = "cd " + os.path.join("annotation_TE", snakemake.params.genome, "sinescan") + " ; " +\
          "mkdir result ; mkdir output ; mkdir final ; " +\
          "sinescan -s 123 -g " + FASTA + " -o output -d result -z final"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

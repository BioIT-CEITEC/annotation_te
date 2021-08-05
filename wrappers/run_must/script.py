######################################
# wrapper for rule: run_must
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_must \n##\n")
f.write("## Run MUSTv2\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)

command = "cd annotation_TE" + snakemake.params.genome + "/must ; " +\
          "mkdir temp ; " + \
          "mustv2 " + FASTA + " " +\
          "result.txt temp"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

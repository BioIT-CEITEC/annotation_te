######################################
# wrapper for rule: run_mitefind
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_mitefind \n##\n")
f.write("## Run miteFinderII\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)

command = "cd annotation_TE" + snakemake.params.genome + "/mitefind ; " +\
          "miteFinderII -input " + FASTA + " " +\
          "-output result.txt"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

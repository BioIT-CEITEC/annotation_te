######################################
# wrapper for rule: run_mitefind_rc
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_mitefind_rc \n##\n")
f.write("## Run miteFinderII\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq_rc)

command = "cd annotation_TE" + snakemake.params.genome + "/mitefind_rc ; " +\
          "miteFinderII -input " + FASTA + " " +\
          "-output result.txt"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

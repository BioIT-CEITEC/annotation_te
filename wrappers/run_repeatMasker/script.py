######################################
# wrapper for rule: run_repeatMasker
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_repeatMasker \n##\n")
f.write("## Run RepeatMasker\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)

command = "cd annotation_TE" + snakemake.params.genome + "/repMasker ; " +\
          "ln -s " + FASTA + " " +\
          "RepeatMasker -pa " + snakemake.threads + " " +\
          "-lib " + snakemake.params.ref + " " + os.path.basename(snakemake.input.seq)

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

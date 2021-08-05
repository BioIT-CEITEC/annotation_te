######################################
# wrapper for rule: createProject
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: createProject \n##\n")
f.write("## Run Reasonate createProject \n")
f.close()

command = "mkdir -p annotation_TE ; " +\
          "reasonaTE -mode createProject -projectFolder annotation_TE " +\
          "-projectName " + snakemake.params.genome + " " +\
          "-inputFasta " + snakemake.input.fasta

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

######################################
# wrapper for rule: run_transposonPSI
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_transposonPSI \n##\n")
f.write("## Run transposonPSI\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)

command = "cd " + os.path.join("annotation_TE", snakemake.params.genome, "transposonPSI") + " ; " +\
          "mkdir -p temp ; mkdir -p result ; "

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

command = "cd " + os.path.join("annotation_TE", snakemake.params.genome, "transposonPSI") + " ; " +\
          "transposonPSI -fastaFile " + FASTA + " " +\
          "-resultFolder result -tempFolder temp -mode nuc"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

command = "cd " + os.path.join("annotation_TE", snakemake.params.genome, "transposonPSI") + " ; " +\
          "mv result/* ./"

shell(command)

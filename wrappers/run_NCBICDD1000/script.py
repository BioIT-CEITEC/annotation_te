######################################
# wrapper for rule: run_NCBICDD1000
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_NCBICDD1000 \n##\n")
f.write("## Run NCBICDD1000\n")
f.close()

command = "rpstblastn -query " + snakemake.input.seq + " " +\
    "-num_threads " + str(snakemake.threads) + " " + \
    "-db " + snakemake.params.dblibrary + " " +\
    "-outfmt '7 stitle evalue qstart qend' -evalue 0.01 " +\
    "-out " + snakemake.output.ncbicdd

# command = "cd annotation_TE" + snakemake.params.genome + "/NCBICDD1000 ; " +\
#           "mkdir temp ; " + \
#           "proteinNCBICDD1000 -fastaFile " + FASTA + " " +\
#           "-resultFolder temp"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)


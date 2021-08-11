######################################
# wrapper for rule: run_ltrHarvest
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_ltrHarvest \n##\n")
f.write("## Run ltrHarvest\n")
f.write("## Create suffix array\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)
INDEX = os.path.basename(snakemake.input.seq) + ".index"

command = "cd annotation_TE/" + snakemake.params.genome + "/ltrHarvest ; " +\
          "gt suffixerator -db " + FASTA + " " +\
          "-indexname " + INDEX + " -tis -suf -lcp -des -ssp -sds -dna"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'a')
f.write("## Run ltrHarvest\n")
f.close()

command = "cd annotation_TE/" + snakemake.params.genome + "/ltrHarvest ; " +\
          "gt ltrharvest -index " + INDEX + " > result.txt"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

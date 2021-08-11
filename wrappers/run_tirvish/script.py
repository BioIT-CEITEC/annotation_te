######################################
# wrapper for rule: run_tirvish
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_tirvish \n##\n")
f.write("## Create suffix array\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)
INDEX = os.path.basename(snakemake.input.seq) + ".index"

command = "cd " + os.path.join("annotation_TE",snakemake.params.genome,snakemake.params.folder) + " ; " +\
          "gt suffixerator -db " + FASTA + " " +\
          "-indexname " + INDEX + " -tis -suf -lcp -des -ssp -sds -dna -mirrored"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'a')
f.write("## Run tirvish\n")
f.close()

command = "cd " + os.path.join("annotation_TE", snakemake.params.genome, snakemake.params.folder) + " ; " +\
          "gt tirvish -index " + INDEX + " > result.txt"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

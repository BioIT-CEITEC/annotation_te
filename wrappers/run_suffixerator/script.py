######################################
# wrapper for rule: run_suffixerator
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_suffixerator \n##\n")
f.write("## Run Suffixerator for tirvish\n")
f.close()

command = "gt suffixerator -db " + snakemake.input.fasta + " " +\
          "-indexname " + snakemake.output.index_mr + " " +\
          "-tis -suf -lcp -des -ssp -sds -dna -mirrored"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_suffixerator \n##\n")
f.write("## Run Suffixerator for tirvish_rc\n")
f.close()

command = "gt suffixerator -db " + snakemake.input.fasta_rc + " " +\
          "-indexname " + snakemake.output.index_rc_mr + " " +\
          "-tis -suf -lcp -des -ssp -sds -dna -mirrored"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_suffixerator \n##\n")
f.write("## Run Suffixerator for ltrharvest\n")
f.close()

command = "gt suffixerator -db " + snakemake.input.fasta + " " +\
          "-indexname " + snakemake.output.index + " " +\
          "-tis -suf -lcp -des -ssp -sds -dna"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)
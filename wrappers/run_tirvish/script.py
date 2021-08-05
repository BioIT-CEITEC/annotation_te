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
f.write("## Run tirvish\n")
f.close()

command = "gt tirvish -index " + snakemake.input.index_mr + " > " + snakemake.output.result_tir

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

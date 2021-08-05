######################################
# wrapper for rule: run_tirvish_rc
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_tirvish_rc \n##\n")
f.write("## Run tirvish_rc\n")
f.close()

command = "gt tirvish -index " + snakemake.input.index_mr_rc + " > " + snakemake.output.result_rc_tir

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

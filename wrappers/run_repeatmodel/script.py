######################################
# wrapper for rule: run_repeatmodel
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_repeatmodel \n##\n")
f.write("## Run RepeatModeler\n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)

command = "cd " + os.path.join("annotation_TE",snakemake.params.genome,"repeatmodel") + " ; " +\
          "cp " + FASTA + " " + os.path.basename(snakemake.input.seq) + " ; " +\
          "BuildDatabase -name sequence_index -engine ncbi " + os.path.basename(snakemake.input.seq) + " ; " +\
          "RepeatModeler -engine ncbi -database sequence_index -pa " + str(snakemake.threads)

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

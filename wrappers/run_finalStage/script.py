######################################
# wrapper for rule: finalStage
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: finalStage \n##\n")
f.write("## Run Reasonate checkAnnotations \n")
f.close()

command = "reasonaTE -mode checkAnnotations -projectFolder annotation_TE " +\
          "-projectName " + snakemake.params.genome + " &>> " + snakemake.log.run

f = open(snakemake.log.run, 'a')
f.write("\n## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'a')
f.write("## Run Reasonate parseAnnotations \n")
f.close()

command = "reasonaTE -mode parseAnnotations -projectFolder annotation_TE " +\
          "-projectName " + snakemake.params.genome

f = open(snakemake.log.run, 'a')
f.write("\n## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'a')
f.write("## Run Reasonate pipeline \n")
f.close()

command = "reasonaTE -mode pipeline -projectFolder annotation_TE " +\
          "-projectName " + snakemake.params.genome

f = open(snakemake.log.run, 'a')
f.write("\n## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'a')
f.write("## Run Reasonate statistics \n")
f.close()

command = "reasonaTE -mode statistics -projectFolder annotation_TE " +\
          "-projectName " + snakemake.params.genome

f = open(snakemake.log.run, 'a')
f.write("\n## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'a')
f.write("## Run Reasonate sequenceRenamer \n")
f.close()

command = "reasonaTE -mode sequenceRenamer -seqNames " + sequence_heads + " " +\
          "-inputGFF " + snakemake.output.inGFF + " " + \
          "-outputGFF " + snakemake.output.outGFF

f = open(snakemake.log.run, 'a')
f.write("\n## COMMAND: "+command+"\n")
f.close()
shell(command)

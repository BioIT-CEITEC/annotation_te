######################################
# wrapper for rule: run_helitronscanner
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: run_helitronscanner \n##\n")
f.write("## Run HelitronScanner \n")
f.write("## Run HelitronScanner - find helitron heads \n")
f.close()

FASTA = "../" + os.path.basename(snakemake.input.seq)

command = "cd annotation_TE" + snakemake.params.genome + "/helitronScanner ; " +\
          "helitronscanner scanHead -g " + FASTA + " " +\
          "-bs 0 -o scanHead.txt"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'a')
f.write("## Run HelitronScanner - find helitron tails \n")
f.close()

command = "cd annotation_TE" + snakemake.params.genome + "/helitronScanner ; " +\
          "helitronscanner scanTail -g " + FASTA + " " +\
          "-bs 0 -o scanTail.txt"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

f = open(snakemake.log.run, 'a')
f.write("## Run HelitronScanner - final results \n")
f.close()

command = "cd annotation_TE" + snakemake.params.genome + "/helitronScanner ; " +\
          "helitronscanner pairends -hs scanHead.txt" +\
          "-ts scanTail.txt " +\
          "-o " + snakemake.output.helitronscan

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)





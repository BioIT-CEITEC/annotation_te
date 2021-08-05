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
f.close()

command = "gt ltrharvest -index " + snakemake.input.index + " > " + snakemake.output.result_ltr

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

# f = open(snakemake.log.run, 'a')
# f.write("## Create LTR harvest output directory \n")
# f.close()
#
# command = "mkdir -p "+ snakemake.params.outinner
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#
# f = open(snakemake.log.run, 'a')
# f.write("## Run LTR harvest \n")
# f.close()
#
# command = "gt ltrharvest -index "+ snakemake.params.genome + " " +\
#           "-gff3 "+ snakemake.params.ltrharvest_gff3 + " " +\
#           "-motif tgca -minlenltr 100 -maxlenltr 7000 -mindistltr 1000 " +\
#           "-maxdistltr 20000 -similar 85 -motifmis 1 -mintsd 5 -xdrop 5 " +\
#           "-overlaps best -longoutput " +\
#           "-outinner "+ snakemake.params.outinner_fa + " " +\
#           "-out "+ snakemake.params.ltrharvest_fa + " " +\
#           "> "+ snakemake.params.ltrharvest_out
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#
# f = open(snakemake.log.run, 'a')
# f.write("## Sort LTR harvest GFF3 \n")
# f.close()
#
# command = "gt gff3 -sort "+ snakemake.params.ltrharvest_gff3 + " " +\
#           "> "+ snakemake.output.ltrharvest_sorted_gff3
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#
# f = open(snakemake.log.run, 'a')
# f.write("## Run LTR digest \n")
# f.close()
#
# command = "gt -j "+ snakemake.params.CPU + " " +\
#           "ltrdigest -outfileprefix "+ snakemake.params.digest_prefix + " " +\
#           "-trnas "+ snakemake.params.eukaryotic-tRNAs + " " +\
#           "-hmms "+ snakemake.params.gydb_hmms + " " +\
#           "-- "+ snakemake.output.ltrharvest_sorted_gff3 + " " +\
#           snakemake.params.genome +" > "+ snakemake.output.ltrdigest_gff3
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#

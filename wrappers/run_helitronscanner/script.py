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
f.close()

command = "reasonaTE -mode annotate -projectFolder " + snakemake.params.reasonateFolder + " " + \
          " -projectName " + snakemake.params.reasonateProject + " " +\
          " -tool helitronScanner"

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

# ## will load each chromosome into memory, without splitting into 1Mb batches (-buffer_size option ==0)
#
#
# command = "helitronscanner scanHead -g "+ snakemake.input.genomefasta + " " +\
#           "-bs 0 -o "+ snakemake.params.scanHead
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#
# f = open(snakemake.log.run, 'a')
# f.write("## Run HelitronScanner - find helitron tails \n")
# f.close()
#
# command = "helitronscanner scanTail -g "+ snakemake.input.genomefasta + " " +\
#           "-bs 0 -o "+ snakemake.params.scanTail
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#
# f = open(snakemake.log.run, 'a')
# f.write("## Run HelitronScanner - final results \n")
# f.close()
#
# command = "helitronscanner pairends -hs "+ snakemake.params.scanHead +" "+\
#           "-ts "+ snakemake.params.scanTail +" "+\
#           "-o "+ snakemake.output.helitron
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#
# f = open(snakemake.log.run, 'a')
# f.write("## Run HelitronScanner reverse complement - find helitron heads \n")
# f.close()
#
# ## will load each chromosome into memory, without splitting into 1Mb batches (-buffer_size option ==0)
#
# command = "helitronscanner scanHead -g "+ snakemake.input.genomefasta + " " +\
#           "-bs 0 --rc -o "+ snakemake.params.scanHead_rc
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#
# f = open(snakemake.log.run, 'a')
# f.write("## Run HelitronScanner reverse complement - find helitron tails \n")
# f.close()
#
# command = "helitronscanner scanTail -g "+ snakemake.input.genomefasta + " " +\
#           "-bs 0 --rc -o "+ snakemake.params.scanTail_rc
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#
# f = open(snakemake.log.run, 'a')
# f.write("## Run HelitronScanner reverse complement - final results \n")
# f.close()
#
# command = "helitronscanner pairends -hs "+ snakemake.params.scanHead_rc +" "+\
#           "-ts "+ snakemake.params.scanTail_rc +" "+\
#           "-o "+ snakemake.output.helitron_rc
#
# f = open(snakemake.log.run, 'a')
# f.write("## COMMAND: "+command+"\n")
# f.close()
# shell(command)
#
#
# ## path to vsearch and silix for clustering
# SILIX = / home / mstitzer / software / bin / silix
# VSEARCH = / home / mstitzer / software / vsearch / bin / vsearch
#
#
# #########################
# ##   tab format output ##
# #########################
#
# python
# helitron_scanner_out_to_tabout.py ${GENOME}.HelitronScanner.draw.hel.fa ${GENOME}.HelitronScanner.tabnames.fa > ${
#     GENOME}.HelitronScanner.tabout
#
# python
# helitron_scanner_out_to_tabout.py ${GENOME}.HelitronScanner.draw.rc.hel.fa ${GENOME}.HelitronScanner.tabnames.fa > ${
#     GENOME}.HelitronScanner.rc.tabout
#
# #########################
# ##  Make families      ##
# #########################
#
# ### think about whether this should be the entire element or the earlier classification based on the terminal 30bp of the helitron.
# ### remember that the mtec helitrons have lots of N's in their internal regions, so this decision may have been due to data quality.
#
# python
# get_last_30bp_fasta.py ${GENOME}.HelitronScanner.tabnames.fa > ${GENOME}.HelitronScanner.tabnames.terminal30bp.fa
#
# $VSEARCH - allpairs_global ${GENOME}.HelitronScanner.tabnames.terminal30bp.fa - blast6out ${
#                                                                                                GENOME}.terminal30bp.allvall.out - id
# 0.8 - query_cov
# 0.8 - target_cov
# 0.8 - -threads =$CPU
#
#
# ## command for clustering entire helitron length (too computationally expensive
# ##$VSEARCH -allpairs_global ${GENOME}.HelitronScanner.tabnames.fa -blast6out ${GENOME}.allvall.out -id 0.8 -query_cov 0.8 -target_cov 0.8 --threads=$CPU
#
# $SILIX ${GENOME}.HelitronScanner.tabnames.terminal30bp.fa ${GENOME}.terminal30bp.allvall.out - f
# DHH - i
# 0.8 - r
# 0.8 > ${GENOME}
# .8080.fnodes
#
# # also cluster with MTEC for naming consistency
# wget
# http: // maizetedb.org / ~maize / TE_12 - Feb - 2015_15 - 35.
# fa
# $VSEARCH - -usearch_global
# TE_12 - Feb - 2015_15 - 35.
# fa - db ${GENOME}.HelitronScanner.tabnames.fa - id
# 0.8 - query_cov
# 0.8 - target_cov
# 0.8 - blast6out ${GENOME}.TEDB
# .8080.searchglobal.toponly.out - strand
# both - top_hits_only - -threads $CPU
#





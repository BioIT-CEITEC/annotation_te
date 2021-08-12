######################################
# wrapper for rule: createProject
######################################
import os
import sys
import math
import subprocess
from snakemake.shell import shell

f = open(snakemake.log.run, 'w')
f.write("\n##\n## RULE: createProject \n##\n")
f.write("## Run Reasonate createProject \n")
f.close()

command = "mkdir -p annotation_TE ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + " ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/finalResults ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/ltrHarvest ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/mitefind_rc ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/must ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/repeatmodel ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/sinefind_rc ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/tirvish_rc ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/transposonCandC ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/transposonCandF ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/helitronScanner ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/ltrPred ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/mitetracker ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/NCBICDD1000 ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/repMasker ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/sinescan ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/transposonCandA ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/transposonCandD ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/transposonPSI ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/helitronScanner_rc ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/mitefind ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/mitetracker_rc ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/parsedAnnotations ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/sinefind ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/tirvish ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/transposonCandB ; " +\
          "mkdir -p annotation_TE/" + snakemake.params.genome + "/transposonCandE ; " +\
          "cp " + snakemake.input.fasta + " annotation_TE/" + snakemake.params.genome + "/sequence.fasta ; " +\
          "seqkit seq -rpv -t dna -o annotation_TE/" + snakemake.params.genome + "/sequence_rc.fasta " + snakemake.input.fasta

f = open(snakemake.log.run, 'a')
f.write("## COMMAND: "+command+"\n")
f.close()
shell(command)

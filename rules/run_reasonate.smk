## ANNOTATION of Transposable Elements
rule createProject:
    input:  fasta = config["genome_fasta"]
    output:  seq = "annotation_TE"+config["genome_name"]+"/sequence.fasta",
             seq_rc = "annotation_TE"+config["genome_name"]+"/sequence.fasta"
    params: genome = config["genome_name"]
    log: "logs/createProject.log"
    conda: "../wrappers/createProject/env.yaml"
    script: "../wrappers/createProject/script.py"

rule run_helitronscanner:
    input:  seq = "annotation_TE"+config["genome_name"]+"/sequence.fasta"
    output: helitronscan = "annotation_TE"+config["genome_name"]+"/helitronScanner/result.txt"
    params: genome=config["genome_name"]
    log: "logs/run_helitronscanner.log"
    conda: "../wrappers/run_helitronscanner/env.yaml"
    script: "../wrappers/run_helitronscanner/script.py"

rule run_helitronscanner_rc:
    input:  seq_rc = "annotation_TE"+config["genome_name"]+"/sequence_rc.fasta"
    output: helitronscan_rc = "annotation_TE" + config["genome_name"] + "/helitronScanner_rc/result.txt"
    params: genome = config["genome_name"]
    log: "logs/run_helitronscanner_rc.log"
    conda: "../wrappers/run_helitronscanner_rc/env.yaml"
    script: "../wrappers/run_helitronscanner_rc/script.py"

rule run_ltrHarvest:
    input: seq = "annotation_TE" + config["genome_name"] + "/sequence.fasta"
    output: ltrharvest = "annotation_TE" + config["genome_name"] + "/ltrHarvest/result.txt"
    params: genome = config["genome_name"]
    log: "logs/run_ltrHarvest.log"
    conda: "../wrappers/run_ltrHarvest/env.yaml"
    script: "../wrappers/run_ltrHarvest/script.py"

rule run_mitefind:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"
rule run_mitetracker:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"
rule run_must:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"
rule run_repeatmodel:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"
rule run_repMasker:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"
rule run_sinefind:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"
rule run_sinescan:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"
rule run_tirvish:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"
rule run_transposonPSI:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"
rule run_NCBICDD1000:
    input: seq="annotation_TE" + config["genome_name"] + "/sequence.fasta"

rule variant_annotation:
    input:  index_des = "annotate/sequence.index.des"
    output: annotated = "annotate/all_variants.annotated.tsv"
    log:    "logs/variant_annotation.log"
    threads: 20
    resources:
        mem_mb=8000
    params: ref = expand("{ref_dir}/seq/{ref_name}.fa",ref_dir = reference_directory,ref_name = config["reference"])[0],
            index = "",
            ref_name = config["reference"],
            organism_name = config["organism"],
            format = config["format_name"],
            not_use_merged = config["not_use_merged"],
            CADD_DB_SNVs = expand("{ref_dir}/annot/vep/CADD_scores_DB/whole_genome_SNVs.tsv.gz",ref_dir = reference_directory)[0],
            CADD_DB_indels = expand("{ref_dir}/annot/vep/CADD_scores_DB/gnomad.genomes.r3.0.indel.tsv.gz",ref_dir = reference_directory)[0],
            dir_plugins = expand("{ref_dir}/annot/vep/VEP_plugins",ref_dir = reference_directory)[0],
    conda:  "../wrappers/run_helitronscanner/env.yaml"
    script: "../wrappers/run_helitronscanner/script.py"

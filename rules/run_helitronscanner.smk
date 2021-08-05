## ANNOTATION of VARIANTS in SAMPLES
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

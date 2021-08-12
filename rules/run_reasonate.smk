## ANNOTATION of Transposable Elements
rule createProject:
    input:  fasta = config["genome_fasta"]
    output:  seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta"),
             seq_rc = os.path.join("annotation_TE",config["genome_name"],"sequence_rc.fasta"),
             heads = os.path.join("annotation_TE",config["genome_name"],"sequence_heads.txt")
    params: genome = config["genome_name"]
    log: run = "logs/createProject.log"
    conda: "../wrappers/createProject/env.yaml"
    script: "../wrappers/createProject/script.py"

rule run_helitronscanner:
    input:  seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: helitronscan = os.path.join("annotation_TE", config["genome_name"], "helitronScanner","result.txt")
    params: genome = config["genome_name"],
            folder = "helitronScanner"
    log: run = "logs/run_helitronscanner.log"
    conda: "../wrappers/run_helitronscanner/env.yaml"
    script: "../wrappers/run_helitronscanner/script.py"

rule run_helitronscanner_rc:
    input:  seq = os.path.join("annotation_TE",config["genome_name"],"sequence_rc.fasta")
    output: helitronscan = os.path.join("annotation_TE", config["genome_name"], "helitronScanner_rc","result.txt")
    params: genome = config["genome_name"],
            folder = "helitronScanner_rc"
    log: run = "logs/run_helitronscanner_rc.log"
    conda: "../wrappers/run_helitronscanner/env.yaml"
    script: "../wrappers/run_helitronscanner/script.py"

rule run_ltrHarvest:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: ltrharvest = os.path.join("annotation_TE", config["genome_name"], "ltrHarvest","result.txt")
    params: genome = config["genome_name"]
    log: run = "logs/run_ltrHarvest.log"
    conda: "../wrappers/run_ltrHarvest/env.yaml"
    script: "../wrappers/run_ltrHarvest/script.py"

rule run_mitefind:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: mitefind = os.path.join("annotation_TE", config["genome_name"], "mitefind","result.txt")
    params: genome = config["genome_name"],
            folder = "mitefind"
    log: run = "logs/run_mitefind.log"
    conda: "../wrappers/run_mitefind/env.yaml"
    script: "../wrappers/run_mitefind/script.py"

rule run_mitefind_rc:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence_rc.fasta")
    output: mitefind = os.path.join("annotation_TE", config["genome_name"], "mitefind_rc","result.txt")
    params: genome = config["genome_name"],
            folder= "mitefind_rc"
    log: run = "logs/run_mitefind_rc.log"
    conda: "../wrappers/run_mitefind/env.yaml"
    script: "../wrappers/run_mitefind/script.py"

rule run_mitetracker:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: mitetracker = os.path.join("annotation_TE", config["genome_name"], "mitetracker","results","job","all.gff3")
    params: genome = config["genome_name"],
            folder = "mitetracker"
    threads: 3
    log: run = "logs/run_mitetracker.log"
    conda: "../wrappers/run_mitetracker/env.yaml"
    script: "../wrappers/run_mitetracker/script.py"

rule run_mitetracker_rc:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence_rc.fasta")
    output: mitetracker = os.path.join("annotation_TE", config["genome_name"], "mitetracker_rc","results","job","all.gff3")
    params: genome = config["genome_name"],
            folder = "mitetracker_rc"
    threads: 3
    log: run = "logs/run_mitetracker_rc.log"
    conda: "../wrappers/run_mitetracker/env.yaml"
    script: "../wrappers/run_mitetracker/script.py"

rule run_must:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: must = os.path.join("annotation_TE", config["genome_name"], "must","result.txt")
    params: genome = config["genome_name"]
    threads: 10
    log: run = "logs/run_must.log"
    conda: "../wrappers/run_must/env.yaml"
    script: "../wrappers/run_must/script.py"

rule run_repeatmodel:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: repeatmodel = os.path.join("annotation_TE", config["genome_name"], "repeatmodel", "sequence_index-families.stk")
    params: genome = config["genome_name"]
    threads: 20
    log: run = "logs/run_repeatmodel.log"
    conda: "../wrappers/run_repeatmodel/env.yaml"
    script: "../wrappers/run_repeatmodel/script.py"

rule run_repMasker:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: repeatmasker = os.path.join("annotation_TE", config["genome_name"], "repMasker", "sequence.fasta.out")
    params: genome = config["genome_name"],
            ref = os.path.join(TE_db_path,config["reference"])
    threads: 20
    log: run = "logs/run_repeatMasker.log"
    conda: "../wrappers/run_repeatMasker/env.yaml"
    script: "../wrappers/run_repeatMasker/script.py"

rule run_sinefind:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: sinefind = os.path.join("annotation_TE",config["genome_name"],"sinefind","sequence-matches.fasta")
    params: genome = config["genome_name"],
            folder = "sinefind"
    log: run = "logs/run_sinefind.log"
    conda: "../wrappers/run_sinefind/env.yaml"
    script: "../wrappers/run_sinefind/script.py"

rule run_sinefind_rc:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence_rc.fasta")
    output: sinefind = os.path.join("annotation_TE",config["genome_name"],"sinefind_rc","sequence_rc-matches.fasta")
    params: genome = config["genome_name"],
            folder = "sinefind_rc"
    log: run = "logs/run_sinefind_rc.log"
    conda: "../wrappers/run_sinefind/env.yaml"
    script: "../wrappers/run_sinefind/script.py"

rule run_sinescan:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: sinescan = os.path.join("annotation_TE",config["genome_name"],"sinescan","result","sequence.sine.fa")
    params: genome = config["genome_name"]
    log: run = "logs/run_sinescan.log"
    conda: "../wrappers/run_sinescan/env.yaml"
    script: "../wrappers/run_sinescan/script.py"

rule run_tirvish:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: tirvish = os.path.join("annotation_TE", config["genome_name"], "tirvish", "result.txt")
    params: genome = config["genome_name"],
            folder = "tirvish"
    log: run = "logs/run_tirvish.log"
    conda: "../wrappers/run_tirvish/env.yaml"
    script: "../wrappers/run_tirvish/script.py"

rule run_tirvish_rc:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence_rc.fasta")
    output: tirvish = os.path.join("annotation_TE", config["genome_name"], "tirvish_rc", "result.txt")
    params: genome = config["genome_name"],
            folder = "tirvish_rc"
    log: run = "logs/run_tirvish_rc.log"
    conda: "../wrappers/run_tirvish/env.yaml"
    script: "../wrappers/run_tirvish/script.py"

rule run_transposonPSI:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta")
    output: transposonpsi = os.path.join("annotation_TE",config["genome_name"],"transposonPSI","sequence.fasta.TPSI.allHits")
    params: genome = config["genome_name"]
    log: run = "logs/run_transposonPSI.log"
    conda: "../wrappers/run_transposonPSI/env.yaml"
    script: "../wrappers/run_transposonPSI/script.py"

rule run_NCBICDD1000:
    input: seq = os.path.join("annotation_TE",config["genome_name"],"sequence.fasta"),
           dblib = expand(os.path.join(TE_db_path,"ncbicdd","Selection1000Library{libnum}.pn"),libnum=libnumber)
    output: ncbicdd = os.path.join("annotation_TE", config["genome_name"], "NCBICDD1000", "temp", "Result{libnum}.txt")
    params: genome = config["genome_name"],
            dblibrary = os.path.join(TE_db_path,"ncbicdd","Selection1000Library{libnum}")
    log: run = "logs/run_NCBICDD1000_{libnum}.log"
    threads: 10
    conda: "../wrappers/run_NCBICDD1000/env.yaml"
    script: "../wrappers/run_NCBICDD1000/script.py"

rule run_finalStage:
    input:  helitronscan = os.path.join("annotation_TE", config["genome_name"], "helitronScanner", "result.txt"),
            helitronscan_rc = os.path.join("annotation_TE", config["genome_name"], "helitronScanner_rc", "result.txt"),
            ltrharvest = os.path.join("annotation_TE", config["genome_name"], "ltrHarvest", "result.txt"),
            mitefind = os.path.join("annotation_TE", config["genome_name"], "mitefind", "result.txt"),
            mitefind_rc = os.path.join("annotation_TE", config["genome_name"],"mitefind_rc","result.txt"),
            mitetracker = os.path.join("annotation_TE", config["genome_name"], "mitetracker", "results", "job", "all.gff3"),
            mitetracker_rc = os.path.join("annotation_TE", config["genome_name"], "mitetracker_rc", "results", "job", "all.gff3"),
            must = os.path.join("annotation_TE", config["genome_name"], "must", "result.txt"),
            repeatmodel = os.path.join("annotation_TE", config["genome_name"], "repeatmodel", "sequence_index-families.stk"),
            repeatmasker = os.path.join("annotation_TE", config["genome_name"], "repMasker", "sequence.fasta.out"),
            sinefind = os.path.join("annotation_TE", config["genome_name"], "sinefind", "sequence-matches.fasta"),
            sinefind_rc = os.path.join("annotation_TE", config["genome_name"], "sinefind_rc", "sequence_rc-matches.fasta"),
            sinescan = os.path.join("annotation_TE", config["genome_name"], "sinescan", "result", "sequence.sine.fa"),
            tirvish = os.path.join("annotation_TE", config["genome_name"], "tirvish", "result.txt"),
            tirvish_rc = os.path.join("annotation_TE", config["genome_name"], "tirvish_rc", "result.txt"),
            transposonpsi = os.path.join("annotation_TE", config["genome_name"], "transposonPSI", "sequence.fasta.TPSI.allHits"),
            ncbicdd = expand(os.path.join("annotation_TE", config["genome_name"], "NCBICDD1000", "temp", "Result{libnum}.txt"), libnum=libnumber),
            heads= os.path.join("annotation_TE",config["genome_name"],"sequence_heads.txt")
    output: outGFF = os.path.join("annotation_TE", config["genome_name"], "finalResults", "FinalAnnotations_Transposons.gff3")
    params: genome = config["genome_name"]
    log:    run = "logs/run_finalStage.log"
    conda:  "../wrappers/run_finalStage/env.yaml"
    script: "../wrappers/run_finalStage/script.py"

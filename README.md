# illumina dragen
---

## somatic calling

- example command for somatic calling
```
dragen -f -r /staging/human/reference/hg19/hg19.fa.k_21.f_16.m_149.v6 --tumor-fastq1 ACRO2-121118_S96_R1_001.fastq.gz --tumor-fastq2 ACRO2-121118_S96_R3_001.fastq.gz --enable-variant-caller true --vc-sample-name ACR02-121118_S96 --output-directory ./322_vqsr_output_dir/ --output-file-prefix ACR02-121118_S96_322 --enable-vqsr true --vqsr-annotation SNP,DP,MQ,TLOD --vqsr-annotation INDEL,DP,MQ,TLOD --vqsr-resource "SNP,15.0,/staging/human/reference/hg19/gatk_bundle/hapmap_3.3.hg19.sites.vcf" --vqsr-resource "SNP,12.0,/staging/human/reference/hg19/gatk_bundle/1000G_omni2.5.hg19.sites.vcf" --vqsr-resource "SNP,10.0,/staging/human/reference/hg19/gatk_bundle/1000G_phase1.snps.high_confidence.hg19.sites.vcf" --vqsr-resource "INDEL,12.0,/staging/human/reference/hg19/gatk_bundle/Mills_and_1000G_gold_standard.indels.hg19.sites.vcf"
```

- 322 panel test location: /isilon/sjung_tmp/dragen/NextSeqOutput/181212_NS500399_0425_AHMFFJBGX7/Data/Intensities/BaseCalls
- previous batch script location: /isilon/dragen

- extract tumor and normal list
```
awk  -F ',' '{print $1,$4}' QIAseq-010219_T_N.csv |grep tumor |awk '{print $1}' > tumor_tmp.txt
awk  -F ',' '{print $1,$4}' QIAseq-010219_T_N.csv |grep normal |awk '{print $1}' > normal_tmp.txt
```

- run the main script
`nohup ./run_tumor_normal.sh > QIAseq-010219_T_N.log`

# illumina dragen
---

## somatic calling

- example command for somatic calling for one paired end sample
```
dragen -f -r /staging/human/reference/hg19/hg19.fa.k_21.f_16.m_149.v6 --tumor-fastq1 ACRO2-121118_S96_R1_001.fastq.gz --tumor-fastq2 ACRO2-121118_S96_R3_001.fastq.gz --enable-variant-caller true --vc-sample-name ACR02-121118_S96 --output-directory ./322_vqsr_output_dir/ --output-file-prefix ACR02-121118_S96_322
```

- example command for somatic calling with vqsr
```
dragen -f -r /staging/human/reference/hg19/hg19.fa.k_21.f_16.m_149.v6 --tumor-fastq1 ACRO2-121118_S96_R1_001.fastq.gz --tumor-fastq2 ACRO2-121118_S96_R3_001.fastq.gz --enable-variant-caller true --vc-sample-name ACR02-121118_S96 --output-directory ./322_vqsr_output_dir/ --output-file-prefix ACR02-121118_S96_322 --enable-vqsr true --vqsr-annotation SNP,DP,MQ,TLOD --vqsr-annotation INDEL,DP,MQ,TLOD --vqsr-resource "SNP,15.0,/staging/human/reference/hg19/gatk_bundle/hapmap_3.3.hg19.sites.vcf" --vqsr-resource "SNP,12.0,/staging/human/reference/hg19/gatk_bundle/1000G_omni2.5.hg19.sites.vcf" --vqsr-resource "SNP,10.0,/staging/human/reference/hg19/gatk_bundle/1000G_phase1.snps.high_confidence.hg19.sites.vcf" --vqsr-resource "INDEL,12.0,/staging/human/reference/hg19/gatk_bundle/Mills_and_1000G_gold_standard.indels.hg19.sites.vcf"
```

- example command for somatic calling with a list of fastq
```
dragen -f -r /staging/human/reference/hg19/hg19.fa.k_21.f_16.m_149.v6 --tumor-fastq-list ./config/T.csv --tumor-fastq-list-sample-id MOL18-163696_S77 --enable-variant-caller true --output-directory ./QIAseq-010219_T --output-file-prefix FOC-TMB.190103_NB501378_0348_AHFMJFBGX9.MOL18 --vc-target-bed /isilon/R_and_D/TMB-Dynamic_Range/322_solid_fastq/QIAseqDisc322-Disc-VAF-regions.bed
```

- 322 panel test location: /isilon/sjung_tmp/dragen/NextSeqOutput/181212_NS500399_0425_AHMFFJBGX7/Data/Intensities/BaseCalls
- previous batch script location: /isilon/dragen

- prepare a bed file
  - add chr
  - convert space to tab-delimited
  ```
  sed 's/^/chr/' file.in > file.out
  awk -v OFS="\t" '$1=$1' file.out > file2.out
  ```

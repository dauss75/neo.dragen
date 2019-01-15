#!/bin/sh

REF="/staging/human/reference/hg19/hg19.fa.k_21.f_16.m_149.v6"
BED="/isilon/sjung_tmp/dragen/FOC-TMB/190103_NB501378_0348_AHFMJFBGX9/QIAseq-010219_analysis/config/QIAseqDisc322-Disc-VAF-regions_chr_added.bed"
FASTQ="/isilon/R_and_D/FOC-TMB/190103_NB501378_0348_AHFMJFBGX9/FASTQs/"
OUTDIR="/isilon/sjung_tmp/dragen/FOC-TMB/190103_NB501378_0348_AHFMJFBGX9/QIAseq-010219_analysis/QIAseq-010219_T/"

SAMPLES="MOL18-163696_S77 MOL18-163711_S78 MOL18-163723_S79 MOL18-163727_S80 MOL18-163735_S81 MOL18-163738_S82 MOL18-163739_S83 MOL18-163742_S84 MOL18-163752_S85 MOL18-163757_S86 MOL18-163726_S87 MOL18-163732_S88 MOL18-163736_S89 MOL18-163779_S90 MOL18-163781_S91 MOL18-163783_S92 MOL18-163787_S93 MOL18-163790_S94 MOL18-163791_S95 MOL18-163792_S96"

for SAMPLE in $SAMPLES
do
 FINALOUT="$OUTDIR$SAMPLE"
 R1="$FASTQ${SAMPLE}_R1.fq.gz"
 R2="$FASTQ${SAMPLE}_R2.fq.gz"
 mkdir $FINALOUT

 echo "dragen -r $REF --tumor-fastq1 $R1 --tumor-fastq2 $R2 --enable-variant-caller true --vc-sample-name $SAMPLE --output-directory $FINALOUT  --output-file-prefix $SAMPLE --vc-target-bed $BED"

 dragen -r $REF --tumor-fastq1 $R1 --tumor-fastq2 $R2 --enable-variant-caller true --vc-sample-name $SAMPLE --output-directory $FINALOUT  --output-file-prefix $SAMPLE --vc-target-bed $BED

done

#!/usr/bin/python

import os
import os.path
from os import listdir
from os.path import isfile,join

all_samplesheet_path = "/hpc/dev/assay/NextSeqData/Validations/RNAFusions/Validation_Runs_Sequencing_Data_Only/dragen_csvs"
s3_dir = "s3://genoptix-dragen-evaluation/RNA_Fastq"

# Get list of samplesheets from the all samplesheet path
samplesheets = [f for f in listdir(all_samplesheet_path) if
        "SampleSheet" in f and isfile(join(all_samplesheet_path, f))]

def replace_last(source_string, replace_what, replace_with):
    """
    function to replace endline special characters '\r\n' 
    """
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail

for sheet in samplesheets:
    ss,flowcell_id_csv = sheet.split("-")
    flowcell_id,csv = flowcell_id_csv.split(".")
    #print flowcell_id
    with open(sheet) as fp:
        samplecount = 1

        # Also create flowcell level dragen csv file
        allcsv_filename = ["allsamples_dragen_", flowcell_id, ".csv"]
        allcsv_output = [all_samplesheet_path, "flowcell_level_csv", "".join(allcsv_filename)]
        allsamples_csv = open("/".join(allcsv_output),"w+")
        header = ["RGID","RGSM","RGLB","Lane","Read1File","Read2File\n"]
        allsamples_csv.write(",".join(header))


        for line in fp:
            line.strip()
            if line.startswith('Sample_ID'):
                fixedline = replace_last(line, '\r\n', '')
                header = fixedline
                #print("header: ", header)
            elif line.startswith('Sample'):
                # Create a dragen csv for each sample line
                fixedline = replace_last(line, '\r\n', '')
                linelength = len(line.split(","))
                if linelength == 10:
                    Sample_ID,Sample_Name,Sample_Plate,Sample_Well,I7_Index_ID,index,I5_Index_ID,index2,Sample_Project,Description = line.split(",")
                else: 
                    Sample_ID,Sample_Name,Sample_Plate,Sample_Well,I7_Index_ID,index,I5_Index_ID,index2,Sample_Project,Description,extra = line.split(",")
                
                filename = [Sample_Name, flowcell_id, "csv"]
                outputfile = (".").join(filename)
                pathcontents = [all_samplesheet_path, flowcell_id, outputfile]
                outputdir = ("/").join(pathcontents[0:2])
                outputfiledir = ("/").join(pathcontents)
                
                # Create flowcell level dir
                if not os.path.exists(outputdir):
                    os.mkdir(outputdir)
                #print(outputfiledir)

                # Create csv file with sample name
                outputfile = open(outputfiledir,"w+")
                header = ["RGID","RGSM","RGLB","Lane","Read1File","Read2File\n"]
                s3_path_elements = [s3_dir,flowcell_id]
                s3_path = "/".join(s3_path_elements)
                s3_csv_path_elements = [s3_dir, flowcell_id, "csv_file"]
                s3_csv_path = "/".join(s3_csv_path_elements)

                # Write to file
                outputfile.write(",".join(header))
                
                sampleno = ["S",str(samplecount)]
                fastq_base = [Sample_Name, "".join(sampleno)]
                lanes = [1,2,3,4]
                for l in lanes:
                    L = ["L00",str(l)]
                    lane = "".join(L)
                    read1 = "R1"
                    read2 = "R2"
                    fastq1_elements = [lane, read1, "001.fastq.gz"]
                    fastq1_elements = fastq_base + fastq1_elements
                    fastq1 = "_".join(fastq1_elements)
                    fastq1_dir = s3_path_elements + [Sample_ID] + [fastq1]
                    fastq2_elements = [lane, read2, "001.fastq.gz\n"]
                    fastq2_elements = fastq_base + fastq2_elements
                    fastq2 = "_".join(fastq2_elements)
                    fastq2_dir = s3_path_elements + [Sample_ID] + [fastq2]

                    outputline = [
                            index,
                            Sample_Name,
                            "UnknownLibrary",
                            str(l),
                            "/".join(fastq1_dir),
                            "/".join(fastq2_dir)]

                    outputfile.write(",".join(outputline))
                    allsamples_csv.write(",".join(outputline))

                outputfile.close()
                samplecount += 1
                #print(index)

            else:
                fixedline = replace_last(line, '\r\n', '')

        print(str(samplecount-1))
        allsamples_csv.close()
    #break


# dragen csv format
#RGID,RGSM,RGLB,Lane,Read1File,Read2File
#CACACTGA.1,RDSR181520,UnknownLibrary,1,/staging/RDSR181520_S1_L001_R1_001.fastq,/staging/RDSR181520_S1_L001_R2_001.fastq




#!/usr/bin/env python3

'''
Viral samples - QC

Author: Aura Zelco
Date: 2024/04/25

Brief description:
This script examines the viral samples QC file, and checks whether the samples are of good enough quality. 

'''
################## MODULES ##################

import argparse
import pandas as pd

################## ARGPARSE ##################

# description of program, printed when -h is called in the command line
usage = 'This script examines the viral samples QC file, and checks whether the samples are of good enough quality.'

# creates an ArgumentParser object which has assigned name 'parser'
parser = argparse.ArgumentParser(prog='Viral_Samples_QC', description=usage)

# specification of input files directory - required
parser.add_argument(
    '-i',
    metavar = 'INPUT_VIRAL_SAMPLE_QC_FILE',
    dest = 'viral_file',
    type=argparse.FileType('r'), # readable file
    required=True, # required, otherwise the script does not run
    help="REQUIRED: input viral samples QC file to check - example: -i samples.txt" 
    )

# Custom function to check whether the input file is a txt file
def file_ext(ext_choices,fname):
    ext = os.path.splitext(fname)[1][1:]
    if ext not in ext_choices:
       parser.error("Input file doesn't end with {}, please use a {} file instead".format(ext_choices))
    return fname

parser.add_argument('file_ext',type=lambda s:file_choices(("txt"),s))

# returns result of parsing 'parser' to the class args
args = parser.parse_args()

################## MAIN ##################

# opens the file
viral_input  = pd.read_table(args.viral_file.readlines(), sep=",")
QC_sum = viral_input.groupby('qc_pass').size()

print("The following table shows how many samples have passed the QC (True) or not (False):\n")
print(QC_sum)

QC_fail = viral_input[viral_input.qc_pass == 'FALSE'].shape[0]
pct_fail = QC_fail * 100 / len(viral_input.index) 
if pct_fail >= 10:
    print("Warning: This file contains 10 percent or more failed samples. Please review the file in detail.")
else:
    print("The file has less than 10 percent of failed samples, and it can proceed with the downstream analysis")
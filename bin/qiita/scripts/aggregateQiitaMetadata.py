# downloadQiitaMetadata.py
# Adam Klie
# 08/17/2020
# Script used to aggregate metadta downloaded from Qiita
# Script called in aggregate_qiita.sbatch to parallelize over all studies

# Import neeeded packages
import pandas as pd
import numpy as np
import tqdm
import glob
import os
import argparse

# Read in the study ids from args file
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--id_file', type=str, help='filepath to File IDs')
# TODO - Add argument for download dir where Qiita donwloaded metadata is ../data/qiita/slurm_files
args = parser.parse_args()
with open(args.id_file, 'r') as f:
    file_ids = [ID.strip() for ID in f.readlines()]
    
# Move into directory with downloaded Qiita metadata
os.chdir('../data/qiita/download')

# Loop through the files for each study in the input file and combine the metadata into a pandas Series
qiita_pairs = pd.Series(index = pd.MultiIndex(levels=[[],[]], labels=[[],[]], names=[u'Sample_ID', u'Attribute']))
for ID in tqdm.tqdm(file_ids):
    id_files = sorted(glob.glob("{}_*".format(ID)))
    if len(id_files) >= 2: 
        meta_data = pd.read_csv(id_files[0], sep='\t', index_col=0, low_memory=False)
        study_prep_data = pd.DataFrame()
        for i in id_files[1:]:
            prep_data = pd.read_csv(i, sep='\t', index_col=0, low_memory=False)
            study_prep_data = pd.concat([study_prep_data, prep_data], sort=True)
        full_data = meta_data.merge(study_prep_data, how='outer', left_index=True, right_index=True) 
        attribute_value_pairs = full_data.T.unstack()
        qiita_pairs = pd.concat([qiita_pairs, attribute_value_pairs], axis=0)    
    else:
        print(id_files)

# Save the attribute-value pair Series as a pickle object
out = ('../' + args.id_file.split('/')[-1].split('.')[0] + '.pickle')
qiita_pairs.to_pickle(out)
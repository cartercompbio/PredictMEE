# PredictMEE - <ins>Predict</ins>ing <ins>M</ins>issing Metadata with <ins>E</ins>ntity <ins>E</ins>xtraction

## Requirements

### Conda or miniconda installation
The predictMEE model and analysis workflow requires a variety of packages to be installed prior to running the code. The easiest way to install all the necessary packages is by installing the [Anaconda3 or minconda3 python package manager](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html).

### Data
The data download script to automate the download and preprocessing of the SRA attribute-value pairs is still a work in progress. For now you can find the data that was used [here](https://drive.google.com/drive/u/0/folders/11-h1sSSKtuy0fbmMl24iLN0L68y0rt7-). 

### Word Embedding Model
The downloadable word2vec model can be found [here](https://github.com/cambridgeltl/BioNLP-2016)

## Installation
You can clone this repo to the curent directory with
```bash
git clone https://github.com/cartercompbio/PredictMEE.git
```

## Configuring environment
Then, install the required packages with the following commands
```bash
cd predictMEE/config
conda env create -f PredictMEE_2020_08_24.yml  # Load the envrionment
conda activate PredictMEE_new # Activate the environment
```

If you are planning on recapitulatiing the full analysis, you will need to mimic the file structure shown below.
```bash
├── bin
│   ├── dataLandscapeSRA.ipynb
│   ├── downloadData.ipynb
│   ├── evaluateModel.ipynb
│   ├── evaluatePrediction.ipynb
│   ├── generateTestSet.ipynb
│   ├── mergeAttributes.ipynb
│   ├── predictMetadata.ipynb
│   └── trainModels.ipynb
├── config
│   └── deep_nlp_cpu.yml
├── data
│   ├── allSRS_05_15_2018.pickle
│   ├── BioSampleAttributes.pickle
│   ├── BioSampleAttributes.xml
│   ├── sra_dump.pickle
│   └── wikipedia-pubmed-and-PMC-w2v
├── doc
│   ├── figures
│   ├── submission
│   └── tables
├── models
├── README.md
└── results
    ├── embedding
    ├── prediction
    ├── training
    └── validation
```

## Running notebooks
Certain notebooks require data and output from other notebooks. In order to run the analysis as was completed for the paper cited below, run the notebooks in the following order.
1. downloadData.ipynb
2. dataLandscapeSRA.ipynb
3. mergeAttributes.ipynb
3. generateTestSet.ipynb
4. trainModels.ipynb
5. evaluateModel.ipynb
6. predictMetadata.ipynb
7. evaluatePrediction.ipynb

## Preprint Citation
Klie A, Tsui BY, Mollah S, Skola D, Dow M, Hsu C-N, Carter H. Increasing metadata coverage of SRA BioSample entries using deep learning based Named Entity Recognition. bioRxiv. 2020:414136. doi: 10.1101/414136.

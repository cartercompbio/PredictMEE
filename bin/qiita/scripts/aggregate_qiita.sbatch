#!/bin/bash
#SBATCH --job-name=aggregate_qiita
#SBATCH --mail-type=ALL
#SBATCH --mail-user=aklie@eng.ucsd.edu
#SBATCH --cpus-per-task=1
#SBATCH --time=00:30:00
#SBATCH --mem-per-cpu=16G
#SBATCH --array=1-27%27
#SBATCH -o ../doc/log/%A.%x.%a.out
#SBATCH -e ../doc/err/%A.%x.%a.err

##############################################
#                JOB INFO                    #
##############################################
echo "Date              = $(date)"
echo "Hostname          = $(hostname -s)"
echo "Working Directory = $(pwd)"
echo ""
echo "Job Name                       = $SLURM_JOB_NAME"
echo "Number of Tasks Allocated      = $SLURM_NTASKS"
echo -e "Number of Cores/Task Allocated = $SLURM_CPUS_PER_TASK\n"

##############################################
# !!!!! JOB COMMANDS BELOW THIS HEADER !!!!! #
##############################################

# USAGE: sbatch aggregate_qiita.sbatch

# Log file reading in and point to correct python
echo -e "Aggregating metadata from file_ids_${SLURM_ARRAY_TASK_ID}.txt"
PYTHON_DIR=/cellar/users/aklie/opt/miniconda3/envs/PredictMEE_new/bin

${PYTHON_DIR}/python aggregateQiitaMetadata.py -i ../data/qiita/file_ids_${SLURM_ARRAY_TASK_ID}.txt
# ═══════════════════════════════════════════════════════════════════
# networksecurity/constants/training_pipeline/__init__.py
# ═══════════════════════════════════════════════════════════════════
# Poore project mein use hone wale SAB constants yahan hain
# Koi bhi hardcoded value file mein nahi hogi — sab yahan se aayegi
#
# WHY CONSTANTS FOLDER?
# Pehle teen projects mein:
#   Student Performance → paths data_ingestion.py mein hardcode the
#   Heart Disease       → same — har file mein apni paths
#   SMS Spam            → same — utils.py mein values directly
#
# Yahan (MLOps style):
#   Sab values EK JAGAH — constants/training_pipeline/__init__.py
#   Koi bhi file import karke use kare
#   Path change karna ho → sirf yahan aao — poora project update
#
# IMP: __init__.py isliye — taaki
#      "from networksecurity.constants import training_pipeline"
#      kaam kare — yeh folder ek Python package ban jaata hai
###==============================================================

import os
import sys
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────────────────────────
# COMMON CONSTANTS — poore pipeline mein use honge
# ─────────────────────────────────────────────────────────────────

TARGET_COLUMN = "Result"
# dataset mein yeh column predict karna hai
# phishing = 1, legitimate = -1

PIPELINE_NAME = "NetworkSecurity"
# pipeline ka naam — artifacts folder structure mein use hoga

ARTIFACT_DIR = "Artifacts"
# IMP: root folder — sab pipeline outputs yahan save honge
# timestamped subfolders honge:
# Artifacts/
# └── 08_24_2026_14_32_00/   ← har run ka alag folder
#     ├── data_ingestion/
#     ├── data_validation/
#     ├── data_transformation/
#     └── model_trainer/
#
# PEHLE TEEN PROJECTS MEIN:
# artifacts/ → sab kuch overwrite hota tha har run pe
# YAHAN:
# Artifacts/timestamp/ → har run ka alag folder
# → full run history maintain hoti hai → MLOps best practice

FILE_NAME = "phishingData.csv"
# feature store mein save hone wali raw file ka naam

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME  = "test.csv"
# split ke baad train/test files ke naam


# ─────────────────────────────────────────────────────────────────
# DATA INGESTION CONSTANTS
# prefix: DATA_INGESTION_ → easily identify karo kahan use hoga
# ─────────────────────────────────────────────────────────────────

DATA_INGESTION_COLLECTION_NAME:  str   = "NetworkData"
# MongoDB collection naam — pushdata.py ne yahan data daala tha
# DataIngestion yahan se pull karega

DATA_INGESTION_DATABASE_NAME:    str   = "ALYAN"
# MongoDB database naam

DATA_INGESTION_DIR_NAME:         str   = "data_ingestion"
# artifact subfolder naam
# path banega: Artifacts/timestamp/data_ingestion/

DATA_INGESTION_FEATURE_STORE_DIR: str  = "feature_store"
# raw data yahan save hoga
# path: Artifacts/timestamp/data_ingestion/feature_store/phishingData.csv
# IMP: feature store = raw data ka backup — split se pehle

DATA_INGESTION_INGESTED_DIR:     str   = "ingested"
# split ke baad train/test yahan save honge
# path: Artifacts/timestamp/data_ingestion/ingested/train.csv
#       Artifacts/timestamp/data_ingestion/ingested/test.csv

DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
# 80% train, 20% test
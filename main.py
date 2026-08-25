# ═══════════════════════════════════════════════════════════════════
# main.py
# ═══════════════════════════════════════════════════════════════════
# Entry point — pipeline manually test karne ke liye
# Production mein TrainingPipeline.run_pipeline() use hoga
# Abhi sirf DataIngestion test kar rahe hain
###==============================================================

import sys


from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig
)
if __name__ == "__main__":
    try:
        logging.info("Training Pipeline started")

        # ── STEP 1: Master Config ──────────────────────────────────
        # timestamp generate hoga — sab artifacts ek folder mein
        training_pipeline_config = TrainingPipelineConfig()
        logging.info(f"Artifact dir: {training_pipeline_config.artifact_dir}")

        # ── STEP 2: Data Ingestion ─────────────────────────────────
        # MongoDB → feature_store → train/test split → artifact
        data_ingestion_config = DataIngestionConfig(
            training_pipeline_config=training_pipeline_config
        )
        data_ingestion = DataIngestion(
            data_ingestion_config=data_ingestion_config
        )
        logging.info("DataIngestion initialized")

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info(f"DataIngestion completed: {data_ingestion_artifact}")
        # data_ingestion_artifact:
        # ├── train_file_path = "Artifacts/.../ingested/train.csv"
        # └── test_file_path  = "Artifacts/.../ingested/test.csv"

        # ── STEP 3: Data Validation ────────────────────────────────
        # schema check → drift detection → valid data save → artifact
        data_validation_config = DataValidationConfig(
            training_pipeline_config=training_pipeline_config
        )
        # IMP: same training_pipeline_config inject karo
        # taaki same Artifacts/timestamp/ folder use ho

        data_validation = DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            # ↑ DataIngestion ka output → DataValidation ka input
            # train/test paths yahan se milenge
            data_validation_config=data_validation_config
        )
        logging.info("DataValidation initialized")

        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info(f"DataValidation completed: {data_validation_artifact}")
        # data_validation_artifact:
        # ├── validation_status       = True/False
        # ├── valid_train_file_path   = "Artifacts/.../validated/train.csv"
        # ├── valid_test_file_path    = "Artifacts/.../validated/test.csv"
        # ├── invalid_train_file_path = "Artifacts/.../invalid/train.csv"
        # ├── invalid_test_file_path  = "Artifacts/.../invalid/test.csv"
        # └── drift_report_file_path  = "Artifacts/.../drift_report/report.yaml"

        print(data_ingestion_artifact)
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
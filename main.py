# ═══════════════════════════════════════════════════════════════════
# main.py
# ═══════════════════════════════════════════════════════════════════
# Entry point — pipeline manually test karne ke liye
# Production mein TrainingPipeline.run_pipeline() use hoga
# Abhi sirf DataIngestion test kar rahe hain
###==============================================================

import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig
)

if __name__ == "__main__":
    try:
        logging.info("Training Pipeline started")

        # Step 1: Master config banao — timestamp generate hoga
        training_pipeline_config = TrainingPipelineConfig()
        logging.info(f"Artifact dir: {training_pipeline_config.artifact_dir}")

        # Step 2: DataIngestion config banao — paths milenge
        # IMP: TrainingPipelineConfig inject karo — same timestamp use hoga
        data_ingestion_config = DataIngestionConfig(
            training_pipeline_config=training_pipeline_config
        )

        # Step 3: DataIngestion object banao — config inject karo
        data_ingestion = DataIngestion(
            data_ingestion_config=data_ingestion_config
        )
        logging.info("DataIngestion initialized")

        # Step 4: Pipeline run karo — artifact milega
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info(f"DataIngestion completed: {data_ingestion_artifact}")

        print(data_ingestion_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
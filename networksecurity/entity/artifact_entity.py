# ═══════════════════════════════════════════════════════════════════
# networksecurity/entity/artifact_entity.py
# ═══════════════════════════════════════════════════════════════════
# Har pipeline component ka RETURN TYPE yahan define hota hai.
#
# WHY ARTIFACT ENTITY?
# PEHLE TEEN PROJECTS MEIN:
#   return (train_path, test_path)  ← simple tuple
#   koi bhi order mein unpack kar sakta tha → bugs
#   type information nahi thi
#
# YAHAN (MLOps style):
#   return DataIngestionArtifact(train_file_path=..., test_file_path=...)
#   typed object → IDE autocomplete → type checking → professional
#   DataValidation ko exactly pata hai kya expect karna hai
###==============================================================

from dataclasses import dataclass

# @dataclass → __init__ auto ban jaata hai
# sirf fields define karo → class ready

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    # "Artifacts/timestamp/data_ingestion/ingested/train.csv"

    test_file_path: str
    # "Artifacts/timestamp/data_ingestion/ingested/test.csv"

# IMP: DataValidation in paths se data padhega
# koi bhi component jo DataIngestion ke baad aaye
# use DataIngestionArtifact milega → type-safe




# ── ARTIFACT 2: DataValidationArtifact ───────────────────────────
# DataValidation.initiate_data_validation() yeh return karega
# DataTransformation ko yeh milega → valid paths se data padhega
@dataclass
class DataValidationArtifact:
    validation_status: bool
    # True = data valid hai → pipeline aage chale
    # False = data invalid hai → pipeline rok do

    valid_train_file_path: str
    # validated/train.csv → DataTransformation yahan se padhega
    # "Artifacts/timestamp/data_validation/validated/train.csv"

    valid_test_file_path: str
    # validated/test.csv → DataTransformation yahan se padhega
    # "Artifacts/timestamp/data_validation/validated/test.csv"

    invalid_train_file_path: str
    # invalid/train.csv → agar drift detect hua → yahan save hoga
    # "Artifacts/timestamp/data_validation/invalid/train.csv"

    invalid_test_file_path: str
    # invalid/test.csv
    # "Artifacts/timestamp/data_validation/invalid/test.csv"

    drift_report_file_path: str
    # drift_report/report.yaml → KS test results yahan save honge
    # "Artifacts/timestamp/data_validation/drift_report/report.yaml"

    
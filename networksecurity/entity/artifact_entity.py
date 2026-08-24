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
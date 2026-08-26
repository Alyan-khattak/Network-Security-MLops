# ═══════════════════════════════════════════════════════════════════
# networksecurity/utils/main_utils/utils.py
# ═══════════════════════════════════════════════════════════════════
# Common reusable utility functions — poore project mein import hoti hain
#
# PEHLE TEEN PROJECTS MEIN:
#   utils.py → save_object, load_object, evaluate_models
#
# YAHAN (MLOps style):
#   utils/main_utils/utils.py → YAML read/write bhi hai
#   YAML kyun? drift_report.yaml, schema.yaml → structured config files
#   utils/ml_utils/ → model specific utilities (alag folder)
#
# FUNCTIONS:
# read_yaml_file()  → schema.yaml padhta hai → dict return karta hai
# write_yaml_file() → drift report.yaml likhta hai
###==============================================================

import os
import sys
import yaml                          # YAML files parse karne ke liye
                                     # pip install pyaml

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import numpy as np
import dill

# ══════════════════════════════════════════════════════════════════
# FUNCTION 1: read_yaml_file
# ══════════════════════════════════════════════════════════════════
def read_yaml_file(file_path: str) -> dict:
    """
    YAML file padhta hai aur Python dict mein convert karta hai.

    KAHAN USE HOTA HAI:
    DataValidation.__init__() mein:
        self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        # data_schema/schema.yaml padhta hai
        # expected columns aur types milte hain
        # validate_number_cols() aur check_numerical_col() mein use hoga

    Parameters:
        file_path (str) : YAML file ka path
                          e.g. "data_schema/schema.yaml"

    Returns:
        dict : YAML content Python dict mein
               e.g. {"columns": [...], "numerical_columns": [...]}
    """
    try:
        with open(file_path, "rb") as yaml_file:
            # "rb" = read binary mode
            # yaml.safe_load → YAML string → Python dict
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)


# ══════════════════════════════════════════════════════════════════
# FUNCTION 2: write_yaml_file
# ══════════════════════════════════════════════════════════════════
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Python dict ko YAML file mein likhta hai.

    KAHAN USE HOTA HAI:
    DataValidation.detect_data_drift() mein:
        write_yaml_file(drift_report_file_path, report)
        # KS test results YAML mein save hote hain
        # "Artifacts/timestamp/data_validation/drift_report/report.yaml"

    Parameters:
        file_path (str)    : jahan save karna hai
        content   (object) : jo likhna hai (dict → YAML)
        replace   (bool)   : True → existing file delete karke naya banao
                             False → existing file pe append (default)

    Returns:
        None — sirf file likhta hai
    """
    try:
        if replace:
            # IMP: replace=True → purani file delete karo
            # warna YAML mein duplicate entries aa sakte hain
            if os.path.exists(file_path):
                os.remove(file_path)

        # folder banao agar exist nahi karta
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            # yaml.dump → Python dict → YAML string → file mein likho
            yaml.dump(content, file)

    except Exception as e:
        raise NetworkSecurityException(e, sys)




# ══════════════════════════════════════════════════════════════════
# FUNCTION 3: save_numpy_array_data
# ══════════════════════════════════════════════════════════════════
def save_numpy_array_data(file_path:str, array: np.array):
    try:
        logging.info("Entered The Save numpy array  method of util.py to save ")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)




# ══════════════════════════════════════════════════════════════════
# FUNCTION 4: save_object
# ══════════════════════════════════════════════════════════════════
def save_object(file_path:str, obj: object):
    try:
        logging.info("Entered The Save object method of util.py to save {obj} ")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(file_obj, obj)

        logging.info("Existed the mehod and saved : {obj} ")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

    





# ─────────────────────────────────────────────────────────────────
# DRY RUN
#
# read_yaml_file("data_schema/schema.yaml")
# → {"columns": [{"having_IP_Address": "int64"}, ...],
#    "numerical_columns": ["having_IP_Address", ...]}
#
# write_yaml_file("Artifacts/.../drift_report/report.yaml",
#                 {"having_IP_Address": {"p_value": 0.23, "drift_status": False}, ...})
# → YAML file ban gayi:
#   having_IP_Address:
#     drift_status: false
#     p_value: 0.23
# ─────────────────────────────────────────────────────────────────
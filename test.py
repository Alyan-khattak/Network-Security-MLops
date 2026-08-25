from networksecurity.utils.main_utils.utils import read_yaml_file

from networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH  # this schma is defrine in data_schema/schema.yml and we will compare the incoming schema with this to validate 

data_schema = read_yaml_file(SCHEMA_FILE_PATH)

print(data_schema["numerical_columns"])

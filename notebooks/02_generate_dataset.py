import json
import os
import sys

# This will add the src directory to sys.path
# meaning that the privacy_fingerprint will be found
# note it assumes the current working directory is the folder containing this notebook
sys.path.append("/Users/zellaking/Repos/privfp-poc/src")


from privacy_fingerprint.common.config import (
    load_global_config_from_file,
    load_experiment_config_from_file,
    load_experiment_config,
)
import privacy_fingerprint.generate.synthea as synthea
import privacy_fingerprint.generate.language_model as llm
import privacy_fingerprint.extract.aws_comprehend as aws


# Example config files are available in the config directory.
# These files will need to be customised with your API keys.

load_global_config_from_file("../configs/global_config.yaml")
load_experiment_config_from_file("../configs/experiment_config.yaml")

# Config options can be modified inline. To keep this notebook/experiment small
# the number of records will be changed to 10.
expt_config = load_experiment_config()
expt_config.synthea.encounter_type = "Encounter for symptom"
expt_config.synthea.num_records = 10  # 100_000 used to create dataset1
load_experiment_config(expt_config.dict())


# The Synthea output will be saved to a directory
output_dir = "../experiments/02_generate_dataset"
os.makedirs(output_dir, exist_ok=True)
export_directory = os.path.join(output_dir, "synthea")

synthea_records = synthea.generate_records(export_directory)

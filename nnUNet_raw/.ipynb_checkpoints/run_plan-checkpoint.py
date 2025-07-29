import os

# Manually define all paths here
os.environ["nnUNet_raw"] = "/scratch/scai/mtech/aib232081/nnUNet_raw_data"
os.environ["nnUNet_preprocessed"] = "/scratch/scai/mtech/aib232081/nnUNet_preprocessed"
os.environ["nnUNet_results"] = "/scratch/scai/mtech/aib232081/nnUNet_results"

# Now import and run the planner
from nnunetv2.experiment_planning.plan_and_preprocess_entrypoints import plan_and_preprocess_entry

if __name__ == '__main__':
    plan_and_preprocess_entry()


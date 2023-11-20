# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/NatchaC89/kidney-disease-classification
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.8 -y
```

```bash
conda activate kidney
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/NatchaC89/kidney-disease-classification.mlflow \
MLFLOW_TRACKING_USERNAME=NatchaC89 \
MLFLOW_TRACKING_PASSWORD=439f36b80d315b8c5b503b55f86b80dab409ac25 \
python script.py


```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/NatchaC89/kidney-disease-classification.mlflow
export MLFLOW_TRACKING_USERNAME=NatchaC89
export MLFLOW_TRACKING_PASSWORD=439f36b80d315b8c5b503b55f86b80dab409ac25
```
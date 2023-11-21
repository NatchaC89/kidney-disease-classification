from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingpipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
import os

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingpipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/NatchaC89/kidney-disease-classification.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "NatchaC89"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "439f36b80d315b8c5b503b55f86b80dab409ac25"

STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e
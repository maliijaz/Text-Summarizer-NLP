from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from TextSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<")
      data_ingestion = DataIngestionPipeline()
      data_ingestion.main()
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} completed! <<<<<<<<<<<<<")
except Exception as e:
      logger.exception(e)
      raise e



STAGE_NAME = "Data validation Stage"
try:
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<")
      data_validation = DataValidationPipeline()
      data_validation.main()
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} completed! <<<<<<<<<<<<<")
except Exception as e:
      logger.exception(e)
      raise e



STAGE_NAME = "Data Transformation Stage"
try:
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<")
      data_transformation = DataTransformationPipeline()
      data_transformation.main()
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} completed! <<<<<<<<<<<<<")
except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Model Trainer Stage"
try:
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<")
      model_trainer = ModelTrainerPipeline()
      model_trainer.main()
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} completed! <<<<<<<<<<<<<")
except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Model Evaluation Stage"
try:
      logger.info(f"*******************")
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<<<<")
      model_evaluation = ModelEvaluationPipeline()
      model_evaluation.main()
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} completed! <<<<<<<<<<<<<")
except Exception as e:
      logger.exception(e)
      raise e
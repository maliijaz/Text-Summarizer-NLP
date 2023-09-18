from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from TextSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} started <<<<<<<<<<<<<")
      data_ingestion = DataIngestionPipeline()
      data_ingestion.main()
      logger.info(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} completed! <<<<<<<<<<<<<")
except Exception as e:
      logger.error(f">>>>>>>>>>>>>>> stage: {STAGE_NAME} failed! <<<<<<<<<<<<<")
      logger.error(e)
      raise e
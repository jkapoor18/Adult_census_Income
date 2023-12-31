import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd 
import numpy as np
from dataclasses import dataclass
from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import ModelTraning
from src.components.data_transformation import DataTransformation
import warnings


#Run
#if __name__=="__main__":
def train_model():
    warnings.filterwarnings('ignore')
    obj=DataIngestion()
    test_path,train_path=obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(test_path,train_path)
    model_traning = ModelTraning()
    model_traning.initatied_model_traning(train_arr, test_arr)
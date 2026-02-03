import sys 
import os 
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from source.logger import logging
from source.exception import CustomeException

@dataclass
class DataPathConfig:
    train_path: str =os.path.join('artifact','train.csv')
    test_path: str =os.path.join('artifact','test.csv')
    raw_path: str =os.path.join('artifact','raw.csv')

class DataInjectionConfig:
    def __init__(self):
        self.injectionpath=DataPathConfig()

    def InitiateInjection(self):
        try:
            logging.info('Data injection has started')  
            df=pd.read_csv(r'D:\Project\new project\data\vitamin_deficiency_disease_dataset_20260123.csv')

            os.makedirs(os.path.dirname(self.injectionpath.train_path), exist_ok=True)

            df.to_csv(self.injectionpath.raw_path,index=False, header=True)
            logging.info('Train Test split initiated')

            train_df, test_df=train_test_split(df, random_state=42, test_size=0.25)

            train_df.to_csv(self.injectionpath.train_path,index=False, header=True)
            test_df.to_csv(self.injectionpath.test_path,index=False, header=True)
            return (
                self.injectionpath.train_path,
                self.injectionpath.test_path
            )
        except Exception as e:
            raise CustomeException(e,sys)

if __name__=="__main__":
    obj=DataInjectionConfig()
    train_data, test_data=obj.InitiateInjection()
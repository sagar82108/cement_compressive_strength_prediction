import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class predictpipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            preprocessor_path= os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
        
        except Exception as e:
            logging.info('error occured in data ingestion config')        
            raise CustomException(e,sys)


class customdata:
    def __init__(self,
                 cement:float,
                 blast_furnace_slag:float,
                 fly_ash:float,
                 water:float,
                 superplasticizer:float,
                 coarse_aggregate:float,
                 fine_aggregate:float,
                 age:float
                
                 ):
        
        self.cement=cement
        self.blast_furnace_slag=blast_furnace_slag
        self.fly_ash=fly_ash
        self.water=water
        self.superplasticizer=superplasticizer
        self.coarse_aggregate=coarse_aggregate
        self.fine_aggregate=fine_aggregate
        self.age=age
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
               'cement': [self.cement],
               'blast_furnace_slag': [self.blast_furnace_slag],
               'fly_ash': [self.fly_ash],
               'water': [self.water],
               'superplasticizer': [self.superplasticizer],
               'coarse_aggregate': [self.coarse_aggregate],
               'fine_aggregate ': [self.fine_aggregate],
               'age': [self.age]
            }

            df=pd.DataFrame(custom_data_input_dict)
            logging.info('dataframe gathered')
            return df
        
        except Exception as e:
            logging.info('exception occured in pipeline')        
            raise CustomException(e,sys)
    
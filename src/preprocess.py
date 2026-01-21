import pandas as pd                  # used to with the tables of data we are using
import numpy as np
import re                            # removes urls and punctuation to create clean text                        
import nltk                          # package for turning data into nlps
from nltk.corpus import stopwords    #
from sklearn.model_selection import train_test_split    # splits data into train and test
from sklearn.metrics import classification_report       # evaluation tool to prove the aii works
from sklearn.feature_extraction.text import CountVectorizer   
from sklearn.linear_model import LogisticRegression  


nltk.download('stopwords')
df = pd.read_csv('')

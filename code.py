import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
# NOTE: Modules in Anaconda can only open if you open VSCode via Anaconda/Anaconda prompt (type "code")
# OR perhaps just use this? & C:/Users/MattC/Anaconda3/python.exe c:/Users/MattC/Documents/GitHub/TensorFlow-Pokemon-Course/code.py

# Extracting data from CSV and limiting it to columns we care about...
df = pd.read_csv('pokemon.csv')
df = df[['isLegendary','Generation', 'Type_1', 'Type_2', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed','Color','Egg_Group_1','Height_m','Weight_kg','Body_Style']]
print(df)

# Converting a variable from boolean to an integer...
df['isLegendary'] = df['isLegendary'].astype(int)

# Pokemon element types are categorical, not ordinal. So converting to integers makes no sense.
# So instead we can create a new (dummy) variable for each category! Each of these indicate if it is of a particular type (1) or not (0).
def dummy_creation(df, dummy_categories):
    for i in dummy_categories:
        df_dummy = pd.get_dummies(df[i])
        df = pd.concat([df,df_dummy],axis=1)
        df = df.drop(i, axis=1)
    return(df)

df = dummy_creation(df, ['Egg_Group_1', 'Body_Style', 'Color','Type_1', 'Type_2'])


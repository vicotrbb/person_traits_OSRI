import pandas as pd
import numpy as np
import random
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import missingno as msno
from sklearn.tree import DecisionTreeRegressor

os.environ['PYTHONHASHSEED']=str(66)
np.random.seed(66)
random.seed(66)

# Loads pandas dataframe of dataset
data = pd.read_csv('files/data.csv', sep="\t")

# Sets features and targets fields
features = [
    "Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10","Q11","Q12","Q13","Q14",
    "Q15","Q16","Q17","Q18","Q19","Q20","Q21","Q22","Q23","Q24","Q25","Q26",
    "Q27","Q28","Q29","Q30","Q31","Q32","Q33","Q34","Q35","Q36","Q37","Q38",
    "Q39","Q40","Q41","Q42","Q43", "Q44"
]
target = ["age", "education", "gender", "orientation", "race", "religion", "hand"]

# Split into train/test dataset
X_train, X_test, y_train, y_test = train_test_split(data[features], data[target],
                                                    train_size=0.80, test_size=0.20)

# Fills NaN Values using SimpleImputer
imputer = SimpleImputer(strategy="median")
imputer.fit(X_train)
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)

imputer = SimpleImputer(strategy="median")
imputer.fit(y_train)
y_train = imputer.transform(y_train)
y_test = imputer.transform(y_test)

# Creates and train model
model = DecisionTreeRegressor(criterion='mse',
                              random_state=42,
                              splitter='best')

model.fit(X_train, y_train)
model.save('OSRI_Decision_Tree_model.hdf5')

sys.stdout.write("Modelo criado")
sys.stdout.write("Score do modelo: %.2f" % model.score(X_train, y_train))

# Flush system out print stream
sys.stdout.flush()

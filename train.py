import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

import pickle


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00342/Data_Cortex_Nuclear.xls'
mice = pd.read_excel(url)

X = mice.drop(['Genotype','Treatment','Behavior'], axis=1)
y = np.vectorize({'c-CS-m':0,'c-CS-s':1,'c-SC-m':2,'c-SC-s':3,'t-CS-m':4,'t-CS-s':5,'t-SC-m':6,'t-SC-s':7}.get)(mice['class'])

X1 = X.dropna(how='any', thresh=40)

X1[['number', 'version']] = X1.MouseID.str.split('_',expand=True)
X1.version = X1.version.astype('int')
cols = list(X1.columns[-2:])+list(X1.columns[:-2])
X1 = X1[cols]

X_updated = X1.set_index('number').copy()
X_updated.update(X1.groupby('number').mean().fillna(0), overwrite=False)
X_updated.reset_index(inplace=True)


x = X_updated.drop(['MouseID', 'number', 'version', 'class'], axis=1)
y = np.vectorize({'c-CS-m':0,'c-CS-s':1,'c-SC-m':2,'c-SC-s':3,'t-CS-m':4,'t-CS-s':5,'t-SC-m':6,'t-SC-s':7}.get)(X_updated['class'])


def correlation(df, threshold):
    col_corr = set()
    corr_matrix = df.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i,j]) > threshold:
                colname = corr_matrix.columns[i]
                col_corr.add(colname)
    return list(col_corr)
    
corr_features = correlation(x, 0.8)
print(len(corr_features))

pre_process = ColumnTransformer(transformers=[
                                    ('drop_columns', 'drop', corr_features),
                                    ('scale_data', MinMaxScaler(), list(set(x.columns)-set(corr_features)))
                                ])

model_pipeline = Pipeline(steps=[('pre_processing',pre_process),
                                 ('model', RandomForestClassifier(bootstrap=False, max_depth=20, n_estimators=1779))
                                 ])                               
model_pipeline.fit(x, y)
print('Model Trained')

pickle.dump(model_pipeline, open('model.pkl', 'wb'))
print('Model Saved')
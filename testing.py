import numpy as np
import pandas as pd

import pickle


X = pd.read_csv('test.csv')
xyz = pickle.load(open('model.pkl', 'rb'))

for row in X.iterrows():
    r = pd.DataFrame(columns=X.columns)
    r.loc[0] = row[1]
    preds = xyz.predict(r)

    cls = {
        0: 'c-CS-m',
        1: 'c-CS-s',
        2: 'c-SC-m',
        3: 'c-SC-s',
        4: 't-CS-m',
        5: 't-CS-s',
        6: 't-SC-m',
        7: 't-SC-s'
    }
    final_pred = np.vectorize(cls.get)(preds).reshape(-1, 1)

    print(final_pred)
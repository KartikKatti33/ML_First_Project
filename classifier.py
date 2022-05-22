# -*- coding: utf-8 -*-
"""

"""

import pandas as pd
import numpy as np
import pickle

Data = pd.read_csv("D:\Datascience\Projects\classifier\Social_Network_Ads.csv")

x= Data.iloc[:,:-1].values
y= Data.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train,X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.25, random_state=0)



from sklearn.preprocessing import StandardScaler
sc= StandardScaler()

X_train= sc.fit_transform(X_train)
X_test= sc.fit_transform(X_test)



from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5, metric= 'minkowski', p=2 )
classifier.fit(X_train, Y_train)

#pred = classifier.predict(sc.transform([[45,26000]]))

pickle.dump(classifier, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[45,26000]]))
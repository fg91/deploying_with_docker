from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas

# loading dataset
iris = load_iris()
x = iris.data
y = iris.target

# train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.5)

# build model
model = RandomForestClassifier(n_estimators = 10)

# train the classifier
model.fit(x_train, y_train)

# prediction
predicted = model.predict(x_test)

# evaluation
print(accuracy_score(predicted, y_test))

import pickle  # saves python object as binary file
with open('/Users/fabiograetz/ml/deploying_with_docker/deploying_random_forest/rf.pkl', 'wb') as model_pickle:
    pickle.dump(model, model_pickle)
    

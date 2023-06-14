# Training a Machine Learning Model

Now that we have prepared the dataset, we can train a machine learning model on the training data. In this example, we will be using a Support Vector Machine (SVM) algorithm:

```python
from sklearn.svm import SVC

# Create the SVM classifier
clf = SVC(kernel='linear')

# Train the classifier on the training data
clf.fit(X_train, y_train)
```



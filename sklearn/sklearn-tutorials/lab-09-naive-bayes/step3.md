# Train and Evaluate the Gaussian Naive Bayes Classifier

Now, we will train the Gaussian Naive Bayes classifier on the training set and evaluate its performance on the test set. We will use the `GaussianNB` class from the `sklearn.naive_bayes` module.

```python
from sklearn.naive_bayes import GaussianNB

# Create a Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Train the classifier
gnb.fit(X_train, y_train)

# Predict the target variable for the test set
y_pred = gnb.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = (y_pred == y_test).sum() / len(y_test)
print("Accuracy:", accuracy)
```

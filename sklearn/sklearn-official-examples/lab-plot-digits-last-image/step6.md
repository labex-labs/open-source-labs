# Improving the Model

If the accuracy of our model is not satisfactory, we can try improving it by tuning the hyperparameters of the SVM algorithm. For example, we can try changing the value of the `C` parameter:

```python
# Create the SVM classifier with a different value of C
clf = SVC(kernel='linear', C=0.1)

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy of the model
print("Accuracy:", accuracy)
```

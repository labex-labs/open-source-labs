# Create and Train the Decision Tree Classifier

Now, we can create and train the Decision Tree classifier using the training data.

```python
# Create a Decision Tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)
```

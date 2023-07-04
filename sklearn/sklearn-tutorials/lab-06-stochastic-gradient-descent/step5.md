# Train the Classifier

Now we can create and train the SGD classifier using scikit-learn's SGDClassifier class. We will use the 'hinge' loss function, which is commonly used for linear classifiers.

```python
clf = SGDClassifier(loss='hinge', random_state=42)
clf.fit(X_train, y_train)
```

# Create and train the MLP model

```python
# Create an MLP classifier with one hidden layer of 5 neurons
clf = MLPClassifier(hidden_layer_sizes=(5,), random_state=1)

# Train the model using the training data
clf.fit(X, y)
```

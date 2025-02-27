# Trainieren eines Klassifiziers mit SGD

Jetzt werden wir einen Klassifizierer mit der SGDClassifier-Klasse trainieren. Wir werden die log_loss-Verlustfunktion und die l2-Strafe verwenden.

```python
# Train a classifier using SGD
clf = SGDClassifier(loss="log_loss", penalty="l2", max_iter=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = clf.predict(X_test)

# Measure the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Classifier Accuracy:", accuracy)
```

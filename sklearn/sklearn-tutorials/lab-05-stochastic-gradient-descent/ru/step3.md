# Обучаем классификатор с использованием SGD

Теперь мы обучим классификатор с использованием класса SGDClassifier. Мы будем использовать функцию потерь log_loss и штраф l2.

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

# Улучшение модели

Если точность нашей модели неудовлетворительна, мы можем попробовать улучшить ее, настроив гиперпараметры алгоритма SVM. Например, мы можем попробовать изменить значение параметра `C`:

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

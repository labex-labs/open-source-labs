# Erstellen und Trainieren des Entscheidungsbaum-Klassifikators

Jetzt können wir den Entscheidungsbaum-Klassifikator (Decision Tree classifier) mit den Trainingsdaten erstellen und trainieren.

```python
# Create a Decision Tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)
```

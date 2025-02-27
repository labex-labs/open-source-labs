# Erstellen und Trainieren des Entscheidungsbaum-Klassifizierers

Jetzt können wir den Entscheidungsbaum-Klassifizierer erstellen und mit den Trainingsdaten trainieren.

```python
# Create a Decision Tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)
```
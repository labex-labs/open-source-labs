# Erstelle und trainiere das MLP-Modell

```python
# Erstelle einen MLP-Klassifizierer mit einer versteckten Schicht von 5 Neuronen
clf = MLPClassifier(hidden_layer_sizes=(5,), random_state=1)

# Trainiere das Modell mit den Trainingsdaten
clf.fit(X, y)
```

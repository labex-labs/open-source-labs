# Induktives Lernmodell deklarieren

In diesem Schritt werden wir das induktive Lernmodell deklarieren, das zur Vorhersage der Clusterzugehörigkeit für unbekannte Instanzen verwendet werden wird. Wir werden `RandomForestClassifier` aus scikit-learn als Klassifizierer verwenden.

```python
classifier = RandomForestClassifier(random_state=42)
inductive_learner = InductiveClusterer(clusterer, classifier).fit(X)
```

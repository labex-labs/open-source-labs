# Décclarer le modèle d'apprentissage inductif

Dans cette étape, nous allons déclarer le modèle d'apprentissage inductif qui sera utilisé pour prédire l'appartenance à un cluster pour des instances inconnues. Nous utiliserons `RandomForestClassifier` de scikit-learn comme classifieur.

```python
classifier = RandomForestClassifier(random_state=42)
inductive_learner = InductiveClusterer(clusterer, classifier).fit(X)
```

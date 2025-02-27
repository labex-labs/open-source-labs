# Declarar el modelo de aprendizaje inductivo

En este paso, declararemos el modelo de aprendizaje inductivo que se utilizará para predecir la pertenencia a un cluster de instancias desconocidas. Usaremos `RandomForestClassifier` de scikit-learn como clasificador.

```python
classifier = RandomForestClassifier(random_state=42)
inductive_learner = InductiveClusterer(clusterer, classifier).fit(X)
```

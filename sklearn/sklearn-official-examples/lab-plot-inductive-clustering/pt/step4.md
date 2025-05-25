# Declarar o Modelo de Aprendizagem Indutiva

Neste passo, declararemos o modelo de aprendizagem indutiva que será usado para prever a pertença a clusters para instâncias desconhecidas. Usaremos `RandomForestClassifier` da biblioteca scikit-learn como classificador.

```python
classifier = RandomForestClassifier(random_state=42)
inductive_learner = InductiveClusterer(clusterer, classifier).fit(X)
```

# Treinar o Modelo

Agora, treinaremos o modelo LOF usando os dados de treinamento. Definimos o número de vizinhos como 20 e a novidade como verdadeira. Também definimos a contaminação como 0,1.

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```

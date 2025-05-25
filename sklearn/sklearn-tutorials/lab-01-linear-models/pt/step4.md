# Regressão Logística

A regressão logística é um método de classificação que estima as probabilidades dos possíveis resultados usando uma função logística. É comumente usada para tarefas de classificação binária. A regressão logística também pode ser estendida para lidar com problemas de classificação multiclasse.

Vamos ajustar um modelo de regressão logística.

```python
clf = linear_model.LogisticRegression(random_state=0).fit(X, y)
print(clf.coef_)
```

- Criamos uma instância de `LogisticRegression` com o parâmetro `random_state` definido como 0.
- Usamos o método `fit` para ajustar o modelo aos dados de treinamento.
- Imprimimos os coeficientes do modelo de regressão logística.

# Gradiente Descendente Estocástico (SGD)

O Gradiente Descendente Estocástico (SGD) é uma abordagem simples, mas eficiente, para treinar modelos lineares. É particularmente útil quando o número de amostras e recursos é muito grande. O SGD atualiza os parâmetros do modelo usando um pequeno subconjunto dos dados de treinamento em cada iteração, o que o torna adequado para aprendizado online e aprendizado fora da memória.

Vamos ajustar um modelo de regressão logística usando SGD.

```python
clf = linear_model.SGDClassifier(loss="log_loss", max_iter=1000)
clf.fit(X, y)

print(clf.coef_)
```

- Criamos uma instância de `SGDClassifier` com o parâmetro `loss` definido como "log_loss" para realizar regressão logística.
- Usamos o método `fit` para ajustar o modelo aos dados de treinamento.
- Imprimimos os coeficientes do modelo de regressão logística obtido usando SGD.

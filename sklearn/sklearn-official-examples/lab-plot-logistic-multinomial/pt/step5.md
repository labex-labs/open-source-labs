# Treinar o Modelo de Regressão Logística um-contra-todos

Agora, treinaremos um modelo de regressão logística um-contra-todos usando os mesmos parâmetros do Passo 3, mas com a opção multi-classe definida como `"ovr"`. Em seguida, imprimiremos a pontuação de treinamento do modelo.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="ovr"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "ovr"))
```

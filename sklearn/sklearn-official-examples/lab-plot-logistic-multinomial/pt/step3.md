# Treinar o Modelo de Regressão Logística Multinomial

Agora, treinaremos um modelo de regressão logística multinomial usando a função `LogisticRegression` do scikit-learn. Definiremos o solucionador para `"sag"`, o número máximo de iterações para 100, o estado aleatório para 42 e a opção multi-classe para `"multinomial"`. Em seguida, imprimiremos a pontuação de treinamento do modelo.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```

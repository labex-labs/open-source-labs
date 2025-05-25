# Criar Modelo SVM com e sem Quebra de Empate

Neste passo, criaremos dois modelos SVM - um com quebra de empate desativada e outro com quebra de empate ativada. Usaremos a classe `SVC` do scikit-learn para criar esses modelos. O parâmetro `break_ties` é definido como `False` e `True` para os dois modelos, respectivamente.

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```

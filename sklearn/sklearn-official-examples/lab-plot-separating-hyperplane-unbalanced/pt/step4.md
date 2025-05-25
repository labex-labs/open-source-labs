# Ajustar o Modelo com Classes Ponderadas

Ajustaremos o modelo e obteremos o hiperplano separador usando a função `SVC` da biblioteca `svm`. Usaremos um kernel linear e definiremos `class_weight` para `{1: 10}`. Isso dará mais peso à classe menor.

```python
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(X, y)
```

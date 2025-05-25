# Plotar a Curva ROC

Em seguida, plotaremos a curva ROC usando a função `RocCurveDisplay.from_estimator`. Esta função recebe o classificador treinado, o conjunto de dados de teste e as etiquetas verdadeiras como entradas e retorna um objeto que pode ser usado para plotar a curva ROC. Em seguida, chamaremos o método `show()` para exibir o gráfico.

```python
svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
svc_disp.show()
```

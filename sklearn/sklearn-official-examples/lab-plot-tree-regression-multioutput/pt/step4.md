# Predizer

Neste passo, faremos previsões usando os modelos criados no passo anterior. Usaremos `np.arange` para criar um novo array de valores de -100 a 100 com um intervalo de 0,01 e, em seguida, usaremos o método `predict` dos nossos modelos para prever a saída.

```python
# Predizer
X_test = np.arange(-100.0, 100.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
y_3 = regr_3.predict(X_test)
```

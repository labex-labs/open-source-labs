# Evaluar el modelo

Evaluaremos el rendimiento de clasificación del modelo GPC entrenado. Generaremos una cuadrícula de puntos y calcularemos las probabilidades predichas para cada punto utilizando el modelo entrenado.

```python
# Evaluar la función real y la probabilidad predicha
res = 50
x1, x2 = np.meshgrid(np.linspace(-lim, lim, res), np.linspace(-lim, lim, res))
xx = np.vstack([x1.reshape(x1.size), x2.reshape(x2.size)]).T

y_true = g(xx)
y_prob = gp.predict_proba(xx)[:, 1]
y_true = y_true.reshape((res, res))
y_prob = y_prob.reshape((res, res))
```

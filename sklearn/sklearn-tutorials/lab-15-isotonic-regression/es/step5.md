# Visualizar los resultados

Finalmente, visualicemos los resultados de nuestro modelo de regresión isotónica. Podemos graficar los puntos de datos originales como puntos de dispersión y los valores predichos como una línea.

```python
import matplotlib.pyplot as plt

# Plot the original data and predicted values
plt.scatter(X, y, c='b', label='Original Data')
plt.plot(X_new, y_pred, c='r', label='Isotonic Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```

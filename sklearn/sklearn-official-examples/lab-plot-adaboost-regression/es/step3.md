# Graficando los resultados

Finalmente, graficamos qué tan bien se ajustan a los datos nuestros dos regresores, el regresor de árbol de decisión simple y el regresor AdaBoost. Usamos la función `scatter()` de Matplotlib para graficar las muestras de entrenamiento y los valores predichos por ambos regresores. Usamos la función `plot()` de Matplotlib para graficar los valores predichos en función de los datos para ambos regresores. Agregamos una leyenda al gráfico para distinguir entre los dos regresores.

```python
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, y, color=colors[0], label="muestras de entrenamiento")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("datos")
plt.ylabel("objetivo")
plt.title("Regresión de árboles de decisión potenciados")
plt.legend()
plt.show()
```

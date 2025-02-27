# Combinar objetos de visualización en una sola gráfica

Los objetos de visualización almacenan los valores calculados que se pasaron como argumentos. Esto permite combinar fácilmente las visualizaciones usando la API de Matplotlib. En el siguiente ejemplo, colocamos las visualizaciones una al lado de la otra en una fila.

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

roc_display.plot(ax=ax1)
pr_display.plot(ax=ax2)
plt.show()
```

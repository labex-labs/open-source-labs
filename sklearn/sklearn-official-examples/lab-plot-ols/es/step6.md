# Visualizar los resultados

Finalmente, podemos trazar los valores predichos contra los valores reales para visualizar qué tan bien el modelo se ajusta a los datos.

```python
import matplotlib.pyplot as plt

# Trazar las salidas
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```

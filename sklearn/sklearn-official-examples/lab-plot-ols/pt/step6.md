# Visualizar os Resultados

Finalmente, podemos plotar os valores previstos contra os valores reais para visualizar o quão bem o modelo se ajusta aos dados.

```python
import matplotlib.pyplot as plt

# Plotar os resultados
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```

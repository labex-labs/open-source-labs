# Visualizar os resultados

Finalmente, vamos visualizar os resultados do nosso modelo de regressão isotônica. Podemos plotar os pontos de dados originais como pontos dispersos e os valores previstos como uma linha.

```python
import matplotlib.pyplot as plt

# Plotar os dados originais e os valores previstos
plt.scatter(X, y, c='b', label='Dados Originais')
plt.plot(X_new, y_pred, c='r', label='Regressão Isotônica')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```

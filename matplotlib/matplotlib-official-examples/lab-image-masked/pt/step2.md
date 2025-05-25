# Criando Dados

Em seguida, criaremos alguns dados para usar em nossos gráficos. Para este tutorial, criaremos um gráfico de linha simples.

```python
# Create the data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.show()
```

# Gráfico de Dispersão (Scatter Plot)

Também podemos criar um gráfico de dispersão (scatter plot) para mostrar a relação entre duas variáveis categóricas. Neste caso, usaremos os mesmos dados de frutas e adicionaremos algum ruído aleatório às contagens para criar uma segunda variável.

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```

# Criação Automática de Legenda

Também podemos usar o método `PathCollection.legend_elements` para criar automaticamente uma legenda para um gráfico de dispersão. Este método tentará determinar um número útil de entradas de legenda a serem exibidas e retornará uma tupla de identificadores (handles) e rótulos (labels).

```python
N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 220, size=N)

fig, ax = plt.subplots()

scatter = ax.scatter(x, y, c=c, s=s)

# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
ax.add_artist(legend1)

# produce a legend with a cross-section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

plt.show()
```

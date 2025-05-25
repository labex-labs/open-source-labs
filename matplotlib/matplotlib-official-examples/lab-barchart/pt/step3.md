# Criar um Gráfico de Barras Agrupadas

Agora, podemos criar nosso gráfico usando a função `bar` do Matplotlib. Criaremos um loop que itera através de nossos atributos e cria um conjunto de barras para cada um. Também ajustaremos a largura das barras e a posição de cada conjunto de barras.

```python
x = np.arange(len(species))
width = 0.25
multiplier = 0

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    multiplier += 1
```

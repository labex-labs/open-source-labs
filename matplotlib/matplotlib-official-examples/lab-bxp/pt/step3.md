# Personalizar as estatísticas do boxplot

Podemos modificar qualquer uma das estatísticas do boxplot que foram calculadas no Passo 2. Neste exemplo, definimos a mediana de cada conjunto como a mediana de todos os dados e dobramos as médias.

```python
for n in range(len(stats)):
    stats[n]['med'] = np.median(data)
    stats[n]['mean'] *= 2
```

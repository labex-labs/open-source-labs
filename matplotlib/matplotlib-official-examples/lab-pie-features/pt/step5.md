# Personalizando as Cores

Podemos personalizar as cores das fatias passando uma lista de cores para o parâmetro `colors` da função `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray', 'saddlebrown'])
```

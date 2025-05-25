# Personalizando os Padrões de Hachura

Podemos personalizar os padrões de hachura das fatias passando uma lista de padrões de hachura para o parâmetro `hatch` da função `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```

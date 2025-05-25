# Definir a família de fontes

Definiremos a família de fontes como "serif" usando o parâmetro `font.family`. Adicionalmente, definiremos o parâmetro `font.serif` como uma lista vazia para usar a fonte serif padrão do LaTeX.

```python
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": [],
})
```

# Definir a fonte para o título

Definimos a fonte para o título do gráfico usando o método `set_title()` da classe `Axes`. Passamos o caminho da fonte como o parâmetro `font` e o nome do arquivo de fonte como o título do gráfico.

```python
ax.set_title(f'This is a special font: {fpath.name}', font=fpath)
```

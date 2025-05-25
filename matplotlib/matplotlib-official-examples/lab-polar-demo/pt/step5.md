# Personalizar o gráfico

Para personalizar o gráfico, podemos usar os seguintes métodos:

- `set_rmax` para definir o valor máximo para `r`
- `set_rticks` para definir os valores dos ticks para `r`
- `set_rlabel_position` para definir a posição dos rótulos radiais

```python
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5)
```

Também podemos adicionar um título ao gráfico usando o método `set_title`.

```python
ax.set_title("A line plot on a polar axis", va='bottom')
```

Finalmente, podemos adicionar uma grade ao gráfico usando o método `grid`.

```python
ax.grid(True)
```

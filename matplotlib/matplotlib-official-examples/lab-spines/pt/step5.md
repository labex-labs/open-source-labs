# Customizar Spines para os Lados Inferior e Esquerdo

No segundo subplot, exibiremos spines apenas nos lados inferior e esquerdo do gráfico. Podemos ocultar os spines nos lados direito e superior do gráfico usando o método `set_visible`.

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```

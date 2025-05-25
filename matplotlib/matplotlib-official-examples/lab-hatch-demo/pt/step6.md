# Adicionar um Patch de Elipse com Hachura

Você também pode adicionar patches hachurados ao seu gráfico. Neste caso, usaremos a função `add_patch` para adicionar um patch de elipse ao nosso gráfico.

```python
plt.gca().add_patch(Ellipse((4, 50), 10, 10, fill=True, hatch='*', facecolor='y'))
```

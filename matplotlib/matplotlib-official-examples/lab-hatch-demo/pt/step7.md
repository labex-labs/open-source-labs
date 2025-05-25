# Adicionar um Patch de Polígono com Hachura

Você também pode adicionar um patch de polígono com hachura. Neste caso, usaremos a função `add_patch` para adicionar um patch de polígono ao nosso gráfico.

```python
plt.gca().add_patch(Polygon([(10, 20), (30, 50), (50, 10)], hatch='\\/...', facecolor='g'))
```

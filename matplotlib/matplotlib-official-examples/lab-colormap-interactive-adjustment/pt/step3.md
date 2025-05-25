# Criar o Gráfico

Agora que você gerou os dados, criará o gráfico usando a função `imshow()`.

```python
fig, ax = plt.subplots()
im = ax.imshow(data2d)
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')
```

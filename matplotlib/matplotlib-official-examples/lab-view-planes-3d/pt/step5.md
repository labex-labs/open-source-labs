# Criar o gráfico 3D

Usamos `subplot_mosaic` para criar o gráfico 3D com base no layout definido no passo 4.

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```

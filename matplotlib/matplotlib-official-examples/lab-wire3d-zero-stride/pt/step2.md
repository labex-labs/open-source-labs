# Criar uma figura e dois subplots

Criaremos uma figura com dois subplots usando o método `subplots()`. Também definiremos a projeção para `'3d'` para que nossos subplots sejam tridimensionais.

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```

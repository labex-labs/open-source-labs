# Definir Escala de Cores e Criar Colorbar

Agora, definiremos a escala de cores para nossas imagens e criaremos uma colorbar para mostrar a faixa de valores. Encontraremos os valores mínimo e máximo para todas as imagens e normalizaremos a escala de cores de acordo.

```python
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axs, orientation='horizontal', fraction=.1)
```

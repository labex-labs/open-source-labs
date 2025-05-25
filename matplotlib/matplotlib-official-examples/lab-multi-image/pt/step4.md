# Atualizar Imagens

Finalmente, atualizaremos as imagens para responder a mudanças na norma de outras imagens. Isso nos permitirá alterar o colormap e a escala de cores de uma imagem e fazer com que todas as outras se atualizem de acordo.

```python
def update(changed_image):
    for im in images:
        if (changed_image.get_cmap() != im.get_cmap()
                or changed_image.get_clim() != im.get_clim()):
            im.set_cmap(changed_image.get_cmap())
            im.set_clim(changed_image.get_clim())

for im in images:
    im.callbacks.connect('changed', update)
```

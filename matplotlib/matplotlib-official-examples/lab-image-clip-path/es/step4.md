# Crear el parche

Para crear el parche, usaremos el módulo `patches` de Matplotlib. Crearemos un parche circular con un radio de 200 píxeles, centrado en el punto (260, 200).

```python
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
```

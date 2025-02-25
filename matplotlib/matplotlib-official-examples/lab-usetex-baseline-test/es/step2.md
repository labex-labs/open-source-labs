# Establecer la fuente de Matplotlib

Necesitamos establecer la fuente que se utilizará para el texto de Matplotlib. Utilizaremos la fuente Computer Modern y la estableceremos como la fuente predeterminada de Matplotlib.

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```

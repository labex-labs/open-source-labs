# Agregar marca de agua de texto

Para agregar una marca de agua de texto, podemos usar el método `text()` del objeto `Figure`. Necesitamos proporcionar la posición, el texto y otras propiedades como el tamaño de fuente, el color y la transparencia.

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```

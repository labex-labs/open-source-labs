# Guardar la gráfica

Finalmente, podemos guardar nuestra gráfica en el disco. Siga estos pasos:

1. Imprima los formatos de archivo admitidos utilizando `print(fig.canvas.get_supported_filetypes())`.

```python
print(fig.canvas.get_supported_filetypes())
```

2. Guarde la figura como un archivo de imagen utilizando `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")`. Descomente esta línea para guardar la figura.

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

Puede abrir el archivo de imagen guardado utilizando el explorador de archivos en la barra lateral izquierda.

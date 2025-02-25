# Personalizando las etiquetas de los ejes

Para personalizar las etiquetas de los ejes, podemos utilizar las funciones `set_xlabel` y `set_ylabel`. También podemos agregar saltos de línea utilizando el carácter "\n".

```python
ax0.set_xlabel('this is a xlabel\n(with newlines!)')
ax0.set_ylabel('this is vertical\ntest', multialignment='center')
```

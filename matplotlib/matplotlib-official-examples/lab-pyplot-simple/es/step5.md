# Guardar el trazado

Puede guardar el trazado como un archivo de imagen utilizando el método `savefig`. El siguiente código guarda el trazado como una imagen PNG:

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Índice')
plt.ylabel('Números')
plt.savefig('simple_plot.png')
```

# Aplicando la función

Ahora que tenemos las funciones, podemos usarlas para crear un mapa de calor con anotaciones. Creamos un nuevo conjunto de datos, damos argumentos adicionales a `imshow`, usamos un formato entero en las anotaciones y proporcionamos algunos colores. También ocultamos los elementos de la diagonal (que son todos 1) usando un `matplotlib.ticker.FuncFormatter`.

```python
data = np.random.randint(2, 100, size=(7, 7))
y = [f"Libro {i}" for i in range(1, 8)]
x = [f"Tienda {i}" for i in list("ABCDEFG")]

fig, ax = plt.subplots()
im, _ = heatmap(data, y, x, ax=ax, vmin=0, cmap="magma_r", cbarlabel="copias vendidas semanalmente")
annotate_heatmap(im, valfmt="{x:d}", size=7, threshold=20, textcolors=("rojo", "blanco"))

def func(x, pos):
    return f"{x:.2f}".replace("0.", ".").replace("1.00", "")

annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)
```

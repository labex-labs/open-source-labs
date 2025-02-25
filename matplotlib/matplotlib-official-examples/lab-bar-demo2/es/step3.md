# Crear el gráfico de barras con unidades predeterminadas

En este paso, crearemos el gráfico de barras con unidades predeterminadas utilizando el método `bar` de Matplotlib. Utilizaremos el parámetro `bottom` para establecer la base de las barras en 0.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].bar(cms, cms, bottom=bottom)
```

# El gráfico de sombreado más simple con barra de colores

En este paso, crearemos el gráfico de sombreado más simple con una barra de colores. Usaremos la función `contourf` para crear el gráfico de contorno relleno y especificaremos los sombreados usando el parámetro `hatches`.

```python
fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches=['-', '/', '\\', '//'],
                  cmap='gray', extend='both', alpha=0.5)
fig1.colorbar(cs)
```

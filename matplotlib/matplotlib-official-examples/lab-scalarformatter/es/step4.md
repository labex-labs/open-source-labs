# Graficar datos en subgráficas

Graficaremos los datos generados en las subgráficas que creamos en el Paso 3.

```python
for col in axs.T:
    col[0].plot(plot1_x, plot1_y)
    col[1].plot(plot2_x, plot2_y)
    col[2].plot(plot3_x, plot3_y)
```

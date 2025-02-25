# Crear subgráficos

Creamos tres subgráficos utilizando la función `subplots` en Matplotlib. Establecemos el parámetro `sharex` en `True` para asegurar que los subgráficos compartan un eje x común. También eliminamos el espacio vertical entre los subgráficos utilizando la función `subplots_adjust`.

```python
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
```

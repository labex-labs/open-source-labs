# Creación de un formateador de índice personalizado

Para representar los datos en función de un índice que va de 0, 1,... len(data), crearemos un formateador de índice personalizado. Este formateador formateará las marcas de graduación como fechas en lugar de enteros.

```python
# Crear formateador de índice personalizado
fig, ax2 = plt.subplots(figsize=(6, 3))
ax2.plot(r.adj_close, 'o-')

# Formatear el eje x como fechas
def format_date(x, _):
    try:
        # convertir datetime64 a datetime y usar strftime de datetime:
        return r.date[round(x)].item().strftime('%a')
    except IndexError:
        pass

ax2.set_title("Creación de un formateador de índice personalizado")
ax2.xaxis.set_major_formatter(format_date)  # internamente crea FuncFormatter
```

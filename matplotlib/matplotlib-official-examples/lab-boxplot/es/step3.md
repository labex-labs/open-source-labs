# Diagrama de caja predeterminado

Comenzaremos creando un diagrama de caja predeterminado para visualizar los datos. Utilizaremos la función `boxplot()` de Matplotlib y pasaremos los datos y las etiquetas como argumentos. También estableceremos el título del gráfico utilizando la función `set_title()`.

```python
fig, ax = plt.subplots()
ax.boxplot(data, labels=labels)
ax.set_title('Default Box Plot')
plt.show()
```

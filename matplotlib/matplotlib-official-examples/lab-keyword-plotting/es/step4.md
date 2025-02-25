# Generar un gráfico

En este paso, generaremos un gráfico de dispersión utilizando el diccionario `data` como entrada a la función `scatter()`. Utilizaremos las cadenas correspondientes a las variables `a`, `b`, `c` y `d` para generar el gráfico.

```python
fig, ax = plt.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entrada a', ylabel='entrada b')
plt.show()
```

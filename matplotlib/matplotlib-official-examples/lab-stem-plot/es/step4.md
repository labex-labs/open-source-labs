# Personalizar la gráfica

Podemos personalizar la gráfica ajustando la línea base utilizando el parámetro `bottom`. También podemos ajustar las propiedades de formato de la gráfica utilizando los parámetros `linefmt`, `markerfmt` y `basefmt`.

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

Esto generará una gráfica con un formato de línea gris y marcadores en forma de diamante. La línea base también se ha ajustado a 1.1.

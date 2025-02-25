# Ordenar los datos

Para obtener curvas nítidas, ordenaremos los datos utilizando el método `sort()`.

```python
# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]
# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()
```

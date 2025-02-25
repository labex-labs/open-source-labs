# Manejo de problemas de orden de bytes

Es posible que encuentres problemas de orden de bytes al trabajar con datos creados en una máquina con un orden de bytes diferente. Convierte los datos al orden de bytes nativo del sistema antes de pasarlos a Pandas.

```python
x = np.array(list(range(10)), ">i4")  # big endian
newx = x.byteswap().newbyteorder()  # forzar el orden de bytes nativo
s = pd.Series(newx)
```

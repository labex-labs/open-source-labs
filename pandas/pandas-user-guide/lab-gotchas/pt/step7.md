# Lidando com Problemas de Byte-ordering

Você pode encontrar problemas de byte-ordering ao lidar com dados criados em uma máquina com uma ordem de bytes diferente. Converta os dados para a ordem de bytes nativa do sistema antes de passá-los para Pandas.

```python
x = np.array(list(range(10)), ">i4")  # big endian
newx = x.byteswap().newbyteorder()  # force native byteorder
s = pd.Series(newx)
```

# Ajustando a Conversão

O argumento `converters` nos permite definir funções de conversão para lidar com conversões mais complexas. Ele aceita um dicionário com índices de coluna ou nomes de coluna como chaves e funções de conversão como valores.

```python
convertfunc = lambda x: float(x.strip(b"%"))/100.
np.genfromtxt(StringIO(data), converters={1: convertfunc})
```

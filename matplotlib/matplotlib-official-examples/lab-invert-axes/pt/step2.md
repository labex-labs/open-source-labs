# Criar Dados

Em seguida, precisamos criar alguns dados para plotar. Neste exemplo, criaremos um array de valores para o tempo (`t`) e um array de valores para a voltagem (`s`).

```python
t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)
```

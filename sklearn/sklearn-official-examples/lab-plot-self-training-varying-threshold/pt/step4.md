# Definir Valores de Limiar

```python
x_values = np.arange(0.4, 1.05, 0.05)
x_values = np.append(x_values, 0.99999)
```

Definimos um array de valores de limiar que variam de 0,4 a 1, com incrementos de 0,05. Em seguida, adicionamos um valor de limiar muito alto, 0,99999, para garantir que incluímos um valor que não resultará em amostras auto-rotuladas.

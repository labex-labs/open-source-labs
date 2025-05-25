# Criar o gráfico

Agora que temos nossos dados, podemos criar nosso gráfico usando Matplotlib. Neste exemplo, criaremos um gráfico de dispersão (scatter plot) usando a função `plot()`.

```python
fig, ax = plt.subplots()
plt.plot(x, y, 'o')
```

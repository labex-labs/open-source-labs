# Criar o gráfico

Agora, podemos criar o gráfico usando as datas e os valores y. Primeiro, criaremos um objeto figura e eixo usando a função subplots. Em seguida, plotaremos o gráfico usando a função plot. Copie e cole o seguinte código:

```python
fig, ax = plt.subplots()
ax.plot(dates, y**2, 'o')
```

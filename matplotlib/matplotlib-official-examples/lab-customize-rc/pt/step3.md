# Criar Subplots

Para criar subplots em Matplotlib, você pode usar o método `subplot()`. Este método recebe três argumentos: o número de linhas, o número de colunas e o número do gráfico. Aqui está um exemplo que cria três subplots:

```python
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([1, 2, 3])
plt.grid(True)

plt.subplot(313)
plt.plot([1, 2, 3])
plt.grid(True)
```

# Gerar Dados

Em seguida, precisamos gerar alguns dados para plotar. Neste exemplo, criaremos três arrays: um para os valores do eixo x, um para os valores do eixo y no primeiro gráfico e um para os valores do eixo y no terceiro gráfico.

```python
dt = 0.01
x = np.arange(-50.0, 50.0, dt)
y1 = np.arange(0, 100.0, dt)
y3 = np.sin(x / 3.0)
```

# Criando Gráficos

Agora, criaremos três subgráficos usando a função `plt.subplots`. Dois gráficos serão criados em uma figura, enquanto o terceiro gráfico será criado em uma figura separada.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```

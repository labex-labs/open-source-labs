# Criar o primeiro gráfico de eventos - orientação horizontal

Criaremos o primeiro gráfico de eventos em uma orientação horizontal.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
```

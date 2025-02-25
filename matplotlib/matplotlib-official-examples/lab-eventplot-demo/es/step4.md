# Crear el primer diagrama de eventos - Orientación horizontal

Crearemos el primer diagrama de eventos en una orientación horizontal.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
```

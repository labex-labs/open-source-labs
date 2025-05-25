# Eixos Gêmeos Quadrados

Produziremos eixos quadrados, com um eixo gêmeo (twin axes). O eixo gêmeo assume o aspecto da caixa (box aspect) do pai (parent).

```python
fig3, ax = plt.subplots()

ax2 = ax.twinx()

ax.plot([0, 10])
ax2.plot([12, 10])

ax.set_box_aspect(1)

plt.show()
```

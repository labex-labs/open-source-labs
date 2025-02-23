# Axes jumeaux carrés

Nous allons produire un axe carré, avec un axe jumeau. L'axe jumeau prend en compte l'aspect de la boîte du parent.

```python
fig3, ax = plt.subplots()

ax2 = ax.twinx()

ax.plot([0, 10])
ax2.plot([12, 10])

ax.set_box_aspect(1)

plt.show()
```

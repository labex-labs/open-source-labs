# Die Bereiche einfärben

Wir werden `fill_between` verwenden, um die Bereiche oberhalb und unterhalb der horizontalen Linie einzufärben, in denen die Sinuswelle positiv und negativ ist, respectively.

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```

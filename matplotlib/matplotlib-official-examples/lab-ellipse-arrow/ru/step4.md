# Разворачиваем стрелку ориентации

Если вы хотите развернуть стрелку ориентации, вы можете поменять тип маркера с `>` на `<`.

```python
# To reverse the orientation arrow, switch the marker type from > to <.
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```

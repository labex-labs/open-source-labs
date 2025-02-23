# Добавляем текстовую стрелку для указания направления

Для указания направления данных мы добавим текстовую стрелку с использованием функции `ax.text()` и параметра `bbox` с `boxstyle`, установленным на "rarrow".

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```

# Добавление легенды

Мы добавим легенду к графику с использованием функции `legend` из `matplotlib.pyplot`. Мы установим метки соответственно как `"не взвешенный"` и `"взвешенный"`.

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["non weighted", "weighted"],
    loc="upper right",
)
```

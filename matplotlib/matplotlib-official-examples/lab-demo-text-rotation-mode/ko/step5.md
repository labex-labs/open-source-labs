# 서브플롯에 텍스트 추가

`text` 함수를 사용하여 각 서브플롯에 텍스트를 추가합니다. `rotation`, `horizontalalignment`, `verticalalignment`, 및 `rotation_mode` 매개변수를 사용하여 텍스트를 회전하고 정렬합니다. 또한 `bbox` 매개변수를 사용하여 텍스트의 경계 상자를 강조 표시합니다.

```python
kw = (
    {} if mode == "default" else
    {"bbox": dict(boxstyle="square,pad=0.", ec="none", fc="C1", alpha=0.3)}
)

texts = {}

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        tx = ax.text(0.5, 0.5, "Tpg",
                     size="x-large", rotation=40,
                     horizontalalignment=ha, verticalalignment=va,
                     rotation_mode=mode, **kw)
        texts[ax] = tx
```

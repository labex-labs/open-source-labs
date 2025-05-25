# 축 제한 및 모양 사용자 정의

`set_xlim`, `set_ylim`, 및 `tick_params` 메서드를 사용하여 각 축의 제한 및 모양을 사용자 정의합니다.

```python
ax[0].set_xlim(0, 2)
ax[1].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[2].set_ylim(0, 2)
for ax1 in ax:
    ax1.tick_params(labelbottom=False, labelleft=False)
```

# 범례 추가

`matplotlib.pyplot`의 `legend` 함수를 사용하여 플롯에 범례를 추가합니다. 레이블은 각각 `"non weighted"`와 `"weighted"`로 설정합니다.

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["non weighted", "weighted"],
    loc="upper right",
)
```

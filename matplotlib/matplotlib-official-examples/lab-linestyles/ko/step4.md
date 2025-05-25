# 플롯 생성

각 선 스타일 집합에 대해 `plot_linestyles` 함수를 호출하여 플롯을 생성할 수 있습니다.

```python
fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[1, 3])

plot_linestyles(ax0, linestyle_str[::-1], title='Named linestyles')
plot_linestyles(ax1, linestyle_tuple[::-1], title='Parametrized linestyles')

plt.tight_layout()
plt.show()
```

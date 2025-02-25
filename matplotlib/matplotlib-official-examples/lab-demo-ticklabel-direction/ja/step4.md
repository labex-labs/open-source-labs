# 目盛りラベルを外向きにする

このステップでは、目盛りラベルが外向きになるサブプロットを作成します。

```python
fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(bottom=0.2)

ax = setup_axes(fig, 131)
for axis in ax.axis.values():
    axis.major_ticks.set_tick_out(True)
```

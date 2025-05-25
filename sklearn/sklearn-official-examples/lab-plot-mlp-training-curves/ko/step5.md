# 각 데이터셋의 학습 곡선 플롯

마지막으로, `plot_on_dataset` 함수를 사용하여 각 데이터셋의 학습 곡선을 플롯할 수 있습니다. 2x2 플롯을 생성하고 각 데이터셋을 별도의 축에 플롯합니다.

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for ax, data, name in zip(
    axes.ravel(), data_sets, ["iris", "digits", "circles", "moons"]
):
    plot_on_dataset(*data, ax=ax, name=name)

fig.legend(ax.get_lines(), labels, ncol=3, loc="upper center")
plt.show()
```

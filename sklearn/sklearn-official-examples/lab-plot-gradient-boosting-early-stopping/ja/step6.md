# 早期終了有無でのフィット時間比較

ここでは、2つのモデルのフィット時間を比較します。

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, time_gb, bar_width, label="Without early stopping", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, time_gbes, bar_width, label="With early stopping", color="coral"
)

max_y = np.amax(np.maximum(time_gb, time_gbes))

plt.xticks(index + bar_width, names)
plt.yticks(np.linspace(0, 1.3 * max_y, 13))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3 * max_y])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Datasets")
plt.ylabel("Fit Time")

plt.show()
```

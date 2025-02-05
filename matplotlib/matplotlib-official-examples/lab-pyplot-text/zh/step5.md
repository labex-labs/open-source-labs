# 添加标题、X 轴标签和 Y 轴标签

我们可以使用 `pyplot` 库的 `title()`、`xlabel()` 和 `ylabel()` 方法为图表添加标题、X 轴标签和 Y 轴标签。我们将添加“电压与时间”作为标题，“时间 [秒]”作为 X 轴标签，“电压 [毫伏]”作为 Y 轴标签。

```python
plt.title(r'Voltage vs Time', fontsize=20)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
```

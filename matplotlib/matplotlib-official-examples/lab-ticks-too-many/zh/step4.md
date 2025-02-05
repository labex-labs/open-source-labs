# 处理日期时间刻度

当在 x 轴上处理日期时间值时，将字符串转换为日期时间对象以获得正确的日期定位器和格式化器非常重要。以下是一个示例：

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建包含日期时间字符串的示例数据
x = ['2021-10-01', '2021-11-02', '2021-12-03', '2021-09-01']
y = [0, 2, 3, 1]

# 将字符串转换为 datetime64
x = np.asarray(x, dtype='datetime64[s]')

# 绘制带有日期时间刻度标签的数据
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.tick_params(axis='x', labelrotation=90)
plt.show()
```

在这个示例中，我们使用 `np.asarray()` 将字符串值转换为 datetime64。当我们再次绘制数据时，刻度标签就符合预期了。

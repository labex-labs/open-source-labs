# 创建一个简单的折线图

让我们从创建一个简单的折线图开始。在这个例子中，我们将绘制区间 [0, 2π] 上的正弦函数和余弦函数。

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```

# 创建一个基本绘图

让我们从创建一个带有文本元素的基本绘图开始。在你的 Python 脚本中，添加以下代码：

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```

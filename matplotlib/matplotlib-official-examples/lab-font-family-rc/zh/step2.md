# 选择特定的无衬线字体

如果我们想使用特定的无衬线字体，可以将`font.sans-serif`参数设置为字体名称列表。Matplotlib 将尝试使用列表中用户系统上可用的第一种字体。为此，我们可以使用以下代码：

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Nimbus Sans"]
```

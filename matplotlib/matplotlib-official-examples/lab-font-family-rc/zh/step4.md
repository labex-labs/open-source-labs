# 选择特定的等宽字体

如果我们想使用特定的等宽字体，可以将`font.monospace`参数设置为字体名称列表。Matplotlib将尝试使用列表中用户系统上可用的第一种字体。为此，我们可以使用以下代码：

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
plt.rcParams["font.monospace"] = ["FreeMono"]
```

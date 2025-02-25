# 単純な折れ線グラフを作成する

まずは簡単な折れ線グラフを作成してみましょう。この例では、区間[0, 2π]における正弦関数と余弦関数をプロットします。

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

# 減衰振動と非減衰振動のプロットを作成する

まず、減衰振動用と非減衰振動用の 2 つのサブプロット付きのグラフを作成します。時間値の配列を作成するために `np.linspace()` 関数を使用し、その後、`np.cos()` 関数と `np.exp()` 関数を使用して、各種類の振動に対応する振幅値をプロットします。

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('damped')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('time (s)')
ax2.set_title('undamped')

fig.suptitle('Different types of oscillations', fontsize=16)

plt.show()
```

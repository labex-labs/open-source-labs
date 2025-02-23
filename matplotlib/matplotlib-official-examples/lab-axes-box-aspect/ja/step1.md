# データに関係なく正方形の軸を作成する

データの制限がどのようなものであっても、正方形の軸を作成します。

```python
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()

ax.set_xlim(300, 400)
ax.set_box_aspect(1)

plt.show()
```

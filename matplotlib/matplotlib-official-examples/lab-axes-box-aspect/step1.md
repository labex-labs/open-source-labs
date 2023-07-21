# A Square Axes, Independent of Data

We will produce a square axes, no matter what the data limits are.

```python
import matplotlib.pyplot as plt
import numpy as np

fig1, ax = plt.subplots()

ax.set_xlim(300, 400)
ax.set_box_aspect(1)

plt.show()
```

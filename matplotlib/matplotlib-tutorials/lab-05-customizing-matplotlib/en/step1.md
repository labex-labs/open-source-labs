# Setting rcParams at runtime

You can dynamically change the default runtime configuration settings in a Python script or interactively from the Python shell. The `matplotlib.rcParams` variable is global to the Matplotlib package and stores all the rc settings. To customize rcParams at runtime, you can modify it directly using the `mpl.rcParams` dictionary. Here's an example:

```python
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
```

This code changes the default line width and line style for all plots created with Matplotlib.

Let's see some random data plotted with the new default settings.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
```

# Import necessary libraries

We first need to import the necessary libraries for generating the animation. We will be using `numpy` for generating random numbers, `matplotlib` for plotting, and `FFMpegWriter` for writing the frames to a file.

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
```

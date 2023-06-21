# Set up the GUI

We start by creating a Tkinter window and setting its title. We also define the size and resolution of the Matplotlib figure we will use.

```python
import tkinter
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
```

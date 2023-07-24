# Import Matplotlib and Set the pgf.texsystem Parameter

First, you need to import the Matplotlib library and set the `pgf.texsystem` parameter to `pdflatex`. This parameter allows you to use LaTeX to customize the font family of your plot.

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```

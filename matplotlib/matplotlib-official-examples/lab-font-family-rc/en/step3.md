# Choose Default Monospace Font

The default monospace font in Matplotlib is determined by the operating system. We can choose to use the default monospace font by setting the `font.family` parameter to `'monospace'`. To do this, we can use the following code:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
```

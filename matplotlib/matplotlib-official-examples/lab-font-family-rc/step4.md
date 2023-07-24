# Choose Specific Monospace Font

If we want to use a specific monospace font, we can set the `font.monospace` parameter to a list of font names. Matplotlib will attempt to use the first font in the list that is available on the user's system. To do this, we can use the following code:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
plt.rcParams["font.monospace"] = ["FreeMono"]
```

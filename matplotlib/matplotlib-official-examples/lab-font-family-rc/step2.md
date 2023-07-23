# Choose Specific Sans-Serif Font

If we want to use a specific sans-serif font, we can set the `font.sans-serif` parameter to a list of font names. Matplotlib will attempt to use the first font in the list that is available on the user's system. To do this, we can use the following code:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Nimbus Sans"]
```

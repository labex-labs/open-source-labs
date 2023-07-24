# Set the Matplotlib font

We need to set the font to be used for Matplotlib text. We will use the Computer Modern font and set it as the default font for Matplotlib.

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```

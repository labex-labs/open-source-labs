# Set up style cycles

We will set up style cycles for the histograms using `cycler`. We will create three style cycles: one for the facecolor, one for the label, and one for the hatch pattern.

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'set {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```

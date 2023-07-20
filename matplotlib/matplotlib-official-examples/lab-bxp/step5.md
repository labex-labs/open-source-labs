# Toggle the display of different elements

We can toggle the display of different elements of the boxplot using various parameters in the `bxp()` function. In this example, we demonstrate how to show or hide the mean, box, caps, notches, and fliers.

```python
# Toggle the display of different elements
plt.bxp(stats, showmeans=True, showbox=False, showcaps=False, shownotches=True, showfliers=False)
plt.show()
```

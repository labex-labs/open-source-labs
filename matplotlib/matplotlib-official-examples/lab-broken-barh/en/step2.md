# Create the broken horizontal bar plot

In this step, we will create the broken horizontal bar plot. We will be using the `broken_barh()` method of the `Axes` class to create the plot. The `broken_barh()` method takes three arguments: the first argument is a list of tuples where each tuple represents a segment of the bar and the first element of the tuple is the starting point of the segment and the second element is the length of the segment; the second argument is the y-coordinate of the bar; and the third argument is the face color of the bar.

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```

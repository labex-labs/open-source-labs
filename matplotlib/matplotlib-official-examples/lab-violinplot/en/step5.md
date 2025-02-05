# Customize plot appearance

We will customize the appearance of the plot by removing y-axis labels and adding a title to the plot.

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```

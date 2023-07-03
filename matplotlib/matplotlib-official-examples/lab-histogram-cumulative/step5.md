# Label the figure

In this step, we will label the figure. We will add a title, gridlines, and labels for the x and y axes.

```python
fig.suptitle("Cumulative Distributions")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("Annual rainfall (mm)")
    ax.set_ylabel("Probability of occurrence")
    ax.label_outer()

plt.show()
```

# 添加图例并显示图形

我们在图形中添加一个图例，以区分未加权模型和加权模型。然后，我们显示该图形。

```python
no_weights_handles, _ = no_weights.legend_elements()
weights_handles, _ = samples_weights.legend_elements()
ax.legend(
    [no_weights_handles[0], weights_handles[0]],
    ["no weights", "with weights"],
    loc="lower left",
)

ax.set(xticks=(), yticks=())
plt.show()
```

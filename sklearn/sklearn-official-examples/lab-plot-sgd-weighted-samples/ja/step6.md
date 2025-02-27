# 凡例を追加してプロットを表示する

重みなしモデルと重み付きモデルを区別するために凡例をプロットに追加します。その後、プロットを表示します。

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

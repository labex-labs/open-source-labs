# グラフにラベルを付ける

このステップでは、グラフにラベルを付けます。タイトル、グリッド線、x軸とy軸のラベルを追加します。

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

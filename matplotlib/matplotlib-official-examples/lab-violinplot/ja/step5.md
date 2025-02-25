# プロットの外観をカスタマイズする

y軸のラベルを削除し、プロットにタイトルを追加することで、プロットの外観をカスタマイズします。

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```

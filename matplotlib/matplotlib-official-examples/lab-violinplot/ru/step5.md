# Настраиваем внешний вид графика

Мы настроим внешний вид графика, удалив метки оси y и добавив заголовок к графику.

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```

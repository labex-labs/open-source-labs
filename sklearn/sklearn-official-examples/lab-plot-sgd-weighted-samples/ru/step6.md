# Добавим легенду и выведем график

Мы добавляем легенду на график, чтобы отличить между моделями без весов и с весами. Затем мы выводим график.

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

# Пометим фигуру

В этом шаге мы присвоим метки фигуре. Добавим заголовок, сетку и метки для осей x и y.

```python
fig.suptitle("Накопленные распределения")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("Годовое количество осадков (мм)")
    ax.set_ylabel("Вероятность наступления")
    ax.label_outer()

plt.show()
```

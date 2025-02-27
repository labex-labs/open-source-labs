# Визуализация результатов

В этом шаге мы визуализируем результаты процесса дискретизации признаков. Мы построим точность классификации на наборе тестовых данных для каждого классификатора и набора данных.

```python
plt.tight_layout()

# Add suptitles above the figure
plt.subplots_adjust(top=0.90)
suptitles = [
    "Линейные классификаторы",
    "Дискретизация признаков и линейные классификаторы",
    "Нелинейные классификаторы",
]
for i, suptitle in zip([1, 3, 5], suptitles):
    ax = axes[0, i]
    ax.text(
        1.05,
        1.25,
        suptitle,
        transform=ax.transAxes,
        horizontalalignment="центр",
        size="x-large",
    )
plt.show()
```

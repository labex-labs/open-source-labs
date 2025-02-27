# Построение графиков вероятностей классов

Мы построим графики вероятностей классов для каждого классификатора и VotingClassifier с использованием столбчатой диаграммы.

```python
N = 4  # количество групп
ind = np.arange(N)  # позиции групп
width = 0.35  # ширина столбца

fig, ax = plt.subplots()

# столбцы для классификаторов 1-3
p1 = ax.bar(ind, np.hstack(([class1_1[:-1], [0]])), width, color="green", edgecolor="k")
p2 = ax.bar(
    ind + width,
    np.hstack(([class2_1[:-1], [0]])),
    width,
    color="lightgreen",
    edgecolor="k",
)

# столбцы для VotingClassifier
p3 = ax.bar(ind, [0, 0, 0, class1_1[-1]], width, color="blue", edgecolor="k")
p4 = ax.bar(
    ind + width, [0, 0, 0, class2_1[-1]], width, color="steelblue", edgecolor="k"
)

# настройка графиков
plt.axvline(2.8, color="k", linestyle="dashed")
ax.set_xticks(ind + width)
ax.set_xticklabels(
    [
        "LogisticRegression\nвес 1",
        "GaussianNB\nвес 1",
        "RandomForestClassifier\nвес 5",
        "VotingClassifier\n(средние вероятности)",
    ],
    rotation=40,
    ha="right",
)
plt.ylim([0, 1])
plt.title("Вероятности классов для примера 1 разных классификаторов")
plt.legend([p1[0], p2[0]], ["класс 1", "класс 2"], loc="upper left")
plt.tight_layout()
plt.show()
```

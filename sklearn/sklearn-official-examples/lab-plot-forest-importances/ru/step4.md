# Важность признаков на основе среднего уменьшения нечистоты

Важность признаков предоставляется атрибутом `feature_importances_` обученной модели, и она вычисляется как среднее и стандартное отклонение накопления уменьшения нечистоты внутри каждого дерева. Мы построим график важности признаков, основанный на нечистоте.

```python
start_time = time.time()
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
elapsed_time = time.time() - start_time

print(f"Время, затраченное на вычисление важностей: {elapsed_time:.3f} секунд")

forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Важность признаков с использованием MDI")
ax.set_ylabel("Среднее уменьшение нечистоты")
fig.tight_layout()
```

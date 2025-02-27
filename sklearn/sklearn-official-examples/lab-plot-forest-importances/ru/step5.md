# Важность признаков на основе перестановки признаков

Важность признаков при перестановке преодолевает ограничения важности признаков, основанной на нечистоте: они не имеют предвзятости по отношению к признакам с высокой基数 и могут быть вычислены на оставшемся тестовом наборе. Мы вычислим полную важность при перестановке. Признаки перемешиваются n раз, и модель переобучается для оценки их важности. Мы построим график ранжирования важности.

```python
start_time = time.time()
result = permutation_importance(
    forest, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
elapsed_time = time.time() - start_time
print(f"Время, затраченное на вычисление важностей: {elapsed_time:.3f} секунд")

forest_importances = pd.Series(result.importances_mean, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Важность признаков с использованием перестановки на всей модели")
ax.set_ylabel("Среднее уменьшение точности")
fig.tight_layout()
plt.show()
```

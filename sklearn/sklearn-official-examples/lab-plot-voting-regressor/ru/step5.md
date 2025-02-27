# Построим графики результатов

Наконец, мы визуализируем 20 предсказаний. Красные звёзды показывают среднее предсказание, сделанное Регурессором голосования.

```python
# Plot the results
plt.figure()
plt.plot(pred1, "gd", label="GradientBoostingRegressor")
plt.plot(pred2, "b^", label="RandomForestRegressor")
plt.plot(pred3, "ys", label="LinearRegression")
plt.plot(pred4, "r*", ms=10, label="VotingRegressor")

plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.ylabel("предсказанное")
plt.xlabel("тренировочные образцы")
plt.legend(loc="best")
plt.title("Предсказания регрессоров и их среднее")

plt.show()
```

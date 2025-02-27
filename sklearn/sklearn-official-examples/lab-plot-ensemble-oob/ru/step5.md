# Визуализируем ошибку вне пакета (Out-Of-Bag, OOB)

Наконец, мы построим график ошибки вне пакета для каждого классификатора в зависимости от количества оценщиков. Это позволит нам определить количество оценщиков, при котором ошибка стабилизируется. Мы будем использовать Matplotlib для создания графика.

```python
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("OOB error rate")
plt.legend(loc="upper right")
plt.show()
```

# Диаграмма рассеяния

Мы также можем создать диаграмму рассеяния, чтобы показать связь между двумя категориальными переменными. В этом случае мы будем использовать те же данные о фруктах и добавить некоторый случайный шум к значениям количества, чтобы создать вторую переменную.

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```

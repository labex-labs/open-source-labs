# Доступ к полям

Если объект ndarray является структурированным массивом, поля массива можно получить доступ к путём индексирования массива строками, подобно словарю.

```python
x = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('a', np.int32), ('b', np.int32)])
print(x['a'])  # Вывод: [1, 3, 5]
```

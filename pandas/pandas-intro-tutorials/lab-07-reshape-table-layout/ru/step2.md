# Сортировка строк таблицы

Отсортируйте набор данных о титанике по возрасту пассажиров, а затем по классу кают и возрасту в порядке убывания.

```python
# Сортировка по возрасту
titanic.sort_values(by="Age").head()

# Сортировка по Pclass и возрасту в порядке убывания
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```

# Настраиваем стиль графика

Мы можем изменить стиль нашего графика, чтобы сделать его более наглячным. Следуйте шагам:

1. Выведите список доступных стилей с использованием `print(plt.style.available)`.

```python
print(plt.style.available)
```

2. Выберите стиль и примените его с использованием `plt.style.use(style_name)`.

```python
plt.style.use('fivethirtyeight')
```

3. Посмотрим на график снова.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```

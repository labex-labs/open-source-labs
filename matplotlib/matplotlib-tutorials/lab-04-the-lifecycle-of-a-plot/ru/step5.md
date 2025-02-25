# Настраиваем внешний вид графика

Мы можем дальнейшим образом настроить внешний вид нашего графика. Следуйте шагам:

1. Поворачиваем метки оси x, чтобы они были более читаемыми.

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. Задаем пределы оси x и оси y, метки и заголовок.

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

3. Показываем график снова.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```

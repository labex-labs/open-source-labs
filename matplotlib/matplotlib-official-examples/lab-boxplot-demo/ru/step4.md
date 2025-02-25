# Настраиваем ящик с усами

Мы можем настроить ящик с усами, изменив внешний вид коробки, усов и выбросов. Мы также можем создать несколько ящиков с усами на одном графике, чтобы сравнить разные группы данных. Вот некоторые примеры того, как настроить ящик с усами:

```python
# Создаем ящик с усами с вырезом
plt.boxplot(data, notch=True)
plt.show()

# Меняем символы точек выбросов на зеленые ромбы
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# Создаем горизонтальные ящики с усами
plt.boxplot(data, vert=False)
plt.show()

# Создаем несколько ящиков с усами на одном графике
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```

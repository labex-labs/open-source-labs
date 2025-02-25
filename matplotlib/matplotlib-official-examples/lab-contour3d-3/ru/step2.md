# Создаем трехмерную фигуру и данные

В этом шаге мы создадим трехмерную фигуру и получим тестовые данные для поверхностной диаграммы.

```python
# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Get test data for the surface plot
X, Y, Z = axes3d.get_test_data(0.05)
```

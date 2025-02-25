# Создаем трехмерную линейную диаграмму

Для второго подграфика мы создадим трехмерную линейную диаграмму. Мы будем использовать функцию `get_test_data` из mpl_toolkits.mplot3d.axes3d для создания данных для диаграммы.

```python
# Create data for the 3D wireframe plot
X, Y, Z = Axes3D.get_test_data(0.05)

# Plot the 3D wireframe plot
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```

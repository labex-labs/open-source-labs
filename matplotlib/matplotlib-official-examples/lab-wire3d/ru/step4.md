# Настроить график

Мы можем настроить график, чтобы сделать его более наглядным. В этом примере мы добавим заголовок, метки осей и изменим цвет графика.

```python
# Customize the plot
ax.set_title('Wireframe Plot')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='green')
```

# Проекция профилей контура

Теперь мы проектируем профили контура на стены графика. Это делается с использованием метода `contourf`. Мы установим параметр `zdir` в 'z', 'x' и 'y', чтобы проектировать профили контура на стены z, x и y соответственно. Также мы установим параметр `offset`, чтобы соответствовать соответствующим пределам осей.

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```

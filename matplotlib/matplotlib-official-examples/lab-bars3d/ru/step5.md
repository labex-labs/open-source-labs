# Настройка осей

Теперь мы настроим оси трехмерного графика. Мы установим метки для осей x, y и z с использованием методов `set_xlabel()`, `set_ylabel()` и `set_zlabel()` соответственно. Мы также установим деления на оси y с использованием метода `set_yticks()`.

```python
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_yticks(yticks)
```

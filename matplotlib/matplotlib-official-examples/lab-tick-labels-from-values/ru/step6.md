# Задаем форматтер и локатор делений

Мы задаем форматтер делений оси x нашей созданной в шаге 5 функцией форматирования с использованием метода `set_major_formatter()`. Также задаем локатор делений оси x `MaxNLocator(integer=True)` для обеспечения того, чтобы значения делений были целыми числами.

```python
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```

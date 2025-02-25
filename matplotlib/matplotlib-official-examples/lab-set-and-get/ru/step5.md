# Алиасы

Для сокращения количества нажатий клавиш в интерактивном режиме у ряда свойств есть короткие алиасы, например, 'lw' для 'linewidth' и'mec' для'markeredgecolor'. При вызове set или get в режиме интроспекции эти свойства будут перечислены в виде 'fullname' или 'aliasname'.

```python
l1, l2 = plt.plot([1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5])
plt.setp(l1, linewidth=2, color='r')
plt.setp(l2, linewidth=1, color='g')
```

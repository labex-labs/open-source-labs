# Сохранить график

Вы можете сохранить график в виде изображения с помощью метода `savefig`. Следующий код сохраняет график в виде PNG-изображения:

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.savefig('simple_plot.png')
```

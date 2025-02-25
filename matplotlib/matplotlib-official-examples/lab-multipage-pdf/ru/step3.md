# Создайте первую страницу

В этом шаге вы создадите первую страницу PDF-файла. На странице будет график простой линии.

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```

# Выборочная подвыборка каждой 6 - ой погрешностной полосы

Теперь давайте применим выборочную подвыборку погрешностных полос для построения только каждой 6 - ой погрешностной полосы. Мы можем сделать это, используя параметр `errorevery` функции `errorbar`.

```python
fig, ax = plt.subplots()

ax.set_title('Every 6th Errorbar')
ax.errorbar(x, y1, yerr=y1err, errorevery=6, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=6, label='y2')

ax.legend()
plt.show()
```

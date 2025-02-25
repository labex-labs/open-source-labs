# Создание графика

Мы создадим график и добавим `PathPatch` на график. Мы установим заголовок графика в `'Составной путь'`.

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```

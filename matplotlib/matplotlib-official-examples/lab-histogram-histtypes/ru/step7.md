# Создаем две гистограммы с накопленными столбцами

Мы можем создать две гистограммы с накопленными столбцами, вызвав функцию `hist` дважды и установив параметр `histtype` в `'barstacked'`. В этом примере мы создадим две гистограммы с накопленными столбцами.

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```

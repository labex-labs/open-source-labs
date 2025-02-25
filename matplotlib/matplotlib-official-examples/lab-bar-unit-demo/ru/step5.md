# Создаем гистограмму

Следующим шагом является создание гистограммы. Мы будем использовать функцию `bar()` для создания графика. Мы создадим два набора столбцов, один для чая и один для кофе. Также добавим на график ошибочные столбцы.

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```

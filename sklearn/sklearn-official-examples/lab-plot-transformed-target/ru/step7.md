# Построим графики распределений целевого признака для данных о недвижимости в Амесе

Построим функции плотности вероятности целевого признака до и после применения QuantileTransformer.

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_ylabel("Вероятность")
ax0.set_xlabel("Целевой признак")
ax0.set_title("Распределение целевого признака")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("Вероятность")
ax1.set_xlabel("Целевой признак")
ax1.set_title("Распределение преобразованного целевого признака")

f.suptitle("Данные о недвижимости в Амесе: цена продажи", y=1.05)
plt.tight_layout()
```

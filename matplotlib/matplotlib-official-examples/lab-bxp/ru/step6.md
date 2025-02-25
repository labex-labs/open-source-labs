# Настраиваем отображение различных элементов

Мы можем настроить отображение различных элементов ящика с усами, используя различные параметры в функции `bxp()`. В этом примере мы демонстрируем, как настроить коробку, медиану, выбросы, точку среднего значения и линию среднего значения.

```python
# Customize the display of different elements
boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12, linestyle='none')
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

plt.bxp(stats, boxprops=boxprops, flierprops=flierprops, medianprops=medianprops, meanprops=meanpointprops, meanline=True, showmeans=True)
plt.show()
```

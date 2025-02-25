# Personalizar la visualización de diferentes elementos

Podemos personalizar la visualización de diferentes elementos del diagrama de caja utilizando varios parámetros en la función `bxp()`. En este ejemplo, demostramos cómo personalizar la caja, la mediana, los valores atípicos, el punto de la media y la línea de la media.

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

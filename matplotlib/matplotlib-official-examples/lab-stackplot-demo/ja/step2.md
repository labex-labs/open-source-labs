# スタックプロットの作成

2 番目のステップは、`stackplot()`関数を使ってスタックプロットを作成することです。1950 年から 2018 年までの各大陸別の世界人口のスタックプロットを作成するために、国連の世界人口見通し（2019 年改訂版）のデータを使います。

```python
# 国連の世界人口見通し（2019 年改訂版）のデータ
# https://population.un.org/wpp/, ライセンス：CC BY 3.0 IGO
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
population_by_continent = {
    'africa': [228, 284, 365, 477, 631, 814, 1044, 1275],
    'americas': [340, 425, 519, 619, 727, 840, 943, 1006],
    'asia': [1394, 1686, 2120, 2625, 3202, 3714, 4169, 4560],
    'europe': [220, 253, 276, 295, 310, 303, 294, 293],
    'oceania': [12, 15, 19, 22, 26, 31, 36, 39],
}

fig, ax = plt.subplots()
ax.stackplot(year, population_by_continent.values(),
             labels=population_by_continent.keys(), alpha=0.8)
ax.legend(loc='upper left', reverse=True)
ax.set_title('World population')
ax.set_xlabel('Year')
ax.set_ylabel('Number of people (millions)')

plt.show()
```

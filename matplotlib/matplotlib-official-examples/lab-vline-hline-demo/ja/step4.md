# グラフを作成する

ここでは、Matplotlib の `subplots` 関数を使ってグラフを作成します。垂直線用のサブプロットと水平線用のサブプロットをそれぞれ 1 つずつ作成します。視認性を向上させるために、グラフのサイズを (12, 6) に設定します。

```python
# Create the plot
fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))
```

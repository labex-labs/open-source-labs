# グラフと軸を作成する

グラフオブジェクトを作成し、それに1セットの軸を追加します。また、グラフのタイトルも設定します。

```python
fig = plt.figure(figsize=(8, 9))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Rankine Power Cycle: Example 8.6 from Moran and "
                     "Shapiro\n\x22Fundamentals of Engineering Thermodynamics "
                     "\x22, 6th ed., 2008")
```

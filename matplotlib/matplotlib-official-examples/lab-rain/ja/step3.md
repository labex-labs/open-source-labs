# 散布図を作成する

次に、雨滴が成長するにつれてアニメーションの間に更新する散布図を作成します。

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```

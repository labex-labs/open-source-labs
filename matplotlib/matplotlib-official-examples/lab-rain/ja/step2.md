# 雨のデータを作成する

次に、雨のデータを作成します。ランダムな位置に、ランダムな成長率と、ランダムな色を持つ50個の雨滴を作成します。

```python
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, (2,)),
                                      ('size',     float),
                                      ('growth',   float),
                                      ('color',    float, (4,))])

rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)
```

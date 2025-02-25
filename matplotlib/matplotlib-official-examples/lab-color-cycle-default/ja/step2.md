# プロパティサイクルを定義して色を取得する

次に、プロパティサイクルを定義して、そこから色を取得する必要があります。

```python
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
```

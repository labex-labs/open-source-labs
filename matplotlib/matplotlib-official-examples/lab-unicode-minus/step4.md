# Setting the Tick Labels

By default, tick labels at negative values are rendered using a Unicode minus rather than an ASCII hyphen. However, we can change this behavior by setting `axes.unicode_minus` to `False`.

```python
plt.rcParams['axes.unicode_minus'] = False
```

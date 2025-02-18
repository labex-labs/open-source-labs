# テキストボックス用のテキストを作成する

データの平均、中央値、および標準偏差を含む文字列を作成します。

```python
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))
```

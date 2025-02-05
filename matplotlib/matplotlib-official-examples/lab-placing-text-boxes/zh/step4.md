# 创建文本框的文本内容

我们将创建一个包含数据均值、中位数和标准差的字符串。

```python
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))
```

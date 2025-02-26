# `import as` 文

インポートする際にモジュールの名前を変更することができます。

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

通常のインポートと同じように機能します。ただ、その1つのファイル内でモジュールの名前を変更するだけです。

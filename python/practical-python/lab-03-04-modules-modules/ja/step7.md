# `from` モジュール import

これは、モジュールから選択されたシンボルを抽出し、それらをローカルで利用可能にします。

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

これにより、モジュールの一部を使用する際にモジュール接頭辞を入力する必要がなくなります。頻繁に使用する名前に便利です。

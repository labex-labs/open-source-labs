# Matplotlibをインポートしてon_close関数を定義する

このステップでは、Matplotlibをインポートし、グラフが閉じたときに呼び出される`on_close`関数を定義します。この関数は、コンソールにメッセージを出力するだけです。

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```

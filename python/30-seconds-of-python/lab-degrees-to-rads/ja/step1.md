# 度からラジアンへ

引数として度で表された角度を受け取り、ラジアンで表された角度を返す関数 `degrees_to_rads(deg)` を作成します。関数は、次の式を使用して度をラジアンに変換する必要があります。

```
radians = (degrees * pi) / 180.0
```

ここで、`pi` は円の周囲の長さと直径の比を表す定数値であり（約 3.14159）、`degrees` は度で表された角度です。

関数は、4 桁の小数で丸めたラジアンで表された角度を返す必要があります。

```python
from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0
```

```python
degrees_to_rads(180) # ~3.1416
```

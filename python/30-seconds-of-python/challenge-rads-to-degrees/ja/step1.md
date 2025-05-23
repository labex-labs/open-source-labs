# ラジアンから度へのチャレンジ

## 問題

`rads_to_degrees` という Python 関数を書きましょう。この関数は、1 つの引数 `rad` を受け取ります。`rad` は、ラジアンで表される角度を表す浮動小数点数です。関数は、度で表される角度を浮動小数点数として返す必要があります。ラジアンから度に角度を変換するには、次の式を使用できます。

```
degrees = radians * (180 / pi)
```

ここで、`pi` は、円の周囲の長さと直径の比を表す定数で、およそ 3.14159 に等しい値です。

あなたの関数は、`math` モジュールから `pi` 定数をインポートする必要があります。

## 例

あなたの関数がどのように機能するかの例を以下に示します。

```python
from math import pi

assert rads_to_degrees(pi / 2) == 90.0
```

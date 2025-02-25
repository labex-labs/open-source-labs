# 華氏から摂氏への変換

引数として華氏の温度を受け取り、摂氏の温度を返す関数`fahrenheit_to_celsius(degrees)`を作成します。この関数は、変換式`C = (F - 32) * 5 / 9`に従う必要があります。ここで、`C`は摂氏の温度であり、`F`は華氏の温度です。

```python
def fahrenheit_to_celsius(degrees):
  return ((degrees - 32) * 5 / 9)
```

```python
fahrenheit_to_celsius(77) # 25.0
```

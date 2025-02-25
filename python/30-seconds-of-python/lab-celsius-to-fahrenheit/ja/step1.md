# 摂氏から華氏へ

摂氏で表された温度を引数として受け取り、華氏で表された温度を返す関数 `celsius_to_fahrenheit` を作成します。摂氏を華氏に変換するには、変換式 `F = 1.8 * C + 32` を使用します。

```python
def celsius_to_fahrenheit(degrees):
  return ((degrees * 1.8) + 32)
```

```python
celsius_to_fahrenheit(180) # 356.0
```

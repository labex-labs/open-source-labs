# 華氏を摂氏に変換する関数を定義する

次に、華氏の温度を摂氏に変換する関数を定義します。

```python
def fahrenheit2celsius(temp):
    """
    Returns temperature in Celsius given Fahrenheit temperature.
    """
    return (5. / 9.) * (temp - 32)
```

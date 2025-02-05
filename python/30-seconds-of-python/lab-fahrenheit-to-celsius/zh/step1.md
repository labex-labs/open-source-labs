# 华氏度到摄氏度的转换

编写一个函数 `fahrenheit_to_celsius(degrees)`，它接受一个华氏温度作为参数，并返回对应的摄氏温度。该函数应遵循转换公式 `C = (F - 32) * 5 / 9`，其中 `C` 是摄氏温度，`F` 是华氏温度。

```python
def fahrenheit_to_celsius(degrees):
  return ((degrees - 32) * 5 / 9)
```

```python
fahrenheit_to_celsius(77) # 25.0
```

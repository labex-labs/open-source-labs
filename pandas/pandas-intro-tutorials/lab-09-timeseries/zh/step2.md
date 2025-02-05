# 将字符串转换为日期时间对象

“datetime”列中的日期目前是字符串。我们要将这些字符串转换为日期时间对象，以便于操作。

```python
# 将“datetime”列转换为日期时间对象
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```

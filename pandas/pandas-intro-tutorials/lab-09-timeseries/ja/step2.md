# 文字列を日付時刻オブジェクトに変換する

「datetime」列の日付は現在文字列です。これらを日付時刻オブジェクトに変換して、操作を簡単にするためです。

```python
# "datetime" 列を日付時刻オブジェクトに変換する
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
```

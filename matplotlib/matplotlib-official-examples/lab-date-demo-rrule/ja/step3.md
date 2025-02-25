# 再帰ルールを設定する

5 年に 1 度のイースターにカスタム日付目盛りを設定することになります。これを行うには、`rrulewrapper` 関数を使用して再帰ルールを設定する必要があります。

```python
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
```

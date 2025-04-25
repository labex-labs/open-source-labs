# 设置循环规则

你将在每隔 5 年的复活节设置自定义日期刻度。为此，你需要使用 `rrulewrapper` 函数设置循环规则。

```python
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
```

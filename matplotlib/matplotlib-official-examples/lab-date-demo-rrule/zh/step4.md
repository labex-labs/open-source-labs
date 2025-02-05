# 设置刻度定位器和格式化器

你将使用 `RRuleLocator` 函数，根据上一步设置的循环规则来设置刻度定位器。你还将使用 `DateFormatter` 函数来设置刻度格式化器。

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```

# 目盛りの配置器 (tick locator) と書式設定器 (formatter) を設定する

前のステップで設定した再帰ルール (recurrence rule) に基づいて、`RRuleLocator` 関数を使用して目盛りの配置器を設定します。また、`DateFormatter` 関数を使用して目盛りの書式設定器を設定します。

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```

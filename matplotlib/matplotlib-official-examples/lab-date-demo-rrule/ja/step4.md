# 目盛りの位置付けと書式設定を行う

前のステップで設定した再帰ルールに基づいて、目盛りの位置付けを行うために `RRuleLocator` 関数を使用します。また、目盛りの書式設定を行うために `DateFormatter` 関数を使用します。

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```

# Set the tick locator and formatter

You will use the RRuleLocator function to set the tick locator based on the recurrence rule you set in the previous step. You will also use the DateFormatter function to set the tick formatter.

```python
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
```

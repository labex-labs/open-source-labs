# 替换列中的值

最后，让我们替换“Sex”列中的值：将“male”替换为“M”，“female”替换为“F”。我们将为此使用`replace()`方法。

```python
# 在“Sex”列中，将“male”替换为“M”，“female”替换为“F”
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
```

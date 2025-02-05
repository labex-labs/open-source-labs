# 订阅信号

要订阅一个信号，使用信号的 `connect` 方法。提供一个在信号发出时应该被调用的函数：

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```

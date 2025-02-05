# 将滑块与更新函数连接

在这一步中，你将把滑块与更新函数连接起来。这将确保每当滑块值发生变化时，绘图都会更新。

```python
sfreq.on_changed(update)
samp.on_changed(update)
```

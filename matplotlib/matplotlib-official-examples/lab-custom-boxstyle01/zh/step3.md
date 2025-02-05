# 向 Matplotlib 注册自定义框样式

一旦你将自定义框样式实现为类，就可以向 Matplotlib 注册它。这样你就可以将框样式指定为字符串，即 `bbox=dict(boxstyle="已注册的名称,参数=值,...",...)`。

```python
BoxStyle._style_list["angled"] = MyStyle  # 注册自定义样式。
```

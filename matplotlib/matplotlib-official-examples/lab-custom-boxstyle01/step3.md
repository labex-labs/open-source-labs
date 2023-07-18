# Register the custom box style with Matplotlib

Once you have implemented a custom box style as a class, you can register it with Matplotlib. This allows you to specify the box style as a string, `bbox=dict(boxstyle="registered_name,param=value,...", ...)`.

```python
BoxStyle._style_list["angled"] = MyStyle  # Register the custom style.
```

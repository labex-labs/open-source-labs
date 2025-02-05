# 注册自定义单位类

在这一步中，我们将把自定义单位类——`Foo`——与转换器类——`FooConverter`——进行注册。

```python
units.registry[Foo] = FooConverter()
```

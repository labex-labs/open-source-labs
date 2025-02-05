# Register the Custom Unit Class

In this step, we will register the custom unit class - `Foo` - with the converter class - `FooConverter`.

```python
units.registry[Foo] = FooConverter()
```

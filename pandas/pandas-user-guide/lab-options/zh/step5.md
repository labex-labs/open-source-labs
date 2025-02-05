# 使用 option_context

`option_context` 函数允许我们在一组选项的环境下执行一个代码块，这些选项在执行后会恢复到之前的设置。

```python
# 使用一组选项执行一个代码块
with pd.option_context("display.max_rows", 10):
    # 尽管全局设置不同，这里仍会打印 10
    print(pd.get_option("display.max_rows"))

# 由于上下文块已结束，这里会打印全局设置
print(pd.get_option("display.max_rows"))
```

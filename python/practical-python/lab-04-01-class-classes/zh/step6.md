# 类作用域

类并不定义名称作用域。

```python
class Player:
 ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # 错误。调用全局 `move` 函数
        self.move(-amt, 0)  # 正确。调用上面的方法 `move`。
```

如果你想对实例进行操作，你总是要显式地引用它（例如，`self`）。

从这组练习开始，我们将对前面章节中的现有代码进行一系列更改。你必须有一个能正常运行的练习 3.18 版本才能开始。如果你没有，请到 `Solutions/3_18` 目录中找到解决方案代码并使用。复制它也可以。
